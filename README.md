# EventWatch
**oof** this ain't much right yet, but I'll probably make it into a proper Discord bot instead of using a webhook :-)

## `.env` setup
### Required
#### `SITE`
The Wikimedia site identifier (en for en.wikipedia.org)
#### `FULL_SITE`
The full URI for the Wikimedia site, excluding the `https`
#### `WATCHLIST`
The page name for the watchlist, set up as detailed below

### Required for `Discord`
#### `WEBHOOK`
Discord webhook URL

### Required for `Scoring`
#### `DB_HOST`
Database host
#### `DB_USER`
Database username
#### `DB_PASS`
Database password
#### `DB_NAME`
Database to use


## Example `.env` file
```
SITE="en"
FULL_SITE="en.wikipedia.org"
WATCHLIST="User:TheresNoTime/testlist"

WEBHOOK="{nice try}"

DB_HOST="127.0.0.1"
DB_USER="root"
DB_PASS="l33t"
DB_NAME="eventwatch"
```

## `constants.py` setup
Please also note the following lines in `constants.py`, which turn on/off "features":
```python
# Config
SCORING = False  # Use db scoring
DISCORD = True   # Use Discord notifications
```

## `Watchlist` page setup
At the moment, the watchlist page is pretty specific - it **must** be set up as below:

```
== Exact ==
* [[User:TheresNoTime/sandbox]]
* [[User talk:TheresNoTime]]
* [[Wikipedia:Administrator intervention against vandalism]]

== Regex ==
* [[User:TheresNoTime/.*]]
* [[^Hurricane.*]]
* [[^Typhoon.*]]
* [[^Cyclone.*]]

```

## TODO

- [ ] Add docstrings/blocks, type hints etc to functions, you scrub.
- [ ] Lots of lines are too damn long!
- [ ] Basically *get good* at Python.
- [ ] Move away from using a webhook and create a bot.
- [ ] Finish user scoring
- [ ] Add user watching