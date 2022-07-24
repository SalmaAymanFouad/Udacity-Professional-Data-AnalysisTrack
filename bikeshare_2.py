import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        city = input("Please choose one of the following cities: chicago, new york city, washington\n").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Please enter one of the valid countries\n")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose a month to filter the data with it, if you don't want to filter data by a specific"\
                      "month write 'all'. Choose a month from january to june\n").lower()
        if (month in MONTHS) or (month == 'all'):
            break
        else:
            print("Please enter one of the valid months\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose a day to filter the data with it, if you don't want to filter data by a specific day"\
                    "write 'all'.\n").lower()
        if(day in DAYS) or (day == 'all'):
            break
        else:
            print("Please enter one of a valid days\n")
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['day'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month

    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        day = DAYS.index(day)
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nThe most common month corresponding to your choosen day filter is: %s ." % (
    MONTHS[(df['month'].mode()[0])-1]))

    # display the most common day of week
    print("\nThe most common day of week corresponding to your choosen day filter is: %s ." % (
    DAYS[(df['day'].mode()[0])-1]))

    # display the most common start hour
    print("\nThe most common start hour corresponding to your choosen filters is at: %s h." % (df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nThe most commonly used start station corresponding to your choosen filters is: %s ." % (
    df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("\nThe most commonly used end station corresponding to your choosen filters is: %s ." % (
    df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + " and " + df['End Station']
    print("\nThe most frequent combination of start station and end station trip corresponding to your choosen filters is: %s ." % (
    df['Start and End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time_sec = df['Trip Duration'].sum()
    sec_rem = int(total_time_sec%60)
    total_time_min = total_time_sec/60
    min_rem = int(total_time_min%60)
    total_time_hr = total_time_min/60
    hr_rem = int(total_time_hr%24)
    total_time_day = int(total_time_hr/24)
    print("\nThe total travel time corresponding to your choosen filters is: {} days and {}hrs {}mins {}secs."
          .format(total_time_day,hr_rem,min_rem, sec_rem))

    # display mean travel time
    avg_time_sec = df['Trip Duration'].mean()
    asec_rem = int(avg_time_sec % 60)
    avg_time_min = avg_time_sec / 60
    amin_rem = int(avg_time_min % 60)
    avg_time_hr = avg_time_min / 60
    ahr_rem = int(avg_time_hr % 24)
    avg_time_day = int(avg_time_hr / 24)
    print("\nThe mean travel time corresponding to your choosen filters is: {} days and {}hrs {}mins {}secs.."
          .format(avg_time_day,ahr_rem,amin_rem, asec_rem))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Number of Users Vs Subscribers:\n{}".format(user_types))
    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Number of Male Vs Females:\n{}".format(gender))
    except:
        print("No information about gender is provided in Washington Dataset\n")
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print("The earliest year of birth of Bike Users is:{}\n"\
              "The most recent year of birth of Bike Users is:{}\n"\
              "The most common year of birth among Bike Users is:{}\n"
              .format(earliest_yob, most_recent_yob, most_common_yob))
    except:
        print("No information about year of birth is provided in Washington Dataset\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """
        Display raw data based on the choosen city without any filtration by month or by day.

        Args:
            (str) city - name of the city to analyze

    """

    start = 0
    end = 4
    df = pd.read_csv(CITY_DATA[city])
    while True:
        display = input("Do you want to show you the raw data? Press 'Yes' to show 5 rows or 'No'" \
                        " if you want to skip to the next step\n")
        if display.lower() == 'yes':
            print(df.loc[start:end])
            start = start+5
            end = end+5
        if display.lower() == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
