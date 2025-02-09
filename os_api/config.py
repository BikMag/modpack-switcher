import os
import json


BASE_DIR = os.path.join(os.path.realpath(os.curdir), 'static')
MODPACK_DIR = ""
DESTINATION_DIR = ""


def save_data(new_modpack_dir, new_destination_dir):
    global MODPACK_DIR, DESTINATION_DIR

    with open('data.json', 'w') as file:
        json.dump(
            {
                "modpack_dir": new_modpack_dir,
                "destination_dir": new_destination_dir
            },
            file,
            indent=4
        )

    MODPACK_DIR = new_modpack_dir
    DESTINATION_DIR = new_destination_dir


def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)


if os.path.exists('data.json'):
    data = load_data()
    MODPACK_DIR = data["modpack_dir"]
    DESTINATION_DIR = data["destination_dir"]
else:
    MODPACK_DIR = os.path.join(BASE_DIR, 'mods')
    DESTINATION_DIR = os.path.join("C:\\Users", os.getlogin(), "AppData\Roaming\.minecraft\mods")
    save_data(MODPACK_DIR, DESTINATION_DIR)
