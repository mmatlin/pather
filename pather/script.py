from pathlib import Path
from uuid import uuid4

import yaml

from .appdata import SCRIPTS_PATH, STORE_SRC_PATH


def _generate_mangle():
    return str(uuid4())[:8]


class Script:
    def __init__(self, cli_name, orig_path, mangle=None):
        self.cli_name = cli_name
        self._orig_path = Path(orig_path)
        if mangle is None:
            self._mangle = _generate_mangle()
        else:
            self._mangle = mangle
        self.path = STORE_SRC_PATH / "scripts" / self._mangle / self._orig_path.name
        self.path.parent.mkdir(parents=True)
        self.path.touch()

    def save_script_contents(self, contents_path):
        with open(self.path, "w") as dest_file:
            with open(contents_path) as src_file:
                dest_file.write(src_file.read())

    def delete_script(self):
        self.path.unlink(missing_ok=True)

    def rename_script(self, new_name):
        self.path = self.path.rename(self.path.resolve().parent / new_name)
        self.path.parent.rmdir()


def load_script(cli_name):
    with open(SCRIPTS_PATH) as scripts_file:
        scripts_data = yaml.safe_load(scripts_file)
    try:
        script_data = scripts_data[cli_name]
        return Script(
            cli_name=cli_name,
            orig_path=script_data["orig_path"],
            mangle=script_data["mangle"],
        )
    except:
        print(f"Couldn't find {cli_name} in the saved scripts data")


def write_script(script):
    with open(SCRIPTS_PATH) as scripts_file:
        scripts_data = yaml.safe_load(scripts_file)
        scripts_data[script.cli_name] = {
            "cli_name": script.cli_name,
            "orig_path": script._orig_path,
            "mangle": script._mangle,
        }
        yaml.safe_dump(scripts_data, scripts_file)
