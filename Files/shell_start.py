#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("test.txt"):
        # get the path to the file in the current directory
        src = path.realpath("test.txt")

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # now use the shell to make a copy of the file
        shutil.copy(src, dst)

        # rename the original file
        # os.rename("test.txt", "newtest.txt")

        # now put things into a ZIP archive
        dir, file = path.split(src)
        shutil.make_archive("archive", "zip", dir)

        # more fine-grained control over ZIP files
        with ZipFile("testZip.zip", "w") as newzip:
            newzip.write("test.txt")
            newzip.write("test.txt.bakr")


if __name__ == "__main__":
    main()
