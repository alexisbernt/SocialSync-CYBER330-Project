#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import csv
from datetime import timedelta


connections_file = 'StreakCounter.csv'
last_run_file = 'last_run.txt'


def set_last_run_date():
    current_date = datetime.datetime.now()
    with open(last_run_file, "w") as file:
        file.write(current_date.strftime("%Y-%m-%d"))


def read_last_run_date():
    try:
        with open(last_run_file, "r") as file:
            last_run_date_str = file.read()
            run_date = datetime.datetime.strptime(last_run_date_str, "%Y-%m-%d")
            return run_date.strftime("%Y-%m-%d")
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None


def get_sorted_data():
    data = pd.read_csv(connections_file)
    # Convert the 'Date' column to a datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    # Sort the DataFrame by the 'Date' column in ascending order
    data_sorted = data.sort_values(by='Date', ascending=True)
    # Reset the index with drip = True
    data_sorted = data_sorted.reset_index(drop=True)
    # Print sorted data
    return data_sorted


def get_overdue_connections():
    for date in get_sorted_data()['Date']:
        date = date.strftime("%Y-%m-%d")
        if date <= read_last_run_date():
            print(date)
set_last_run_date()
read_last_run_date()
get_overdue_connections()


# In[2]:


import csv

pending_list = []

# print(pending_list)

def get_current_connections(pending_list):
    with open('StreakCounter.csv') as file_obj:
        with open(last_run_file, "r") as file:
            reader_obj = csv.reader(file) 
            for date in get_sorted_data()['Date']:
                date = date.strftime("%Y-%m-%d")
                if date == read_last_run_date():
                    print('Here is your current connection need: ')
                    print(date)
                    # iterate over each row in the csv file using reader object 
                for row in reader_obj: 
                    print(row)
                    # Then should we store this item in a list until fufilled (?)
                    pending_list.append(row) 
                print(pending_list)

get_current_connections(pending_list)


# In[3]:


def display_prompt(pending_list):
    if pending_list == 0:
        print('No connections to be made at this time.')
        print('Would you like to add connections?')
        # create way for user to add connections ... 
    for item in pending_list:
        connect_prompt = input('Did you connect with your assigned connections? (y/n): ')
        if connect_prompt == 'y':
            # remove the item from pending list
            pending_list.remove(item)
            # update the file to state that connection was made 
            print('Great! You made your connection. When would you like to connect with this person again?')
            print("a. 2 days from now.")
            print("b. One week from now.")
            print("c. One month from now.")
            begin_date_string = str(read_last_run_date())
            begin_date = datetime.datetime.strptime(begin_date_string, "%Y-%m-%d")
            connect_again = input('When would you like to connect with this person again? (a,b,c): ')
            # if the next connection is two days from now
            if connect_again == 'a':
                end_date = begin_date + timedelta(days=2)
            # if the next connection is one week from now
            if connect_again == 'b':
                end_date = begin_date + timedelta(days=7)
            # if the next connection is one month from now 
            if connect_again == 'c':
                end_date = begin_date + timedelta(days=30)
            if connect_again != 'a' or 'b' or 'c':
                print('Invalid Input.')
        while connect_prompt == 'n': 
            print('Please connect now with the assigned connection.')
            connect_prompt = input('Did you connect with your assigned connections? (y/n): ')
            if connect_prompt == 'y':
                # remove the item from pending list
                pending_list.remove(item)
            else:
                print('Error. Invalid input.')
        if connect_prompt != 'y' or 'n':
            print('Please try again.')
            
        
display_prompt(pending_list)


# In[ ]:




