#!/usr/bin/env python
# coding: utf-8

# ## CYBER 330 FINAL 

# In[1]:


# store information in file (if streak is missed then the streak is wiped)
# if streak is maintained the data is stored 
# make sure data is not wiped 


# In[7]:


# part 1 through using 'import csv'

import csv ,operator

connections = {}

# Open the CSV file and iterate through the rows adding it to the dictionary
def get_dict():
    with open('CSVFiles/StreakCounter.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            item, term =row
            connections[item] = term


get_dict()

# Display all names and date in a table for to the user
for item in connections:
    print(item, ',',connections[item])

# part 1 Using the same csv file but opening with pandas and then sorting via pandas

data=csv.reader(open('CSVFiles/StreakCounter.csv'), delimiter='/')
data=sorted(data,key=operator.itemgetter(0),reverse=True)


# In[1]:


# 1. Dictionary example with people and sequences of dates
import pandas as pd
data = pd.read_csv('CSVFiles/StreakCounter.csv')
print(data)
# print(sc.to_string())


# In[2]:

# This sorting of the data is similar to material covered in chapter 9 (Sorted and Unsorted List/Queue Implementation)
import pandas as pd

def get_date(csv_file):
    data = pd.read_csv('CSVFiles/StreakCounter.csv')
    # Convert the 'Date' column to a datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    # Sort the DataFrame by the 'Date' column in ascending order
    data_sorted = data.sort_values(by='Date', ascending=True)
    # Reset the index with drip = True 
    data_sorted = data_sorted.reset_index(drop=True)
    # Print sorted data
    print(data_sorted)
# Calling with specific file name (StreakCounter.csv)
get_date('CSVFiles/StreakCounter.csv')


# In[3]:


# Consecutive days run done

import datetime
# using a file to store the last run date 
file_path = 'CSVFiles/last_run.txt'
# this list will do the storage (store items)
user_activity = []

# initializing a streak counter 
streak = 0

def read_last_run_date():
    try:
        with open(file_path, "r") as file:
            last_run_date_str = file.read()
            return datetime.datetime.strptime(last_run_date_str, "%Y-%m-%d")
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None
    
# simulating a list of items (replace with data)
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# the condition for a streak 
if len(user_activity) >= 2:
    streak += 1 
    
def write_current_date():
    current_date = datetime.datetime.now()
    with open(file_path, "w") as file:
        file.write(current_date.strftime("%Y-%m-%d"))

def count_consecutive_days():
    last_run_date = read_last_run_date()
    current_date = datetime.datetime.now()

    if last_run_date is None:
        # If the program hasn't been run before, set the last run date and return 1
        write_current_date()
        return 1
    
# Calculate the time difference between the current date and the last run date
    time_difference = current_date - last_run_date

    # Check if the difference is exactly one day
    if time_difference.days == 1:
        write_current_date()
        return time_difference.days + 1
    else:
        # If the program wasn't run consecutively, reset the count to 1
        write_current_date()
        return 1

consecutive_days = count_consecutive_days()
print(f"Consecutive days run: {consecutive_days}")


# In[ ]:


# IDEAS 

# highlight a user 
    # Example: A university's "user of the week"

