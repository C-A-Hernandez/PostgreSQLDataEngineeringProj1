import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def user_input(city):
    
        city=('chicago','new york','washington')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_menu = "\t1. Chicago\n\t2. New York City\n\t3. Washington"
    while True:
        
        print('Hello! Let\'s explore some US bikeshare data!')
        print("\nPick a city.  Enter city's number or name from items below:")
        print(city_menu)
        city_input=input("\n\tYour choice please: ")
        if city_input == "1" or city_input.lower() == "chicago":
            city = "chicago"
            break
        elif city_input == "2" or city_input.lower() == "new york city":
            city = "new york city"
            break
        elif city_input == "3" or city_input.lower() == "washington":
            city = "washington"
            break
            

    # TO DO: get user input for month (all, january, february, ... , june)
    month_menu = "\n\t1. All\n\t2. January\n\t3. February\n\t4. March\n\t5. April\n\t6. May\n\t7. June"
    while True:
        
        print("\nPick a month.  Enter month's number or name from items below:")
        print(month_menu)
        month_input = input("\n\tYour choice please: ")
        if month_input == "1" or month_input.lower() == "all":
            month = 'all'
            break 
        elif month_input == "2" or month_input.lower() == "january":
            month = 'january'
            break
        elif month_input == "3" or month_input.lower() == "february":
            month = 'february'
            break
        elif month_input == "4" or month_input.lower() == "march":
            month = 'march'
            break
        elif month_input == "5" or month_input.lower() == "april":
            month = 'april'
            break
        elif month_input == "6" or month_input.lower() == "may":
            month = 'may'
            break
        elif month_input == "7" or month_input.lower() == "june":
            month = 'june'
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_menu = "\n\t1. All\n\t2. Sunday\n\t3. Monday\n\t4. Tuesday\n\t5. Wednesday\n\t6. Thursday\n\t7. Friday\n\t8. Saturday"
    while True:
        
        print("\nPick a day.  Enter day's number or name form items below:")
        print(day_menu)
        day_input = input("\n\tYour choice please: ")
        if day_input == "1" or day_input.lower() == "all":
            day = 'all'
            break
        if day_input == "2" or day_input.lower() == "sunday":
            day = 'sunday'
            break
        if day_input == "3" or day_input.lower() == "monday":
            day = 'monday'
            break
        if day_input == "4" or day_input.lower() == "tuesday":
            day = 'tuesday'
            break
        if day_input == "5" or day_input.lower() == "wednesday":
            day = 'wednesday'
            break
        if day_input == "6" or day_input.lower() == "thursday":
            day = 'thursday'
            break
        if day_input == "7" or day_input.lower() == "friday":
            day = 'friday'
            break
        if day_input == "8" or day_input.lower() == "saturday":
            day = 'saturday'
            break
            
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
    #load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                                      
    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
                                      
    #filter by month if applicable
    if month != 'all':
        #use the index of the months list to get the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #filter by month to create the new dataframe
        df = df[df['month'] == month]
                                      
    #filter by day of week if applicable
    if day != 'all':
       #filter by day of week to create the new dataframe
       df = df[df['day_of_week'] == day.title()]
                                      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] =df['Start Time'].dt.weekday_name
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    
    print('Most Common Month:', most_common_month)
    
    # TO DO: display the most common day of week
    
    most_common_day = df['day_of_week'].mode()[0]
    
    print('Most Common Day of Week:', most_common_day)


    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    
    most_common_start_hour = df['hour'].mode()[0]
    
    print('Most Common Start Hour:', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    
    print('Most Commonly Used Start Station:', most_commonly_used_start_station)
    
    


    # TO DO: display most commonly used end station
    
    most_commonly_used_end_station = df['End Station'].mode()[0]
    
    print('Most Commonly Used End Station:', most_commonly_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip

    df['Trip'] = 'From "' + df['Start Station'] + '"to"' + df['End Station'] + '"'
    
    commonly_used_combo_station = df['Trip'].mode()[0]
        
    print('Most Frequent Combination of Start Station and End Station Trip:\n\t', commonly_used_combo_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    
    print ('Total Travel Time:\n', total_travel_time)


    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    
    print ('Mean Travel Time', mean_travel_time) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    counts_of_user_types = df['User Type'].value_counts()
    
    print('Counts of User Types:\n', counts_of_user_types)
    
    


    # TO DO: Display counts of gender
    
    try:
    
         counts_of_gender = df['Gender'].value_counts()
    
         print('Counts of Gender:\n', counts_of_gender)
    
    except:
        
        print ("\n Gender data not available.")


    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:    

         earliest_year_of_birth = df['Birth Year'].min()
    
         print('Earliest Year of Birth:', earliest_year_of_birth)
    
    except:
        
        print ("\n Year of birth data not available.")
        
    try:

         most_recent_year_of_birth = df['Birth Year'].max()
    
         print('Most Recent Year of Birth:', most_recent_year_of_birth)
        
    except:
        
        print ("\n Year of birth data not available.")
    
    try:
    
        most_common_year_of_birth = df['Birth Year'].mode()[0]
    
        print('Most Common Year of Birth:', most_common_year_of_birth)
        
    except:
        
        print ("\n Year of birth data not available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print("City: {}, Month: {}, Day: {}".format(city.title(), month.title(), day.title()))
        raw_data_view = input('\n Would you like to view 5 lines of raw data? Please enter yes or no: ')
        while raw_data_view.lower() == 'yes':
            print('Print out of the five lines of raw data:')
            count = 0
            print(df.iloc[count:count+5])
            count = count + 5
            break
            
        
        raw_data_view = input('\n Would you like to view 5 additional lines of raw data? \n Please enter yes or no: ')
        while raw_data_view.lower() == 'yes':
            print('Print out of the additional five lines of raw data:')
            print(df.iloc[count:(count + 5)])
            count = count + 5
            raw_data_view = input('\n Would you like to view 5 additional lines of raw data? \n Please enter yes or no: ')
            if raw_data_view.lower() != 'yes':
               break
                
       
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
