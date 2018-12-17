#!/usr/bin/env python
import time
import pandas as pd
from shutil import get_terminal_size

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_month(filters):
    """
        Asks user to enter name of month if filters is not 'none' or 'day'.

        :param:
            (str) filters - Name of the filter applied, none, both, month or day.

        :return:
            (str) month - Month from 'january' to 'july' to filter data. 'All' if user does not want to filter by month
        """

    if filters == 'None' or filters == 'Day':
        return 'All'

    while True:
        month = input('\n\nChoose the month by which you want to filter the data:\n1) January\
        \n2) February\n3) March\n4) April\n5) May\n6) June\n7) All?\nPlease input numbers only(1-7):\n')
        month = month.title()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

        # Attempting to decode mnemonic input else prompt for input again
        if month not in months:
            if month == '1' or month == 'Jan':
                month = 'January'
            elif month == '2' or month == 'Feb':
                month = 'February'
            elif month == '3' or month == 'Mar':
                month = 'March'
            elif month == '4' or month == 'Apr':
                month = 'April'
            elif month == '5' or month == 'Ma':
                month = 'May'
            elif month == '6' or month == 'Jun':
                month = 'June'
            elif month == '7':
                month = 'All'
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
        (str) day - Day of week to filter data. 'All' if user does not want to filter by day
    """

    if filters == 'None' or filters == 'Month':
        return 'All'

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
        get_month(filters) - Returns name of month to filter data, or 'All' if no month filter is chosen.
        get_day(filters) - Returns name of day to filter data, or 'All' if no day filter is chosen.

    :returns:
        (str) city - Name of the city to analyze.
        (str) filter - Name of the filters: month, day, both, or none.
        (str) month - Name of the month to filter by, or 'All' to apply no month filter.
        (str) day - Name of the day to filter by, or 'All' to apply no day filter.
    """
    print('Hello! Let\'s explore some US bike-share data.\n')

    # Gets city to filter data
    while True:
        city = input('Choose among the following cities for which you want to see the data: \
        \n1) Chicago\n2) New York\n3) Washington?\n')
        city = city.title()

        # Decoding mnemonic inputs
        if city == '1' or city == 'Chi' or city == 'C':
            city = 'Chicago'
        elif city == '2' or city == 'Ny' or city == 'N Y' or city == 'Newyork' or city == 'N':
            city = 'New York'
        elif city == '3' or city == 'Wash' or city == 'W':
            city = 'Washington'

        # Asking user to input again if unexpected input else continue
        if city == 'Chicago' or city == 'New York' or city == 'Washington':
            print('Looks like you want to explore the statistics of: ', city)
            break
        else:
            print('\n******************INVALID INPUT*******************')
            print('Please select the city from the available options.')

    # Asking user which filter to apply and accepting required values
    while True:
        filters = input('\n\nWould you like to filter the data by:\n1) Month\n2) Day \n3) Both or\n4) None at all?\
        \nChoose among the available filters(1 - 4):\n')
        filters = filters.title()

        options = ['1', '2', '3', '4', 'Month', 'Day', 'Both', 'None']

        # Taking care of invalid filters else getting required values of filters
        if filters not in options:
            print('\n******************INVALID INPUT*******************')
            print('Please apply any of the following filters: Month, Day, Both, or None')
        else:
            # Decoding mnemonic inputs
            if filters not in options[4:8]:
                if filters == '1':
                    filters = 'Month'
                elif filters == '2':
                    filters = 'Day'
                elif filters == '3':
                    filters = 'Both'
                elif filters == '4':
                    filters = 'None'

            # Providing feedback to users
            print("Okay, We will apply the following filter: ", filters)

            # Getting values for month and day according to selected filter
            month = get_month(filters)
            day = get_day(filters)
            break

    # Displaying the filters to data:
    print('\n\n****************CHOSEN FILTERS****************')
    print('City: {}\nMonth: {}\nDay: {}'.format(city, month, day))
    print('**********************************************')

    return city, month, day, filters


def common_month(df):
    """
    :param:
        (data-frame) df - Pandas data-frame containing the travel data points

    :return:
        (str) month - The month which has maximum travel.
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month = df['Month'].mode()[0]

    return months[month-1]


def common_day(df):
    """
    :param:
        (data-frame) df - Pandas data-frame containing the travel data points

    :return:
        (str) day - The day which has maximum travel.
    """
    return df['Day'].mode()[0]


def load_data(city, month, day, filters):
    """
    Loads data and applies the filters

    Displays:
            Some statistics on whole data set before applying filter.
            Most popular month: If filter is 'Month'
            Most popular day: If filter is 'Day'
            Most popular month and day: If filter is 'Both'

    :param:
        (str) city - City whose statistics user want to see.
        (str) month - Month whose statistics user want to see.
        (str) day- Day whose statistics user want to see.
        (str) filters - The filters which user want to apply on data.

    :return:
        (data-frame) df - Data frame containing relevant data after filters are applied.
    """
    print('\n\n*****************LOADING DATA*****************')
    start_time = time.time()

    df = pd.read_csv(CITY_DATA[city])
    print('City: ', city)
    print('Total data points found: ', len(df))

    # Changing start time to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Day'] = df['Start Time'].dt.weekday_name
    df['Month'] = df['Start Time'].dt.month

    # Displaying statistics for whole data
    if filters == 'Month':
        print('Most common month for travelling: ', common_month(df))
    elif filters == 'Day':
        print('Most common day for travelling: ', common_day(df))
    elif filters == 'Both':
        print('Most common month for travelling: ', common_month(df))
        print('Most common day for travelling: ', common_day(df))

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('**********************************************')

    print('\n\n***************APPLYING FILTERS***************')
    start_time = time.time()
    months = ['January', 'February', 'March', 'April', 'May', 'June']

    if filters == 'Month':
        print('Filter: Month = ', month.title())
        df = df[df['Month'] == months.index(month) + 1]
    elif filters == 'Day':
        print('Filter: Day = ', day)
        df = df[df['Day'] == day]
    elif filters == 'Both':
        print('Filter:\n        Month =  {}\n        Day = {}'.format(month.title(), day))
        df = df[df['Month'] == months.index(month) + 1]
        df = df[df['Day'] == day]
    else:
        print('Filter: ', filters)

    print('Total data points after applying filter: ', len(df))
    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('**********************************************')

    return df


def restart_prog():
    """
    Asks user whether to restart the program. If 'yes' program is restarted else exit from program.
    """
    # Asking user whether to restart the program?
    while True:
        restart = input('\n\nWould you like to restart? Enter:\n1) yes\n2) no\n')
        restart = restart.lower()

        # Decoding mnemonic inputs
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


def main():
    while True:
        city, month, day, filters = get_filters()
        df = load_data(city, month, day, filters)

        # To restart or quit program
        restart_prog()


if __name__ == '__main__':
    main()
