import csv
from hash_map_base import HashMapBase
from datetime import datetime

connections_file = '_internal/SocialSync.csv'
connection_map = HashMapBase()


# pull all data from the csv files into the hash map
def pull_connections():
    with open(connections_file, "r", newline='') as file:
        fileReader = csv.reader(file)
        for name, date in fileReader:
            if name == 'Name':
                pass
            else:
                date = datetime.strptime(date, "%Y-%m-%d")
                date = date.strftime("%Y-%m-%d")
                connection_map[name] = date


# push all connections in the hash map into the CSV style to store
def push_connections():
    with open(connections_file, "w", newline='') as file:
        fileWriter = csv.writer(file)
        fileWriter.writerow(['Name', 'Date'])
        for name, date in connection_map.items():
            fileWriter.writerow([name, date])
