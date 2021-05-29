import os
import sys
import glob
import shutil
import fire

sys.path.append(os.getcwd())
from src.config import DIR_TO_ARANGE, EXT_INTEREST


def arange_dir(target_dir):
    """file ext janitor"""
    for file_target in glob.glob(target_dir + "*.*"):

        # get extension
        file_ext = file_target.split(".")[-1]

        # skip if ext not in ext interest
        if file_ext not in EXT_INTEREST:
            continue

        # check if dir ext is exist, if not exist, create new directory
        if not os.path.exists(target_dir + file_ext):
            print(
                f"> directory for ext: {file_ext} not found. creating new directory for ext: {file_ext}"
            )
            os.mkdir(target_dir + file_ext)

        # move file to its extension directory
        print(f"> moving {file_target} to {target_dir + file_ext}")
        shutil.move(file_target, target_dir + file_ext)


def janitor():
    """main janitor runner"""
    for dir_interest in DIR_TO_ARANGE:
        # clean up dir_interest
        arange_dir(dir_interest)


def init_test():
    """test bootstrap"""

    for ext in EXT_INTEREST:
        if not os.path.exists(os.getcwd() + "/test"):
            print("> bootstraping test directory")
            os.mkdir(os.getcwd() + "/test")

        for file_id in range(0, 5):
            print(f"> creating {os.getcwd()}/test/file-{file_id}.{ext}")
            with open(os.getcwd() + f"/test/file-{file_id}.{ext}", "w") as f:
                f.write(f"{ext}-{file_id}")


if __name__ == "__main__":
    fire.Fire()
