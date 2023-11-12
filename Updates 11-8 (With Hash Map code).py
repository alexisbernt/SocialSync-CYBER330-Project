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

print(pending_list)

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


# In[1]:


# abstract base classes 
from collections.abc import MutableMapping

class MutableMapping:
    class Item:
        __slots__ = '_key', '_value'
    def __init__(self, key, value):
        self._key = key
        self._value = value
        
    def __init__(self, items):
        self._items = {}  # Use a dictionary to store key-value pairs initially

    def __getitem__(self, key):
        return self._items[key]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __delitem__(self, key):
        del self._items[key]

    def __iter__(self):
        return iter(self._items)
    
    def __len__(self):
        return len(self._items)

    def __eq__(self, other):
        return self._key == other._key  # compare items based on their keys

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self._key < other._key  # compare items based on their keys

    def __contains__(self, key):
        return key in self._items


# In[2]:


# Example use / check:
if __name__ == "__main__":
    class MapBase(MutableMapping):
        pass

    my_map = MutableMapping(None)
    my_map['key1'] = 'a'
    my_map['key2'] = 'b'

    print(my_map['key1'])  # Output: 'a'
    print('key2' in my_map)  # Output: should be True
    print(len(my_map))  # Output: 2
    print(' ')
    print(my_map)  # Output: MapBase({'key1': 'value1', 'key2': 'value2'})
    
# # attempt to get each value (having issues with):
#     for x in range(len(my_map)):
#         print(my_map.__getitem__[x])


# In[3]:


class MapBase(MutableMapping):
    class _Item:
        __slots__ = '_key', '_value'
    def __init__(self, k, v):
        self._key = k
        self._value = v 
        
    def __eq__(self, other):
        return self._key  == other._key # compare items based on their keys
    
    def __ne__(self, other): 
        return not (self == other)
    
    def __lt__(self, other):
        return self._key < other._key # compare items based on their keys 
    
    


# In[4]:


# class HashMapBase(MapBase):
class HashMapBase(MapBase):
    
    def __init__(self, cap=11, p=109345121):
        # create an empty hash-table map
        self._table = cap * [None]
        self._n = 0 # number of entries in the map
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
        self._items = [] # a list to store key-value pairs

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2*len(self._table)-1)
            
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n -= 1
        
    def _resize(self,c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k,v) in old:
            self[k] = v
            
    def _bucket_getitem(self, j, k):
        if self._table[j] is None:
            raise KeyError(f'Key not found: {k}')
        for key, value in self._table[j]:
            if key == k:
                return value
        raise KeyError(f'Key not found: {k}')
            
    def _bucket_setitem(self, j, k, v):
        # way to store key-value pairs in _items
        self._items.append((k,v))
        


# In[5]:


from random import randrange

class HashMapBase:
    def __init__(self, cap=11, p=109345121):
        # create an empty hash-table map
        self._table = cap * [None]
        self._n = 0  # number of entries in the map
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)
        self._items = [] # a list to store key-value pairs

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
        
    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    def _bucket_getitem(self, j, k):
        if self._table[j] is None:
            raise KeyError(f'Key not found: {k}')
        for key, value in self._table[j]:
            if key == k:
                return value
        else:
            raise KeyError(f'Key not found: {k}')

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = []
            # iterates over elements of list stored in hash table at specific index
        for index, (key, value) in enumerate(self._table[j]):
            if key == k:
                self._table[j][index] = (k, v)
                return
        self._table[j].append((k, v))
        self._n += 1

    def _bucket_delitem(self, j, k):
        # iterates over elements of list stored in hash table at specific index
        for index, (key, value) in enumerate(self._table[j]):
            if key == k:
                del self._table[j][index]
                return
        # if the key is not found
        raise KeyError(f'Key not found: {k}')


# In[6]:


# create an instance of HashMapBase with default constructor values
ex_hash_map = HashMapBase()
ex_hash_map['key1'] = 'valuea'
ex_hash_map['key2'] = 'valueb'
ex_hash_map['key3'] = 'valuec'

print(ex_hash_map['key1'])  
print(ex_hash_map['key2'])  
print(ex_hash_map['key3'])  
# can add, retrieve, and delete key-value pairs in the hash map
# Add key-value pairs to ex_hash_map


# In[ ]:




