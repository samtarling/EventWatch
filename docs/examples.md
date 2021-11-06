# Examples

## Example `Event` from `EventStream`
```json
{
    "$schema": "/mediawiki/recentchange/1.0.0",
    "meta": {
        "uri": "https://en.wikipedia.org/wiki/User:Deisenbe/sandbox/Reichenthal",
        "request_id": "1ee2eed1-5bb4-434a-9b3c-b2948fc6c056",
        "id": "b668d491-76d9-4131-8111-e7a9e092d540",
        "dt": "2021-11-06T13:57:01Z",
        "domain": "en.wikipedia.org",
        "stream": "mediawiki.recentchange",
        "topic": "eqiad.mediawiki.recentchange",
        "partition": 0,
        "offset": 3416667519
    },
    "id": 1440399890,
    "type": "edit",
    "namespace": 2,
    "title": "User:Deisenbe/sandbox/Reichenthal",
    "comment": "/* Early life */",
    "timestamp": 1636207021,
    "user": "Deisenbe",
    "bot": False,
    "minor": False,
    "length": {
        "old": 14012,
        "new": 14020
    },
    "revision": {
        "old": 1053855113,
        "new": 1053855737
    },
    "server_url": "https://en.wikipedia.org",
    "server_name": "en.wikipedia.org",
    "server_script_path": "/w",
    "wiki": "enwiki",
    "parsedcomment": "<span dir='auto'><span class='autocomment'><a href='/wiki/User:Deisenbe/sandbox/Reichenthal#Early_life' title='User:Deisenbe/sandbox/Reichenthal'>→\u200eEarly life</a></span></span>'
}
```