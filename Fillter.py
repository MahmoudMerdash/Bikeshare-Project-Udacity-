# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:37:44 2021

@author: DELL
"""

"""
Importing section 
"""
import ReadFile as rf
import pandas as pd 

###########################################################################################################################

chosing_lst = ['month', 'day', 'both', 'none'] # list to cobamre the entered user vlaue if it is not equal ask him/her again 
month_lst = ['January', 'February', 'March', 'April' ,'May', 'June','all'] # the six months that are in data files and the all indicates that the user will need all data in this months 
days_lst = ['Monday','Tuesday','Wedensday', 'Thursday','Friday','Saturday','Sunday', 'all'] # same as months 


def fillter_method():
    """
    Ask user which method needed to analyze data
    Input:
        None

    Returns
    -------
    user_choice : TYPE
        DESCRIPTION. the name of method will be used 

    """
    user_choice = None # to save the user input  
    chosing_lst = ['month', 'day', 'both', 'none'] # list to cobamre the entered user vlaue if it is not equal ask him/her again 
    print("\nWould you like to filter the data by month, day, both , or not at all? type none for no time filter\n")
    while True: # loop to check the imput from user it will break after getting tight answer 
        try:
            user_choice = input().lower().strip() # lower and strip methods to remove spaces and get input in lower case only 
            if user_choice in chosing_lst:
                break
            else:
                print("please Enter the correct choice [month, day, both, none\n")
        except Exception as e:
            print("you cased an error {}".format(e))
    
    return user_choice




def get_fillter(method):
    
    """
    Ask use to specify the month and day to analyz data
    Input:
        (str) method the filter method that needed to be analyze data monthly, daily, both or none
    Output: 
        (str) the name of the month that speciefied to analyze 
        (str) the name of the day that speciefied to analyze 
        or None if the input method is none
    """
    month  = None
    day = None
    # USEING OF LOOP JUST TO MAKE SURE THE USER ENTERED THE CORRECT VALUE OF MONTH AND DAY 
    
    if method == 'month':
        while True:
            month = input("Which month? January, February, March, Aprilm May, or June?").lower().strip().capitalize()
            if month in month_lst:
                break
            else:
                month = input("Please ENter valie value January, February, March, Aprilm May, or June?").lower().strip().capitalize()
    elif method == 'day':
        day = input("which day? (Sunday.....etc)").lower().strip().capitalize()
        while True:
            if day in days_lst:
                break
            else:
                day = input("please enter the coorect name of the day\n").lower().strip().capitalize()
    elif method == 'both':
        month = input("Which month? January, February, March, April, May, or June?").lower().strip().capitalize()
        day = input("which day? (Sunday.....etc)").lower().strip().capitalize()
        while True:
            if month in month_lst:
                if day in days_lst:
                    break
                else:
                   day = input("please enter the coorect name of the day\n").lower().strip().capitalize()
            else:
                month = input("Please ENter valie value January, February, March, April, May, or June?").lower().strip().capitalize()
    return month, day
    
def apply_filletr():
    """
    Apply filter data frame that loaded from one of three files 
    input:
        None.
    Output:
        return the fillter data frame regarding the user choice 
    
    """
    file_name = rf.read_file_name() # get the name of file from user 
    methond_name = fillter_method() #get the method rquired to apply filter 
    month, day = get_fillter(methond_name) # get the names of month and days to fillter the data 
    df = rf.load_data(file_name) # load files 
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert start time cells to time format 
    df['Month'] = df['Start Time'].dt.month # creat a new column of months 
    df['Days_names'] = df['Start Time'].dt.dayofweek #creat new column of each days 
    df['Days_num'] = df['Start Time'].dt.day #create day in number forms 
    if month != "all" and month is not None:
        month = month_lst.index(month)+1 #get the equivelant numer of month 
        df = df[df['Month'] == month] # get the only date frame with 
    if day != 'all' and day is not None:
        df = df[df['Days_names'] == days_lst.index(day)]
        
    return df 

if __name__ == '__main__':
    df = apply_filletr()
    print(df)