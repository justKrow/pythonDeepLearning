#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("item exists :" + str(path.exists("test.txt")))
    print("item is a file :" + str(path.isfile("test.txt")))
    print("item is a directory :" + str(path.isdir("test.txt")))

    # Work with file paths
    print("item path :" + str(path.realpath("test.txt")))
    print("item path and name :" + str(path.split(path.realpath("test.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("test.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("test.txt")))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("test.txt"))
    print(td.total_seconds(), "seconds")


if __name__ == "__main__":
    main()
