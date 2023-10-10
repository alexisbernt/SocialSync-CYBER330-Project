import csv

connections = {}


# Open the CSV file and iterate through the rows adding it to the dictionary
def get_dict():
    with open('StreakCounter.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            item, term =row
            connections[item] = term


get_dict()

# Display all names and date in a table for to the user
for item in connections:
    print(item, connections[item])
