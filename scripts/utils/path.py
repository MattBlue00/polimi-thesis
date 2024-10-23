import os

def _get_root_directory(current_file_name):
    script_dir = os.path.dirname(os.path.abspath(current_file_name))  # script directory
    return os.path.dirname(script_dir)  # root directory

def get_directory_from_root(current_file_name, dir_name):
    return os.path.join(_get_root_directory(current_file_name), dir_name)  # datasets directory

def get_directory_from_dir_name(current_directory, dir_name):
    return os.path.join(current_directory, dir_name)