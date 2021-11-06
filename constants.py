import os
import typing
import dotenv

dotenv.load_dotenv()

# Version
VERSION = "1.0.0"

# Config
SCORING = False  # Use db scoring
DISCORD = True  # Use Discord notifications

# Constants
SITE = typing.cast(
    str,
    os.getenv('SITE')
)  # type: ignore
FULL_SITE = typing.cast(
    str,
    os.getenv('FULL_SITE')
)  # type: ignore
WATCHLIST = typing.cast(
    str,
    os.getenv('WATCHLIST')
)  # type: ignore
WEBHOOK = typing.cast(
    str,
    os.getenv('WEBHOOK')
)  # type: ignore
DB_HOST = typing.cast(
    str,
    os.getenv('DB_HOST')
)  # type: ignore
DB_USER = typing.cast(
    str,
    os.getenv('DB_USER')
)  # type: ignore
DB_PASS = typing.cast(
    str,
    os.getenv('DB_PASS')
)  # type: ignore
DB_NAME = typing.cast(
    str,
    os.getenv('DB_NAME')
)  # type: ignore

# Generated
LINK_URL = typing.cast(
    str,
    f"https://{FULL_SITE}/wiki/"
)  # type: ignore
