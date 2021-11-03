# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:41:56 2021

@author: DELL
"""
import DataManip as dm 

def main():
    city = dm.file_name #get the fist city that the user entered 
    
    dm.time_state(dm.df,dm.month,dm.day)
    dm.station_state(dm.df)
    dm.trip_duration_states(dm.df)
    dm.user_state(dm.df)
    restart = input("\nWould you like to restart? Enter ues or no.\n")
    while restart.lower() == 'yes':
        df,month, day, city = dm.ft.apply_filletr()
        dm.time_state(df,month,day)
        dm.station_state(df)
        dm.trip_duration_states(df)
        dm.user_state(df)
        restart = input("\nWould you like to restart? Enter ues or no.\n")
        if restart.lower() != 'yes':
            break
    dm.ft.rf.display_rawData(city)
        
    
if __name__ == "__main__":
    main()
    