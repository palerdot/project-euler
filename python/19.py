import time
import math

start_time = time.time()

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

START_YEAR = 1901
END_YEAR = 2000

def is_leap_year(year):
    # if a century year see if it is divisible by 400
    if (year%100 == 0):
        return year%400 == 0 
    # else just see if it is divisible by 4
    else:
        return year%4 == 0

# get days for a month in a given year
def get_days_for_month(month, year):

    # if februray
    if (month == 2):
        # see if it is leap year
        if (is_leap_year(year)):
            return 29
        else:
            return 28

    thirty = [9, 4, 6, 11]

    if month in thirty:
        return 30
    else:
        return 31

# returns number of days relative to: 01 Jan 1900
def get_relative_days(day, month, year):
    total_days = 0
    # first traverse through the years
    for y in range(1900, year):
        if (is_leap_year(y)):
            total_days = total_days + 366
        else:
            total_days = total_days + 365

    # now traverse through months
    for m in range(1, month):
        days = get_days_for_month(m, year)
        total_days = total_days + days

    # now finally add the day
    total_days = total_days + day

    # return the total days
    return total_days - 1

TOTAL_SUNDAYS = 0

# for the given years
for year in range(START_YEAR, END_YEAR + 1):
    # for each month
    for month in range(1, 13):
        # get relative days for 1st of each month
        difference = get_relative_days(1, month, year)

        is_sunday = (DAYS[difference%7] == "Sun")
        if (is_sunday):
            TOTAL_SUNDAYS = TOTAL_SUNDAYS + 1

print "Total sundays ", TOTAL_SUNDAYS

print time.time() - start_time, " seconds"