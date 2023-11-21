import tkinter
from tkinter import Tk, Button
from tkinter import ttk  # importing the ttk module for combobox (dropdown)
from tkcalendar import Calendar
from Main import *
labels = []

class ConnectionManagerGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.upper_frame = tkinter.Frame(self.main_window, width=800, height=600)
        self.upper_frame2 = tkinter.Frame(self.main_window, width=800, height=600)
        self.body_frame = tkinter.Frame(self.main_window, width=800, height=600)
        self.body_frame2 = tkinter.Frame(self.main_window, width=800, height=600)
        self.lower_frame = tkinter.Frame(self.main_window, width=800, height=600)
        self.main_window.geometry('800x600')

        # button for reveal
        self.reveal_button = tkinter.Button(self.upper_frame, text='REVEAL', command=self.display_prompt)
        self.reveal_button.pack()

        # dropdown display for selecting which connection to update
        self.update_var = tkinter.StringVar()
        self.update_options = self.get_sorted_data()
        self.update_var.set(self.update_options[0])
        self.update_dropdown = ttk.Combobox(self.upper_frame, textvariable=self.update_var, values=self.update_options)
        self.update_dropdown.pack()

        self.update_name = tkinter.Label(self.upper_frame2, text='Updated name: ')
        self.update_name_entry = tkinter.Entry(self.upper_frame2, width=10)
        self.update_date = tkinter.Label(self.upper_frame2, text='Updated date: ')
        self.update_date_entry = tkinter.Entry(self.upper_frame2, width=10)
        self.update_name.pack(side='left')
        self.update_name_entry.pack(side='left')
        self.update_date.pack(side='left')
        self.update_date_entry.pack(side='left')
        self.update_button = tkinter.Button(self.upper_frame2, text='UPDATE', command=self.get_sorted_data)
        self.update_button.pack()
        self.spacing = tkinter.Label(self.upper_frame2, text=' ')
        self.spacing.pack()

        # add functionality
        self.calendar = (Calendar(self.body_frame, selectmode='day', date_pattern='yyyy-mm-dd'))
        self.calendar.pack()
        self.prompt_name = tkinter.Label(self.body_frame, text='Name to add: ')
        self.add_name = tkinter.Entry(self.body_frame, width=10)
        # self.prompt_date = tkinter.Label(self.body_frame, text='Date to add: ')
        # self.add_date = tkinter.Entry(self.body_frame, width=10)
        self.add_button = tkinter.Button(self.body_frame, text='ADD', command=self.add)
        self.prompt_name.pack(side='left')
        self.add_name.pack(side='left')
        # self.prompt_date.pack(side='left')
        # self.add_date.pack(side='left')
        self.add_button.pack(side='left')

        # delete functionality
        self.prompt_removal_name = tkinter.Label(self.body_frame2, text='Name to remove: ')
        self.remove_name = tkinter.Entry(self.body_frame2, width=10)
        self.prompt_removal_date = tkinter.Label(self.body_frame2, text='Date to remove: ')
        self.remove_date = tkinter.Entry(self.body_frame2, width=10)
        self.remove_button = tkinter.Button(self.body_frame2, text='REMOVE', command=self.delete)
        self.prompt_removal_name.pack(side='left')
        self.remove_name.pack(side='left')
        self.prompt_removal_date.pack(side='left')
        self.remove_date.pack(side='left')
        self.remove_button.pack(side='left')

        # pack frames
        self.upper_frame.pack()
        self.upper_frame2.pack()
        self.body_frame.pack()
        self.body_frame2.pack()
        self.lower_frame.pack()

        tkinter.mainloop()

    def get_sorted_data(self):
        lst = []
        for name in get_sorted_data()['Name']:
            lst.append(name)
        return lst

    def display_prompt(self):
        for item in labels:
            item.destroy()
        for name, date in connection_map.items():
            label = tkinter.Label(self.lower_frame, text=[name, date])
            label.pack()
            labels.append(label)

    def add(self):
        new_date = datetime.datetime.strptime(self.calendar.get_date(), "%Y-%m-%d").strftime("%Y-%m-%d")
        new_name = self.add_name.get()
        connection_map[new_name] = new_date

    def delete(self):
        pass


pull_connections()
run_gui = ConnectionManagerGUI()
