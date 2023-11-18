import tkinter
from tkinter import Tk, Button
from tkinter import ttk  # importing the ttk module for combobox (dropdown)
class ConnectionManagerGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.upper_frame = tkinter.Frame(self.main_window, width=800, height=600)
        self.upper_frame2 = tkinter.Frame(self.main_window, width=800, height=600)
        self.body_frame = tkinter.Frame(self.main_window, width=800, height=600)
        self.body_frame2 = tkinter.Frame(self.main_window, width=800, height = 600)
        self.lower_frame = tkinter.Frame(self.main_window, width=800, height=600)

        # button for reveal
        self.reveal_button = tkinter.Button(self.upper_frame, text='REVEAL', command=self.get_sorted_data())
        self.reveal_button.pack()

        # dropdown display for selecting which connection to update
        self.update_var = tkinter.StringVar()
        self.update_options = [self.get_sorted_data()]
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
        self.update_button = tkinter.Button(self.upper_frame2, text='UPDATE', command=self.get_sorted_data())
        self.update_button.pack()
        self.spacing = tkinter.Label(self.upper_frame2, text=' ')
        self.spacing.pack()

        # add functionality
        self.prompt_name = tkinter.Label(self.body_frame, text='Name to add: ')
        self.add_name = tkinter.Entry(self.body_frame, width=10)
        self.prompt_date = tkinter.Label(self.body_frame, text='Date to add: ')
        self.add_date = tkinter.Entry(self.body_frame, width=10)
        self.add_button = tkinter.Button(self.body_frame, text='ADD', command=self.delete())
        self.prompt_name.pack(side='left')
        self.add_name.pack(side='left')
        self.prompt_date.pack(side='left')
        self.add_date.pack(side='left')
        self.add_button.pack(side='left')

        # delete functionality
        self.prompt_removal_name = tkinter.Label(self.lower_frame, text='Name to remove: ')
        self.remove_name = tkinter.Entry(self.lower_frame, width=10)
        self.prompt_removal_date = tkinter.Label(self.lower_frame, text='Date to remove: ')
        self.remove_date = tkinter.Entry(self.lower_frame, width=10)
        self.remove_button = tkinter.Button(self.lower_frame, text='REMOVE', command=self.display_prompt())
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
        pass

    def display_prompt(self):
        pass

    def delete(self):
        pass


run_gui = ConnectionManagerGUI()