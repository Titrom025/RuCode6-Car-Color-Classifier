import os
import re
import shutil


def create_dir_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def recreate_dir(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)


def get_files(folder):
    return _sorted_alphanumeric([f for f in os.listdir(folder)
                                if os.path.isfile(os.path.join(folder, f))])


def get_dirs(folder):
    return [f for f in os.listdir(folder)
            if os.path.isdir(os.path.join(folder, f))]


def _sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)
