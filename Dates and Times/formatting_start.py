#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()
    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print("current year is ", now.strftime("%y"))
    print("current weekday is ", now.strftime("%A"))
    print("current month is ", now.strftime("%b"))
    print("current day is ", now.strftime("%d"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("locale date and time : %c"))
    print(now.strftime("locale date : %x"))
    print(now.strftime("locale time : %X"))

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("current time : %I:%M:%S %p"))
    print(now.strftime("24-hour time : %H:%M"))


if __name__ == "__main__":
    main()
