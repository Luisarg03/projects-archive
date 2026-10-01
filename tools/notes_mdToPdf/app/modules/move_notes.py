import shutil


def copy_folder(source, dest):
    try:
        shutil.copytree(source, dest, dirs_exist_ok=True)
    except FileExistsError:
        shutil.rmtree(dest)
        shutil.copytree(source, dest)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
