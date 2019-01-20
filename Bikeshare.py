#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:18:20 2018

@author: Pran Kumar Sarkar
"""
import time
import numpy as np
import pandas as pd
from shutil import get_terminal_size
import matplotlib.pyplot as plt
import seaborn as sns

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
        month = input('\nChoose the month by which you want to filter the data:\n1) January\
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
            print('\nLooks like you want to explore the statistics of: ', city)
            break
        else:
            print('\n******************INVALID INPUT*******************')
            print('Please select the city from the available options.')

    print('----------------------------------------------')
    # Asking user which filter to apply and accepting required values
    while True:
        filters = input('\nWould you like to filter the data by:\n1) Month\n2) Day \n3) Both or\n4) None at all?\
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
            print('----------------------------------------------')

            # Getting values for month and day according to selected filter
            month = get_month(filters)
            day = get_day(filters)
            break

    # Displaying the filters to data:
    print('\n\n****************CHOSEN FILTERS****************')
    print('City: {}\nMonth: {}\nDay: {}'.format(city, month, day))
    print('----------------------------------------------')

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

    month = months[month-1]
    popular_month_count = (df['Month'] == months.index(month) + 1).sum()

    return month, popular_month_count


def common_day(df):
    """
    :param:
        (data-frame) df - Pandas data-frame containing the travel data points

    :return:
        (str) day - The day which has maximum travel.
    """
    day = df['Day'].mode()[0]
    popular_day = (df['Day'] == day).sum()

    return day, popular_day


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
    df['Hour'] = df['Start Time'].dt.hour

    # Displaying statistics for whole data
    if filters == 'Month':
        popular_month, count_popular_month = common_month(df)
        print('Most popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)

    elif filters == 'Day':
        popular_day, count_popular_day = common_day(df)
        print('Most popular day for travelling: ', popular_day)
        print('Counts: ', count_popular_day)

    elif filters == 'Both':
        popular_month, count_popular_month = common_month(df)
        popular_day, count_popular_day = common_day(df)
        print('\nMost popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)
        print('\nMost popular day for travelling: ', popular_day)
        print('Counts: ', count_popular_day)

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('----------------------------------------------')

    print('\n\n***************APPLYING FILTERS***************')
    start_time = time.time()
    months = ['January', 'February', 'March', 'April', 'May', 'June']

    if filters == 'Month':
        print('Filter:\n        Month = ', month.title())
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
    print('----------------------------------------------')

    return df


def time_stats(df, filters):
    """
    Displays statistics of most frequent times of travel.

    :param:
        (data frame) df - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """

    print('**********************************************')
    print('  Calculating Most Frequent Times Of Travel')
    print('               Filter: ', filters)
    print('**********************************************')

    start_time = time.time()
    popular_month, count_popular_month = common_month(df)
    popular_day, count_popular_day = common_day(df)
    popular_hour = df['Hour'].mode()[0]
    count_popular_hour = (df['Hour'] == popular_hour).sum()

    if filters == 'None':
        print('\nMost popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)
        print('\nMost popular day for travelling: ', popular_day)
        print('Counts: ', count_popular_day)
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)
    elif filters == 'Both':
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)
    elif filters == 'Month':
        print('\nMost popular day for travelling: ', popular_day)
        print('Counts: ', count_popular_day)
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)
    elif filters == 'Day':
        print('\nMost popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)

    print('\nThis took about {} seconds'. format(time.time() - start_time))
    print('----------------------------------------------')


def station_stats(df, filters):
    """
    Displays statistics on most popular station and trip.

    :param:
        (data frame) df - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """
    print('\n**********************************************')
    print('  Calculating Most Popular Stations & Trips')
    print('               Filter: ', filters)
    print('**********************************************')
    start_time = time.time()

    print('Most Commonly Used Start Station: ', df['Start Station'].mode()[0])
    print('Counts: ', df['Start Station'].value_counts()[0])
    print('\nMost Commonly Used End Station: ', df['End Station'].mode()[0])
    print('Counts: ', df['End Station'].value_counts()[0])
    print('\nMost Popular Trip: ')

    # Calculating most popular combination of Start and End Stations
    grouped_data = df.groupby(['Start Station', 'End Station']).size().to_frame('number').reset_index()
    popular_trip_location_index = grouped_data['number'].idxmax()

    start_station = grouped_data.loc[popular_trip_location_index]['Start Station']
    end_station = grouped_data.loc[popular_trip_location_index]['End Station']
    count = grouped_data['number'].max()

    print('Start Station: {}\nEnd Station: {}\nCounts: {}'.format(start_station, end_station, count))
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('----------------------------------------------')


def trip_duration_stats(df, filters):
    """
    Displays statistics on total and average and total trip duration.

    :param:
        (data frame) df - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """

    print('\n**********************************************')
    print('          Calculating Trip Duration')
    print('               Filter: ', filters)
    print('**********************************************')
    start_time = time.time()

    # Calculating trip duration
    total_trip_duration = df['Trip Duration'].sum()
    average_trip_duration = df['Trip Duration'].mean()

    # Displaying total time
    print('Total Duration: {} seconds'.format(total_trip_duration))
    print('Counts: ', df['Trip Duration'].count())

    # Displaying average duration
    print('\nAverage Duration: {} seconds'.format(average_trip_duration))
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('----------------------------------------------')


def user_stats(df, filters):
    """
    Displays statistics on types of users, gender, most recent and most common year of birth.

    :param:
        (data frame) df - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """
    print('\n**********************************************')
    print('          Calculating User Statistics')
    print('               Filter: ', filters)
    print('**********************************************')
    start_time = time.time()

    # Calculating count on user types
    unique_user = df['User Type'].unique()
    unique_user_count = df['User Type'].value_counts()
    total_counted_user = unique_user_count[0] + unique_user_count[1]
    actual_user_count = len(df)

    # Displaying statistics on user types
    print('\n\n------------ User-Type Statistics ------------')
    print('{} : {} or {:.3f} %'.format(unique_user[0], unique_user_count[0],
                                       unique_user_count[0]*100/actual_user_count))
    print('{} : {} or {:.3f} %'.format(unique_user[1], unique_user_count[1],
                                       unique_user_count[1]*100/actual_user_count))

    # Displaying statistics for unknown user type
    if len(unique_user) == 3 and len(unique_user_count) == 3:

        if unique_user[2] == 'Dependent':
            print('{} : {} or {:.3f} %'.format(unique_user[2], unique_user_count[2],
                                               unique_user_count[2]*100/actual_user_count))
        else:
            print('Unknown : {} or {:.3f} %'.format(unique_user_count[2],
                                                    unique_user_count[2]*100/actual_user_count))

    elif len(unique_user) == 3 and len(unique_user_count) != 3:
        other_user_count = actual_user_count - total_counted_user

        if unique_user[2] == 'Dependent':
            print('{} : {} or {:.3f} %'.format(unique_user[2],
                                               other_user_count, other_user_count*100/actual_user_count))
        else:
            print('Unknown : {} or {:.3f} %'.format(other_user_count, other_user_count*100/actual_user_count))

    print('----------------------------------------------')

    # Calculating and displaying statistics on gender
    print('\n\n-------------- Gender Statistics -------------')
    if 'Gender' not in df.columns:
        print('No data is found for Gender')
    else:
        gender_data = pd.DataFrame(df['Gender'].value_counts(),df['Gender'].unique())
        gender_data.drop(np.nan, inplace=True)
        gender_data_index = gender_data.index
        total_counted_gender = gender_data['Gender'].sum()

        print('{} : {} or {:.3f} %'.format(gender_data_index[0], gender_data['Gender'][0],
                                           gender_data['Gender'][0]*100/actual_user_count))
        print('{} : {} or {:.3f} %'.format(gender_data_index[1], gender_data['Gender'][1],
                                           gender_data['Gender'][1]*100/actual_user_count))

        # Displaying statistics of unknown gender type
        if total_counted_gender != actual_user_count:
            unknown_gender_count = actual_user_count - total_counted_gender
            print('Unknown : {} or {:.3f} %'.format(unknown_gender_count, unknown_gender_count * 100 / actual_user_count))
    print('----------------------------------------------')

    # Calculating statistics on earliest, most-recent and most common year of birth
    print('\n\n------------ Birth Year Statistics -----------')

    if 'Birth Year' not in df.columns:
        print('No Data is found for Birth Year.')
    else:
        most_earliest_birth_year = df.loc[df['Birth Year'].idxmin()]['Birth Year']
        most_recent_birth_year = df.loc[df['Birth Year'].idxmax()]['Birth Year']
        most_common_birth_year = df['Birth Year'].mode()[0]
        most_common_birth_year_counts = (df['Birth Year'] == most_common_birth_year).sum()

        print('Most earliest birth year: ', most_earliest_birth_year)
        print('Most recent birth year: ', most_recent_birth_year)
        print('Most common birth year: ', most_common_birth_year)
        print('Counts: ', most_common_birth_year_counts)

    print('----------------------------------------------')
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('----------------------------------------------')


def show_data(df, filters, city):
    """
    Displays statistics on types of users, gender, most recent and most common year of birth.

    :param:
        (data frame) df - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
        (str) city - The city chosen for seeing statistics.
    """

    # Asking whether to show data
    while True:
        show = input('\nDo you want to see individual trip data? Type:\n1) Yes\n2) No\n')
        show = show.lower()

        if show == '1' or show == 'yes' or show == 'y':
            index = 0

            # Displaying individual trip data
            print('\n**********************************************')
            print('       Displaying Individual Trip Data.')
            print('               City: ', city)
            print('               Filter: ', filters)
            print("  Press 'q' to stop seeing individual data.")
            print('**********************************************\n')
            while True:

                while index % 5 != 0 or index == 0:
                    print(df.iloc[index])
                    print('\n----------------------------------------------\n')
                    index += 1

                # Asking user whether to see more data points
                if index % 5 == 0:
                    show_next = input('Do you want to see five more trip data?\n'
                                      'Press q to escape and any other key to continue:\n')
                    show_next = show_next.lower()

                    if show_next == 'q':
                        restart_program()
                        quit(0)
                    else:
                        print(df.iloc[index])
                        print('\n----------------------------------------------\n')
                        index += 1
        elif show == '2' or show == 'no' or show == 'n':
            break
        else:
            print("\nInvalid Input. Please enter 'yes' or 'no'")
            print('----------------------------------------------')


def visualize_data(df, filters, city, month, day):
    """
    Visualizes different statistics.

    :param:
        (data frame) df - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
        (str) city - The chosen city
        (str) month - The filtering month
        (str) day - The filtering day
    """

    # Asking whether to show data
    while True:
        show = input('\nDo you want to visualize different statistics? Type:\n1) Yes\n2) No\n')
        show = show.lower()

        if show == '1' or show == 'yes' or show == 'y':

            # Displaying individual statistics
            print('\n**********************************************')
            print('       Visualizing different Statistics.')
            print('               City: ', city)
            print('               Filter: ', filters)
            print('  Please wait. This might take a few moments.')
            print('**********************************************\n')
            start_time = time.time()

            # Setting style and size of seaborn plots
            sns.set(style='white', palette='inferno')
            
            # Displaying daily travel statistics
            if filters == 'Month' or filters == 'None':
                plt.figure(figsize=(10,5))
                sns.countplot(df['Day'],
                              order=['Sunday', 'Monday', 'Tuesday',
                                     'Wednesday', 'Thursday', 'Friday',
                                     'Saturday']).set_title('Daily Travel Statistics('+city+')')
                plt.show()
            
            # Displaying hourly statistics
            plt.figure(figsize=(10,5))
            sns.countplot(df['Hour']).set_title('Hourly Travel Statistics('+city+')')
            plt.show()
            
            # Displaying user type statistics
            plt.figure(figsize=(10,5))
            df['User Type'].value_counts().plot(kind='bar')
            plt.title('User Type Statistics('+city+')')
            plt.xlabel('User Type')
            plt.ylabel('Counts')
            plt.xticks(rotation=0)
            plt.show()
            
            # Washington does not has gender and birth year data
            if city != 'Washington':
                # Displaying gender statistics
                plt.figure(figsize=(10,5))
                df['Gender'].value_counts().plot(kind='bar')
                plt.title('Gender Statistics('+city+')')
                plt.xlabel('Gender')
                plt.ylabel('Counts')
                plt.xticks(rotation=0)
                plt.show()

                # Displaying Birth Year Statistics
                plt.figure(figsize=(15,10))
                df['Birth Year'].value_counts(sort=False).plot(kind='bar')
                plt.title('Birth Year Statistics('+city+')')
                plt.xlabel('Birth Year')
                plt.ylabel('Counts')
                plt.xticks(rotation=45)
                plt.show()
            
            print('----------------------------------------------')
            print('\nThis took about {} seconds.'.format(time.time() - start_time))
            print('----------------------------------------------')
            break
        elif show == '2' or show == 'no' or show == 'n':
            print('----------------------------------------------')
            break
        else:
            print("\nInvalid Input. Please enter 'yes' or 'no'")
            print('----------------------------------------------')


def restart_program():
    """
    Asks user whether to restart the program. If 'yes' program is restarted else exit from program.
    """
    # Asking user whether to restart the program?
    while True:
        print('----------------------------------------------')
        restart = input('\nWould you like to restart? Enter:\n1) yes\n2) no\n')
        restart = restart.lower()

        # Decoding mnemonic inputs and taking required actions
        if restart == '2' or restart == 'no' or restart == 'n':
            print('\n******************THANK YOU*******************\n')
            quit(0)
        elif restart == '1' or restart == 'yes' or restart == 'y':
            print("\n" * get_terminal_size().lines, end='')
            main()
            quit(0)
        else:
            print("Invalid Input. Please type 'y' or 'n'....")


def main():
    while True:
        city, month, day, filters = get_filters()
        df = load_data(city, month, day, filters)

        print('\n\n************DISPLAYING STATISTICS*************')
        time_stats(df, filters)
        station_stats(df, filters)
        trip_duration_stats(df, filters)
        user_stats(df, filters)
        visualize_data(df, filters, city, month, day)
        show_data(df, filters, city)

        # To restart or quit program
        restart_program()


if __name__ == '__main__':
    main()
