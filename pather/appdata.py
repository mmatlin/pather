from configparser import ConfigParser
from pathlib import Path

import yaml
from appdirs import user_data_dir


def _get_appdata_location():
    return Path(
        user_data_dir(appname="pather", appauthor=False, roaming=True)
    ).resolve()


APPDATA = _get_appdata_location()

_STORE_PATH = APPDATA / "pather_store"
STORE_SRC_PATH = _STORE_PATH / "pather_store"
SCRIPTS_PATH = APPDATA / "scripts.yaml"


def initialize_store():
    STORE_SRC_PATH.mkdir(parents=True, exist_ok=True)
    (STORE_SRC_PATH / "__init__.py").touch()
    (STORE_SRC_PATH / "run.py").touch()
    (STORE_SRC_PATH / "scripts").mkdir(parents=True, exist_ok=True)


def initialize_appdata():
    initialize_store()

    SCRIPTS_PATH.touch()
    with open(SCRIPTS_PATH, "w") as scripts_file:
        yaml.safe_dump(dict(), scripts_file)

    (APPDATA / "setup.cfg").touch()
    (APPDATA / "setup.py").touch()
