# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:58:09 2021

@author: DELL
"""
#this file has all fuctions that are used to manipulate the data frame from imported csv of bikeshare

import Fillter as ft
import time 

df, month, day,file_name = ft.apply_filletr() # to load data then apply the disered fillter 


def time_state(df,month,day):
    """
    Display ststistics on the most frequent time of travel
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION. the filter dataframe

    Returns
    -------
    None.

    """
    print("-"*60)
    print("\nCalculating the Most Frequent Time of travel......\n")
    start_time = time.time() # hold the processor time at this operation
    if month == 'all' or month is None: # if the user not select specific month from start 
        popular_month = df['Month'].mode()[0] # return the most repeated value in Month column 
        print("The most Populr Month is {}".format(popular_month))
    if day == 'all' or day is None:     # if the user did not select specific day from start new 
        popular_day = ft.days_lst[df['Days_names'].mode()[0]]
        print("The Most Popular Day is {}".format(popular_day))
        
    
    popular_hr = (df['Start Time'].dt.hour).mode()[0]
    print("The Most Popluar Hour is {}".format(popular_hr))
    
    print("This took {} secondes..".format(time.time()-start_time))
    print('-'*60)
  
    
def station_state(df):
    """
    Display the Most Popular start station and start to end station 

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.the filter dataframe

    Returns
    -------
    None.

    """
    print("\n Calculating the most start station and start to end station\n")
    start_time = time.time() # hold the processor time at this operation
    popluart_start_station = df['Start Station'].mode()[0] # get the most repeated station name in start station 
    df['Start To End'] = df['Start Station']+str(' to ')+df['End Station']
    popular_start_to_end = df['Start To End'].mode()[0]
    print("The Most Popluar Start Station is {}".format(popluart_start_station))
    print("The Most Popular Start to End Station is {}".format(popular_start_to_end))
    print("it took {} seconds to calculate this operations".format(time.time()-start_time))
    
    
def trip_duration_states(df):
    """
    To display the total and mean time that have been taken through the specifc fillter period 

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.the filter dataframe

    Returns
    -------
    None.

    """
    print("\n Calculating the total trip time that have been take through the fillter priod\n")
    start_time = time.time()
    # To display the total time that have been taken through the specifc fillter period 
    total_time = df['Trip Duration'].sum()
    print('{:02f} hours:{:02f} minutes:{:02f} seconds'.format(total_time//3600, (total_time%3600)//6, total_time%3600%60))
    # T0 display mean travel time
    average_duration = round(df['Trip Duration'].mean()) # round to remove dicemal numbers 
    print('{:02f} hours:{:02f} minutes:{:02f} seconds'.format(average_duration//3600, (average_duration%3600)//6, average_duration%3600%60))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    
def user_state(df):
    """
    Diplat the type and number of users that used to use bikeshare program.
    1. user type 
    2. check if there is geneder column diplace the number of each type 
    3. check if there is birth date column display eldest, youngest and commen year 
    Parameters
    ----------
    df : TYPE
        DESCRIPTION. DESCRIPTION.the filter dataframe

    Returns
    -------
    None.

    """
    print("\n Calcualting user state \n")
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    print("The type of user bby number are given below\n\n{}".format(user_type))
    try:
        user_gender = df['Gender'].value.counts()
        print("Type of user is {}".format(user_gender))
    except Exception as e:
        print("You Get an Error {}".format(e))
        print("Oops your Data does not have gender column\n")
    try:
        eldest = int(df['Birth Year'].min())
        youngest = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("The eldest year of birth: {}\nThe Youngest year of birth: {}\nThe common year of birth: {}".format(eldest,youngest,common_year))    
    except Exception as e:
        print("You Get an Error {}".format(e))
        print("Oops your Data does not have Birth Date column\n") 
        
    print("\n this took {:02f} seconds".format(time.time()-start_time))
    print('-'*60)




if __name__ =="__main__":
    
    print(df)   
    time_state(df,month,day)
    station_state(df)
    trip_duration_states(df)
    user_state(df)