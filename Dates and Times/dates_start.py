#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
    # DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date:", today)

    # TODO: print out the date's individual components
    print("Today's date components:", today.day, today.month, today.year)

    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Week day number:", today.weekday())
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    print("it is ", days[today.weekday()])

    # DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    timeNow = datetime.now()
    print("Now's date:", timeNow)

    # TODO: Get the current time
    currTime = datetime.time(datetime.now())
    print("Current time:", currTime)


if __name__ == "__main__":
    main()
