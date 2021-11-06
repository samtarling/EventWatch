import time
import re
from pywikibot.comms.eventstreams import EventStreams
import pywikibot
import mwparserfromhell
import pymysql
import constants
import discordNotify


watchedPages = []
watchedPageRegex = []


def getUserScore(user: str):
    '''Get a user's score'''
    if constants.SCORING:
        db = pymysql.connect(
            host=constants.DB_HOST,
            user=constants.DB_USER,
            password=constants.DB_PASS,
            database=constants.DB_NAME
        )
        cursor = db.cursor()
        sql = f"SELECT score FROM user_score WHERE user_name = '{user}'"
        if cursor.execute(sql):
            for item in cursor.fetchall():
                db.close()
                return item[0]
        else:
            db.close()
            return 0
    else:
        return 0


def updateScore(user: str):
    '''Updates a user's score in the database'''
    if constants.SCORING:
        db = pymysql.connect(
            host=constants.DB_HOST,
            user=constants.DB_USER,
            password=constants.DB_PASS,
            database=constants.DB_NAME
        )
        cursor = db.cursor()
        datetime = time.strftime('%Y-%m-%d %H:%M:%S')
        sql = f"INSERT INTO user_score (user_name, last_update) VALUES ('{user}','{datetime}') ON DUPLICATE KEY UPDATE last_update = '{datetime}', score=score-1"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()


def checkPageTitle(title: str):
    '''Checks if a given title is in the watchlist'''
    global watchedPages
    global watchedPageRegex
    if title in watchedPages:
        return True
    else:
        for regex in watchedPageRegex:
            title_regex = re.compile(regex.strip_code(), re.IGNORECASE)
            if title_regex.findall(title):
                return True
    return False


def addPageWatch(title: str):
    '''Add a given title to the watchlist'''
    global watchedPages
    if title not in watchedPages:
        watchedPages.append(title)


def addPageRegexWatch(title: str):
    '''Add a given title regex to the watchlist'''
    global watchedPageRegex
    if title not in watchedPageRegex:
        watchedPageRegex.append(title)


def getPage(title: str):
    '''Get a Page object'''
    site = pywikibot.Site(constants.SITE)
    page = pywikibot.Page(site, title)
    return page


def readWatchList(title: str):
    '''Read the watchlist data from a given Wiki page'''
    page = getPage(title)
    text = page.get()
    wikitext = mwparserfromhell.parse(text)

    for section in wikitext.get_sections(include_lead=False):
        section_title = section.nodes[0]
        if section_title == '== Exact ==':
            for link in section.filter_wikilinks():
                addPageWatch(link.title)
        elif section_title == '== Regex ==':
            for link in section.filter_wikilinks():
                addPageRegexWatch(link.title)

    print(watchedPages)
    print(watchedPageRegex)
    print(f"Watchlists updated from [{constants.LINK_URL}{constants.WATCHLIST}]")
    if constants.DISCORD:
        discordNotify.sendPlain(f"Watchlists updated from [{constants.LINK_URL}{constants.WATCHLIST}]")


def createDiffLink(change: str, short: bool):
    '''Generate a diff link'''
    revision = change['revision']['new']
    if short:
        return f"http://enwp.org/Special:Diff/{revision}"
    else:
        return f"{constants.LINK_URL}Special:Diff/{revision}"


def createLogMessage(change, code: str):
    '''Create and display a log message'''
    diffLink = createDiffLink(change, True)
    user = change['user']
    comment = change['comment']
    title = change['title']
    if constants.SCORING:
        score = getUserScore(user)
        logMessage = f"[{code}] {user} [s:{score}] edited {title} (`{comment}`) [{diffLink}]"
    else:
        logMessage = f"[{code}] {user} edited {title} (`{comment}`) [{diffLink}]"
    return logMessage


def handleWatchlistUpdate():
    '''Handle the watchlist page being edited'''
    global watchedPages
    global watchedPageRegex

    watchedPages = []
    watchedPageRegex = []

    print('Watchlist was edited, updating..')
    if constants.DISCORD:
        discordNotify.sendPlain('Watchlist was edited, updating..')
    readWatchList(constants.WATCHLIST)


def handleWLEvent(change):
    '''Handle a watchlist match'''
    user = change['user']
    if constants.SCORING:
        updateScore(user)
    logMessage = createLogMessage(change, 'wl/t')
    print(logMessage)
    if constants.DISCORD:
        discordNotify.sendPlain(logMessage)


def checkEvent(change):
    '''Check a change for any events to fire'''
    if change['bot'] is False:
        title = change['title']

        if title == constants.WATCHLIST:
            handleWatchlistUpdate()

        if checkPageTitle(title):
            handleWLEvent(change)


def streamEdits():
    '''Stream edits'''
    stream = EventStreams(
        streams=[
            'recentchange',
            'revision-create'
        ]
    )
    stream.register_filter(
        server_name=constants.FULL_SITE,
        type='edit'
    )
    print('Filtering events...')
    while stream:
        change = next(iter(stream))
        checkEvent(change)


def main():
    '''Set up EventWatch and stream edits'''
    global watchedPages
    global watchedPageRegex

    if constants.DISCORD:
        discordNotify.sendPlain(f"CVNwatch v{constants.VERSION} starting...")
    print(f"CVNwatch v{constants.VERSION} starting...")

    if constants.SCORING:
        if constants.DISCORD:
            discordNotify.sendPlain('[scoring mode: ON]')
        print('[scoring mode: ON]')
    else:
        if constants.DISCORD:
            discordNotify.sendPlain('[scoring mode: OFF]')
        print('[scoring mode: OFF]')

    readWatchList(constants.WATCHLIST)

    print('Starting streaming...')
    if constants.DISCORD:
        discordNotify.sendPlain('Starting streaming...')
    streamEdits()


if __name__ == "__main__":
    main()
