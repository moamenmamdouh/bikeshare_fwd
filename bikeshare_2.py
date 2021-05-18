import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago","new york city","washington"]
    city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
    while(city not in cities):
        city = input("Please only choose from the given options.\nWould you like to see data for Chicago, New York City, or Washington? ").lower()    
    
    # get user input for month (all, january, february, ... , june)
    months = ["all","january","february","march","april","may","june"]
    month = input("Which month - January, February, March, April, May, or June? ").lower()
    while(month not in months):
        month = input("Please only choose from the given options.\nWhich month - January, February, March, April, May, or June? ").lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").lower()
    while(day not in days):
        day = input("Please only choose from the given options.\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()
    print("Most common month is\n{}".format(common_month))

    # display the most common day of week
    common_day = df["day_of_week"].mode()
    print("Most common day is\n{}".format(common_day))

    # display the most common start hour
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()
    print("Most common hour is {}".format(common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()
    print("Most common start station is {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df["End Station"].mode()
    print("Most common end station is {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df["Whole Trip"] = df["Start Station"] + " " + df["End Station"]
    frequent_trip = df["Whole Trip"].mode()
    print("Most frequent trip is {}".format(frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum()
    print("Total travel time is {}".format(total_travel))

    # display mean travel time
    mean_travel = df["Trip Duration"].mean()
    print("Mean travel time is {}".format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df["User Type"].value_counts()
    print(user_counts)

    # Display counts of gender
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print(gender_counts)

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("The earliest year of birth is {}".format(int(df["Birth Year"].min())))
        print("The most recent year of birth is {}".format(int(df["Birth Year"].max())))
        print("The most common year of birth is {}".format(int(df["Birth Year"].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(df):
    """Display raw data as per user request. 5 rows at a time"""
    preview_index = 0
    print(df.iloc[preview_index:preview_index + 5])
    user_answer = input("Would you like to view more raw data? ").lower()
    while(user_answer == "yes"):
        preview_index += 5
        print(df.iloc[preview_index:preview_index + 5])
        user_answer = input("Would you like to view more raw data? ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
