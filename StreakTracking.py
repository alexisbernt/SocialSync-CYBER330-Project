import pandas as pd
import datetime


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
            return datetime.datetime.strptime(last_run_date_str, "%Y-%m-%d")
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
        if date <= read_last_run_date():
            print(date)


set_last_run_date()
get_overdue_connections()
