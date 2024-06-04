import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = {'all','january','february','march','april', 'may','june'}
DAY_DATA ={'all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter the city name to view the US bikeshare data : ").lower()
    while city not in CITY_DATA :
        print ("Oops! Looks like your city is invalid value!")
        city= input("Please choose 1 of 3 cities:chicago, new york city,washington : ").lower()
               
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter the month to view the US bikeshare data : ").lower()
    while month not in MONTH_DATA :
        print ("Oops! Looks like the month is invalid value!")
        month= input("If you want to select all months, enter all and otherwise enter values: january, february, march, April, may, june : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the days of week to view the US bikeshare data : ").lower()
    while day not in DAY_DATA :
        print ("Oops! Looks like the day is invalid value! ")
        day= input("If you want to select all day of the week, enter all and vice versa, enter the values: monday, tuesday, wednesday, thursday', friday, saturday, sunday : ").lower()

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
    df = pd.read_csv (CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month !='all':
        months=['january','february','march','april', 'may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day !='all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is : ", common_month)

    # TO DO: display the most common day of week
    common_dayweek = df['day_of_week'].mode()[0]
    print("The most common day of week is : ", common_dayweek)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common day of start hour is : ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is : ", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is : ", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip : ", start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is : ", total_travel_time)
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is : ", str(round(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types : ", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Counts of gender : ", df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = int(df['Birth Year'].min())
        print("The earliest year of birth : ", earliest_birth)
        recent_birth = int(df['Birth Year'].max())
        print("The most recent year of birth : ", recent_birth)
        common_birth = int(df['Birth Year'].mode()[0])
        print("The most common year of birth : ", common_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Displays raw data with the specified number of rows at a time.
    """
    start_index= 0 
    end_index = 5
    while True:
        show_rawdata = input("\nWould you like to see 5 lines of raw data? Answer 'yes' or 'no' : ").lower()
        if show_rawdata !='yes':
            break
        print(df.iloc[start_index:end_index])
        
        if start_index >= len(df):
            print("\nNo more raw data to show.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
