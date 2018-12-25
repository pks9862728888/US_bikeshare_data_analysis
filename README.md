Analysis Of US Bikeshare Data From Motivate
===========================================

Overview:
-------------------------------------------
This project analyzes the bike-share data of US from Motivate for popular cities Washington, New York, and Chicago; and then shows various statistics according to filter chosen by user. It also shows individual travel data if the user want to see it.

Moreover after seeing statistics of a particular station, the user can restart the program to see the statistics of another station or same station with different filters.

### Available Filters

**Day:** This filters the data by day.\
**Month:** This filters the data by month.\
**Both:** This filters the data by both month and year.\
**None:** This does not filter data at all.

*If filter is day, month, or both, then statistics of popular day, month or both are shown respectively before filter is applied.*

### Statistics Shown

These statistics are shown on filtered data:~

**Time statistics:** This shows statistics of most popular day of travel, most popular month of travel, and most popular hour of travel. *However if data is filtered by day, month or both, then statistics on most popular day, month or both is shown on whole data set instead of showing it on filtered data-set.*

**Station Statistics:** This shows statistics of the most common Start Station, most common End Station, and most popular trip based on combination of Start and End Stations.

**Trip Duration Statistics:** This shows statistics of the total trip duration and the average trip duration.

**User Statistics:** This shows statistics on the types of users, gender of users, most recent, most common, and most earliest birth year of the bike users.


Sample execution screenshots:
-------------------------------------------
Chosen country: *Chicago*\
Chosen filter: *both*\
Chosen month: *February*\
Chosen day: *Tuesday*

![Choosing country](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2000.png)
![Choosing filters](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2001.png)
![Displaying Time and station statistics](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2002.png)
![Displaying Trip Duration and User Statistics](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2003.png)
![Choosing to see individual trip data](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2004.png)
![Displaying individual trip data](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2005.png)
![Terminating the program](https://github.com/pks9862728888/US_bikeshare_data_analysis/blob/master/Screenshots/Bikeshare%2006.png)

References:
-------------------------------------------
1. Clearing the screen: [Stack Overflow Link](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
2. Counting grouped occurences in dataframe: [Stack Overflow Link](https://datascience.stackexchange.com/questions/29840/how-to-count-grouped-occurrences)
3. Udacity: [Python Foundation Nanodegree](https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy?utm_source=GoogleSearch&utm_medium=NewAcq&utm_campaign=PR-GoogleSearch-Inpayment-BrandCourse-NewAcq-D-BMM-RLSA&utm_content=BMM&gclid=CjwKCAiAx4fhBRB6EiwA3cV4Ks8nLotobMAv23vHBe6hjE7WguW6oa7jzSK5xLmdX99ZQ66j9ZFd4BoCA8QQAvD_BwE)
4. Python for Data Analysis by Wes McKinney
5. Mentor(*available in Slack*): Sir Vardaan Sharma