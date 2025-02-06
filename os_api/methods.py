import glob
import os
import shutil

from os_api.config import MODPACK_DIR, DESTINATION_DIR, BASE_DIR


def get_mods(dir_name):
    mod_dir = os.path.abspath(MODPACK_DIR + dir_name)
    if not os.path.exists(mod_dir):
        print(f'Directory "{dir_name}" doesn\'t exist')
        return None

    mods_names = []
    for f in os.listdir(mod_dir):
        mod_path = os.path.join(mod_dir, f)
        if os.path.isfile(mod_path) and f.endswith('.jar'):
            mods_names.append(f)

    return mods_names


def get_modpacks(path=MODPACK_DIR):
    return [
        d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))
    ]


def move_modpack(dir_name):
    mod_dir = os.path.abspath(MODPACK_DIR + dir_name)
    if not os.path.exists(mod_dir):
        print(f'Directory "{dir_name}" doesn\'t exist')
        return

    clear_dir(DESTINATION_DIR) # Решить вопрос с очисткой папки перед перемещением модов

    files = glob.iglob((os.path.join(mod_dir, '*.jar')))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, DESTINATION_DIR)

    print(f'Modpack "{dir_name}" has been moved')


def clear_dir(path):
    for file_name in os.listdir(path):
        file = os.path.join(path, file_name)
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)

def remove_dir(dir_name):
    dir_path = os.path.join(MODPACK_DIR, dir_name)
    if not os.path.exists(dir_path):
        print(f'Directory "{dir_name}" doesn\'t exists')
        return

    shutil.rmtree(dir_path)
    print(f'Directory "{dir_name}" has been removed')

def create_dir(dir_name):
    dir_path = os.path.join(MODPACK_DIR, dir_name)
    if os.path.exists(dir_path):
        print(f'Directory "{dir_name}" exists')
        return

    os.mkdir(dir_path)
    os.startfile(dir_path)
    print('Now you can add mods in this directory')

def rename_dir(dir_name, new_dir_name):
    dir_path = os.path.join(MODPACK_DIR, dir_name)

    new_dir_path = os.path.join(MODPACK_DIR, new_dir_name)
    if os.path.exists(new_dir_path):
        print(f'Directory "{dir_name}" exists')
        raise FileExistsError("test")

    os.rename(dir_path, new_dir_path)

def open_dir(dir_path):
    os.startfile(dir_path)
