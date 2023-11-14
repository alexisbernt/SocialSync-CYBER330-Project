import pandas as pd
import datetime
import csv
from datetime import timedelta
from hash_map_base import HashMapBase

# designate File locations, create hashmap object, create empty list for connections
connections_file = 'CSVFiles/StreakCounter.csv'
last_run_file = 'CSVFiles/last_run.txt'
connection_map = HashMapBase()
pending_list = []


# set the last run date to the current date
def set_last_run_date():
    current_date = datetime.datetime.now()
    with open(last_run_file, "w") as file:
        file.write(current_date.strftime("%Y-%m-%d"))


# return the date stored in the last run date file
def read_last_run_date():
    try:
        with open(last_run_file, "r") as file:
            last_run_date_str = file.read()
            run_date = datetime.datetime.strptime(last_run_date_str, "%Y-%m-%d")
            return run_date.strftime("%Y-%m-%d")
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None


# sort all data from the csv file by date
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


# return all connections that are current or older than the last run date
def get_overdue_connections():
    for date in get_sorted_data()['Date']:
        date = date.strftime("%Y-%m-%d")
        if date <= read_last_run_date():
            print(date)


# add all connections equal to the last run date to a connections list
def get_current_connections(pending_list):
   # open the file
    with open(last_run_file, "r") as file:
        reader_obj = csv.reader(file)
        for name, date in connection_map.items():
            if date == read_last_run_date():
                print('Here is your current connection need: ')
                print(name, date)
                pending_list.append(name)


# ask the user to make their connections
def display_prompt(pending_list):
    if len(pending_list) == 0:
        print('No connections to be made at this time.')
        add_connect = input('Would you like to add connections? (y/n): ')
        # # create way for user to add connections ...
        if add_connect == 'y':
            add_name = input('What is the name of the person to connect with? ')
            add_date = input('When would you like to connect with this person? ')
            connection_map[add_name] = add_date
        elif add_connect == 'n':
            return
        else:
            print('Error. Please proceed and try again.')
            display_prompt(pending_list)

    elif len(pending_list) != 0:
        connect_prompt = input('Did you connect with ' + pending_list[0] + '? (y/n): ')
        if connect_prompt == 'y':
            update_connections()
        elif connect_prompt == 'n':
            while connect_prompt == 'n':
                print('Please connect now with the assigned connection.')
                display_prompt(pending_list)
        elif connect_prompt != 'y' or 'n':
            print('Please try again.')
    # if len(pending_list) != 0:
    #     display_prompt(pending_list)


# ask the user when they want the next connection and update it in the hash map
def update_connections():
    # update the file to state that connection was made
    print('Great! You made your connection. When would you like to connect with this person again?')
    print("a. 2 days from now.")
    print("b. One week from now.")
    print("c. One month from now.")
    begin_date_string = str(read_last_run_date())
    begin_date = datetime.datetime.strptime(begin_date_string, "%Y-%m-%d")
    connect_again = input('When would you like to connect with this person again? (a,b,c): ').lower()
    # if the next connection is two days from now
    if connect_again == 'a':
        end_date = begin_date + timedelta(days=2)
        connection_map[pending_list.pop(0)] = end_date.strftime("%Y-%m-%d")
    # if the next connection is one week from now
    elif connect_again == 'b':
        end_date = begin_date + timedelta(days=7)
        connection_map[pending_list.pop(0)] = end_date.strftime("%Y-%m-%d")
    # if the next connection is one month from now
    elif connect_again == 'c':
        end_date = begin_date + timedelta(days=30)
        connection_map[pending_list.pop(0)] = end_date.strftime("%Y-%m-%d")
    elif connect_again != 'a' or 'b' or 'c':
        print('Invalid Input.')


# update the hash map with everything from the csv file
def pull_connections():
    for name, date in zip(get_sorted_data()['Name'], get_sorted_data()['Date']):
        date = date.strftime("%Y-%m-%d")
        connection_map[name] = date


# push all connections in the hash map into the CSV style to store
def push_connections():
    with open(connections_file, "w", newline='') as file:
        fileWriter = csv.writer(file)
        fileWriter.writerow(['Name', 'Date'])
        for name, date in connection_map.items():
            fileWriter.writerow([name, date])


pull_connections()

get_current_connections(pending_list)
display_prompt(pending_list)

push_connections()
