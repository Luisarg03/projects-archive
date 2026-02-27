import os
import shutil


def clear_path(path, removefiles=False, extensions=None, removesubfolders=False, subfolders=None):
    for root, dirs, files in os.walk(path):
        for file in files:
            if removefiles is True and file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                os.remove(file_path)

        if removesubfolders:
            for dir in dirs:
                if dir in subfolders:
                    dir_path = os.path.join(root, dir)
                    shutil.rmtree(dir_path)
    return True
