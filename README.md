Project 1: Analysis Of US Bikeshare Data From Motivate
======================================================
### by Pran Kumar Sarkar

US Bikeshare Data analysis project, part of the Udacity [Python Foundation Nanodegree](https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy).

Overview:
-------------------------------------------
This project analyzes the bike-share data of US from [Motivate](https://www.motivateco.com/) for popular cities Washington, New York, and Chicago; and then shows various statistics according to filter chosen by user. It also shows visual statistics and individual travel data if the user want to see it.

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

**User Statistics:** This shows statistics on the types of bike users, gender of bike users, most recent, most common, and most earliest birth year of the bike users.

Moreover Time statistics, Station statistics, and User statistics are also shown in graphs.

## Required Libraries and Dependencies:

Python 3.x is required to run this project. The Python executable should be in your default path, in which the Python installer should have set. 

Additional required packages:
* **pandas** : ```pip install pandas -y```
* **numpy** : ```pip install numpy -y```
* **seaborn** : ```pip install seaborn -y```
* **matplotlib** : ```pip install matplotlib -y```

To install the above packages(*if not installed*) open terminal or command prompt and type in the commands provided above.

## Project contents:

This project consists for the following files:

* **bikeshare.py** - main Python script to run.
* **chicago.csv** - contains bikeshare data for Chicago city.
* **new_york_city.csv** - contains bikeshare data for New York city.
* **washington.csv** - contains bikeshare data for Washington city.
* **README.md** - Readme file containing detailed instructions for program execution and project overview.
* **_config.yml** - Configuration file for github theme.

## Download:
This project can be downloaded by [clicking here](https://github.com/pks9862728888/US_bikeshare_data_analysis/archive/master.zip) 

## How to Run Project:

Download the project zip file to your computer and unzip the file. Or clone this repository to your desktop by typing the following code in your terminal(*for Linux*) or command prompt(*for windows*):

```bash
git clone https://github.com/pks9862728888/Movie_trailer_website_generator.git
```

Navigate to the project directory and type in the following command:

```bash
python Bikeshare.py
```

## Extra Credit Description:

The following features were implemented to gain an extra credit from Udacity:

* Added functionality to show popular day and popular month of trip on whole data if data is to be filtered by day or month or both.
* Shows the number and percentage of data which are missing.
* Added functionality to visualize the individual statistics in graph.

## References:
1. [Python Foundation Nanodegree Udacity](https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy)
2. [Markdown formatting for README.md](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
3. [Writing Readme Free Course Udacity](https://classroom.udacity.com/courses/ud777)
4. [Sample Readme by tsega](https://github.com/tsega/movie-trailer-website/blob/master/README.md)
5. Clearing the screen: [Stack Overflow Link](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
6. Counting grouped occurences in dataframe: [Stack Overflow Link](https://datascience.stackexchange.com/questions/29840/how-to-count-grouped-occurrences)
7. Python for Data Analysis by Wes McKinney
8. Mentor(*available in Slack*): Sir Vardaan Sharma

Thank you.
