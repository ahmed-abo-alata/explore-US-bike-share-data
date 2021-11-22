import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data=['all','january', 'february', 'march', 'april', 'may', 'june']
day_data=['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
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
    while True:
        try:
            city=input('do you want to explore data about washington, chicago,or new york city?').lower()
            if city not in CITY_DATA :
                raise ValueError
            break
        except:
            print("that's not a valid input.\nnote: spelling is segnificant.")
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            month=input("if you want to explore data of all months please enter 'all',\n and if you want to explore data of a  specific month please enter the month name: ").lower()
            if month not in  month_data:
                raise ValueError
            break
        except:
            print("that's not a valid input.\nnotes: 1-spelling is segnificant.\n       2-data is only about the frist 6 months of the year")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day =input("if uou want to explore data of all days of the week please enter 'all'\n and if you want to explore data of a  specific day please enter the day name: ").title()
            if day not in  day_data:
                raise ValueError
            break
        except:
            print("that's not a valid input.\n notes: spelling is segnificant.")
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.weekday_name

    if month!='all':
        month =  month_data.index(month)
        df=df[df['month']==month]
    if day!='All':
        df=df[df['day']==day]
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    """it dose not make sense if the program displays the most common month and day if the prugram user have already chosen to show data of specific month or day, fo iam going to use if statement"""
    # TO DO: display the most common month
    if month=='all'and day=='All':
        most_common_month=df['month'].mode()[0]
        print('the most common month: ',most_common_month)
    # TO DO: display the most common day of week
        most_common_day=df['day'].mode()[0]
        print('the most common day: ',most_common_day)
    # TO DO: display the most common start hour
        df['hour']=df['Start Time'].dt.hour
        most_common_hour=df['hour'].mode()[0]
        print('the most common hour: ',most_common_hour)
    elif day=='All'and month!='all':
        most_common_day=df['day'].mode()[0]
        print('the most common day: ',most_common_day)
        df['hour']=df['Start Time'].dt.hour
        most_common_hour=df['hour'].mode()[0]
        print('the most common hour: ',most_common_hour)
    elif month=='all'and day!='All':
        most_common_month=df['month'].mode()[0]
        print('the most common month: ',most_common_month)
        df['hour']=df['Start Time'].dt.hour
        most_common_hour=df['hour'].mode()[0]
        print('the most common hour: ',most_common_hour)
    else:
        df['hour']=df['Start Time'].dt.hour
        most_common_hour=df['hour'].mode()[0]
        print('the most common hour: ',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station=df['Start Station'].mode()[0]
    print('the most common start station is: ',most_start_station)
    # TO DO: display most commonly used end station
    most_end_station=df['End Station'].mode()[0]
    print('the most common end station is: ',most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip']='from '+df['Start Station']+' to '+df['End Station']
    most_trip=df['trip'].mode()[0]
    print('the most popular trip is ',most_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('the total travel time = ',total_travel_time,'secounds.')

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('the mean travel time = ',mean_travel_time,'secounds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    """In chicago data, i noticed one user with a 'user type' 'dependent', so i consedered it as outlier and the next line of code is to remove it"""
    df=df[df['User Type']!='Dependent']

    print('there are two user types:Subscriber and Customer, and there counts are as following:')
    print(df['User Type'].value_counts())
    if city=='washington':
        print('washington data dont have any information about Gender or Date Of Birth')
    else:
    # TO DO: Display counts of gender
        print('\nnote: the data of gender and age is only available for subscribers.\nGender count for subscribers is as following:')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        most_recent=int(df['Birth Year'].max())
        print('\nthe youngest subscriber was born in :',most_recent)
        earliest=int(df['Birth Year'].min())
        print('the oldest subscriber was born in :',earliest)
        most_common=int(df['Birth Year'].mode()[0])
        print('the most common year of bieth for subscribers is:',most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data=input('\nwould you like view 5 rows of individual trip data? enter yes or no\n').lower()
    start_loc=0
    while  view_data=='yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_data =input('do you wish to view the next 5 rows of the data? enter yes or no\n').lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
