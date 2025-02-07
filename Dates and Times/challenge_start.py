# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar


def count_days(year, month, whichday):
    # Your code goes here.
    count = 0
    calendarMonth = calendar.monthcalendar(year, month)
    print(calendarMonth)
    for week in calendarMonth:
        for index, day in enumerate(week):
            print(index)
            if index == whichday:
                count = count + 1
    return count
