#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=4, minutes=3))

# TODO: print today's date
now = datetime.now()
print("Today's date:", now)

# TODO: print today's date one year from now
print("One year from now:", str(now+timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("In 3 weeks and 5 days, it will be : ",
      str(now+timedelta(weeks=3, days=5)))


# TODO: calculate the date 1 week ago, formatted as a string
print("Time one week ago this time: ", str(now-timedelta(weeks=1)))

# How many days until April Fools' Day?
today = date.today()
aprilFool = date(today.year, 4, 1)

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if aprilFool < today:
    print("April Fool's day already went by ",
          (today-aprilFool).days, "days ago")
    aprilFool = aprilFool.replace(year=today.year + 1)


# TODO: Now calculate the amount of time until April Fool's Day
timeToAprilFool = aprilFool - today
print("It is ", timeToAprilFool, " days before the april fool day")
