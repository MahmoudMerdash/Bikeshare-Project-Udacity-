# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:15:41 2021

@author: DELL
"""

import pandas as pd 

def read_file_name()->str:
    """
        Read file name form user and return it to be used in another function 
        
        Arg:
            None
        Return 
        file Name that used needs to explore its data
    """
    city_list = ['Chicago', 'New York', 'Washington']
    print("Hello let's explore some US bike Share Data\n\n")
    while True:
        try:
            file_name = input("Enter the name of city to explore its data [Chicago, New York, Washington ").lower().title().strip()
            if file_name not in city_list: 
                print('\n******************************************')
                print('You enter wrong city')
                print('*******************************************\n')
            else:
                
                break
            
        except:
            print('You might enter invalid input please ')
    return file_name


            
def load_data(file_name:str):
    """
       Loads data for the specified city and filters by month and day if applicable.
       Please make sure the three files have names of chicago, new york and washington and all in csv format
       if you get an error check file naming and location 

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """ 
    df = None

    file_directory = {'Chicago':'chicago.csv',
                      'New York':'new_york_city.csv',
                      'Washington':'washington.csv'}
    df = pd.read_csv(file_directory[file_name])
        
            
    return df 
    
    
if __name__ == '__main__':
    name = read_file_name()   
    df = load_data(name) 
    print(df.head())
    print(df['Gender'].value_counts())
    
    