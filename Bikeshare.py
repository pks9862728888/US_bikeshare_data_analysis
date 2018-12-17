#!/usr/bin/env python
import time
import pandas as pd
from shutil import get_terminal_size

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_month(filters):
    """
        Asks user to enter name of month if filters is not 'none' or 'day'.

        :param:
            (str) filters - Name of the filter applied, none, both, month or day.

        :return:
            (str) month - Month from 'january' to 'july' to filter data. 'all' if user does not want to filter by month
        """

    if filters == 'none' or filters == 'day':
        return 'all'

    while True:
        month = input('\n\nChoose the month by which you want to filter the data:\n1) January\
        \n2) February\n3) March\n4) April\n5) May\n6) June\n7) All?\nPlease input numbers only(1-7):\n')
        month = month.lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

        # Attempting to decode mnemonic input else prompt for input again
        if month not in months:
            if month == '1' or month == 'jan':
                month = 'january'
            elif month == '2' or month == 'feb':
                month = 'february'
            elif month == '3' or month == 'mar':
                month = 'march'
            elif month == '4' or month == 'apr':
                month = 'april'
            elif month == '5' or month == 'ma':
                month = 'may'
            elif month == '6' or month == 'jun':
                month = 'june'
            elif month == '7':
                month = 'all'
            else:
                print('\n******************INVALID INPUT*******************')
                print('Please select any option from (1-7):')
                continue
        break
    return month


def get_day(filters):
    """
    Asks user to enter name of day if filters is not 'none' or 'month'.

    :param:
        (str) filters - Name of the filter applied, none, both, month or day.

    :return:
        (str) day - Day of week to filter data. 'all' if user does not want to filter by day
    """

    if filters == 'none' or filters == 'month':
        return 'all'

    while True:
        day = input('\nChoose the day by which you want to filter the data:\n1) Sunday\n2) Monday\n3) Tuesday\
        \n4) Wednesday\n5) Thursday\n6) Friday\n7) Saturday\n8) All?\nPlease input numbers only(1-8):\n')
        day = day.title()
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']

        # Attempting to decode mnemonic input else prompt for input again
        if day not in days:
            if day == '1' or day == 'Sun' or day == 'S' or day == 'Su':
                day = 'Sunday'
            elif day == '2' or day == 'Mon' or day == 'M':
                day = 'Monday'
            elif day == '3' or day == 'Tue' or day == 'Tu':
                day = 'Tuesday'
            elif day == '4' or day == 'Wed' or day == 'W':
                day = 'Wednesday'
            elif day == '5' or day == 'Thr' or day == 'Th':
                day = 'Thursday'
            elif day == '6' or day == 'Fri' or day == 'F':
                day = 'Friday'
            elif day == '7' or day == 'Sat' or day == 'Sa':
                day = 'Saturday'
            elif day == '8' or day == 'all':
                day = 'All'
            else:
                print('\n******************INVALID INPUT*******************')
                print('Please select any option from (1-8):')
                continue
        break
    return day


def get_filters():
    """
    Asks user to enter the name of city and select filters from month, day, both or none.

    Calls:
        get_month(filters) - Returns name of month to filter data, or 'all' if no month filter is chosen.
        get_day(filters) - Returns name of day to filter data, or 'all' if no day filter is chosen.

    :returns:
        (str) city - Name of the city to analyze.
        (str) filter - Name of the filters: month, day, both, or none.
        (str) month - Name of the month to filter by, or 'all' to apply no month filter.
        (str) day - Name of the day to filter by, or 'all' to apply no day filter.
    """
    print('Hello! Let\'s explore some US bike-share data.\n')

    # Gets city to filter data
    while True:
        city = input('Choose among the following cities for which you want to see the data: \
        \n1) Chicago\n2) New York\n3) Washington?\n')
        city = city.lower()

        # Decoding mnemonic inputs
        if city == '1' or city == 'chi' or city == 'c':
            city = 'chicago'
        elif city == '2' or city == 'ny' or city == 'n y' or city == 'newyork' or city == 'n':
            city = 'new york'
        elif city == '3' or city == 'wash' or city == 'w':
            city = 'washington'

        # Asking user to input again if unexpected input else continue
        if city == 'chicago' or city == 'new york' or city == 'washington':
            print('Looks like you want to explore the statistics of: ', city.title())
            break
        else:
            print('\n******************INVALID INPUT*******************')
            print('Please select the city from the available options.')

    # Asking user which filter to apply and accepting required values
    while True:
        filters = input('\n\nWould you like to filter the data by:\n1) month\n2) day \n3) both or\n4) none at all?\
        \nChoose among the available filters(1 - 4):\n')
        filters = filters.lower()

        # Taking care of invalid filters else getting required values of filters
        if filters not in ['1', '2', '3', '4', 'month', 'day', 'both', 'none']:
            print('\n******************INVALID INPUT*******************')
            print('Please apply any of the following filters: month, day, both, none')
        else:
            # Decoding mnemonic inputs
            if filters not in ['month', 'day', 'both', 'none']:
                if filters == '1':
                    filters = 'month'
                elif filters == '2':
                    filters = 'day'
                elif filters == '3':
                    filters = 'both'
                elif filters == '4':
                    filters = 'none'

            # Providing feedback to users
            print("Okay, We will apply the following filter: ", filters.title())

            # Getting values for month and day according to selected filter
            month = get_month(filters)
            day = get_day(filters)
            break

    # Displaying the filters to data:
    print('\n\n****************CHOSEN FILTERS****************')
    print('City: {}\nMonth: {}\nDay: {}'.format(city.title(), month.title(), day.title()))
    print('**********************************************')

    return city, month, day, filters


def main():
    while True:
        city, month, day, filters = get_filters()

        # Asking user whether to restart the program?
        while True:
            restart = input('\n\nWould you like to restart? Enter:\n1) yes\n2) no\n')
            restart = restart.lower()

            if restart == '2' or restart == 'no' or restart == 'n':
                restart = False
                break
            elif restart == '1' or restart == 'yes' or restart == 'y':
                restart = True
                break

        # Restarting if user want to restart else quitting.
        if restart:
            print("\n" * get_terminal_size().lines, end='')
            main()
        else:
            print('\n******************THANK YOU*******************\n')
            quit(0)


if __name__ == '__main__':
    main()
