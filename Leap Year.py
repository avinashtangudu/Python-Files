
# Number of days in each month

days_in_each_month = [0,31,28,31,30,31,30,31,30,31,30,31]

def leap_year(year):
    ''' Gives back True for Leap Year & False for Non-Leap Year'''

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_a_month(year, month):
# This will print the number of days in that month.
    
    if not 1 <= month <= 12:
        return 'Not A Leap Year'
    if month == 2 and leap_year(year):
        return 29
    return days_in_each_month[month]

print(leap_year(2020)) # Here you can write whatever "year" you want to check.

print(days_in_a_month(2021, 2)) # Here we are wrinting "Year" and "Month" in it.
