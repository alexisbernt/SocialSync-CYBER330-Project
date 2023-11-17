import tkinter
from tkinter import Tk, Button
from tkinter import ttk  # importing the ttk module for combobox (dropdown)
class ConnectionManagerGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.upper_frame = tkinter.Frame(self.main_window, width=800, height=600)
        self.body_frame = tkinter.Frame(self.main_window, width=800, height=600)
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

        # add functionality
        self.prompt_label_add = tkinter.Label(self.upper_frame, text='ADD: ')
        self.prompt_label_add.pack()
        self.prompt_name = tkinter.Label(self.body_frame, text='Name: ')
        self.add_name = tkinter.Entry(self.body_frame, width=10)
        self.prompt_date = tkinter.Label(self.body_frame, text='Date: ')
        self.add_date = tkinter.Entry(self.body_frame, width=10)
        self.prompt_name.pack(side='left')
        self.add_name.pack(side='left')
        self.prompt_date.pack(side='left')
        self.add_date.pack(side='left')

        # delete functionality
        self.prompt_label_remove = tkinter.Label(self.body_frame, text='REMOVE: ')
        self.prompt_label_remove.pack()
        self.prompt_removal_name = tkinter.Label(self.lower_frame, text='Name: ')
        self.remove_name = tkinter.Entry(self.lower_frame, width=10)
        self.prompt_removal_date = tkinter.Label(self.lower_frame, text='Date: ')
        self.remove_date = tkinter.Entry(self.lower_frame, width=10)
        self.prompt_removal_name.pack(side='left')
        self.remove_name.pack(side='left')
        self.prompt_removal_date.pack(side='left')
        self.remove_date.pack(side='left')

        # pack frames
        self.upper_frame.pack()
        self.body_frame.pack()
        self.lower_frame.pack()

        tkinter.mainloop()

    def get_sorted_data(self):
        pass


run_gui = ConnectionManagerGUI()