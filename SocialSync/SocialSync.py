from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import *
import ttkbootstrap as tb
import time
from Page_Manager import Book

from CSV_interactions import *

width, height = 720, 480


class SocialSync:
    def __init__(self):
        self.screen = tb.Window(title='SocialSync', size=[width, height], resizable=[False, False], themename='superhero')
        self.name_list = ScrolledFrame(self.screen, width=width, height=height)
        self.current_widget = []
        self.sorted_names = {}
        self.sort_type = StringVar()
        self.sort_type.set('Name Ascending')
        self.visible_lines = []
        self.page_label = ''
        self.book = Book()
        self.name_sort()

    # clear all widgets from the screen
    def clear_screen(self):
        if self.name_list.winfo_exists():
            self.name_list.container.destroy()
        for button in self.current_widget:
            button.destroy()
        self.current_widget.clear()

    # Create the main menu
    def menu_screen(self, start_time, term=''):
        self.clear_screen()
        self.book.empty()
        entries = 0

        # create a frame for all the menu option at the top of the screen
        menu_frame = Frame(self.screen, width=width)
        menu_frame.pack(fill=X, pady=10, padx=10)
        self.current_widget.append(menu_frame)

        # create a scroll frame for all the connections
        self.name_list = ScrolledFrame(self.screen, width=width, height=height-125)
        self.name_list.pack()
        self.current_widget.append(self.name_list)

        # set up frame for page control
        page_frame = Frame(self.screen, width=width)
        page_frame.pack(fill=X, pady=10, padx=10)
        self.current_widget.append(page_frame)

        # Search bar and button
        search_entry = tb.Entry(menu_frame, bootstyle='Primary')
        search_entry.pack(side=LEFT)
        self.current_widget.append(search_entry)
        search_button = tb.Button(menu_frame, text='Search', command=lambda : self.menu_screen(time.time(), search_entry.get()))
        search_button.pack(side=LEFT)
        self.current_widget.append(search_button)

        # Sort menu
        sort_menu_button = tb.Menubutton(menu_frame, text='Filter')
        sort_menu_button.pack(side=LEFT, padx=10)
        self.current_widget.append(sort_menu_button)
        sort_menu = tb.Menu(sort_menu_button)
        sort_menu.add_radiobutton(label='Name Ascending', variable=self.sort_type, command=self.name_sort)
        sort_menu.add_radiobutton(label='Name Descending', variable=self.sort_type, command=lambda: self.name_sort(True))
        sort_menu.add_radiobutton(label='Date Ascending', variable=self.sort_type, command=self.date_sort)
        sort_menu.add_radiobutton(label='Date Descending', variable=self.sort_type, command=lambda: self.date_sort(True))
        sort_menu_button['menu'] = sort_menu

        # Button to the add connections menu
        add_button = tb.Button(menu_frame, text="add connections", command=self.add_screen)
        add_button.pack(side=LEFT)
        self.current_widget.append(add_button)

        # set up column headers
        line_frame = tb.Frame(self.name_list)
        line_frame.pack()
        self.current_widget.append(line_frame)
        name_frame = tb.Frame(line_frame)
        name_frame.pack(side=LEFT)
        date_frame = tb.Frame(line_frame)
        date_frame.pack(side=LEFT)
        button_frame = tb.Frame(line_frame, width=120, height=50)
        button_frame.pack(side=LEFT)
        self.current_widget.append(name_frame)
        name_label = tb.Label(name_frame, text='Connection Name', width=25, bootstyle='superhero', font=('Helvetica', 12, 'underline'))
        name_label.pack(side=LEFT)
        self.current_widget.append(name_label)
        date_label = tb.Label(date_frame, text='Connection Date', width=25, bootstyle='superhero', font=('Helvetica', 12, 'underline'))
        date_label.pack(side=LEFT)
        self.current_widget.append(date_label)

        # Display names and dates
        for name, date in self.sorted_names:
            if term.lower() in name.lower():
                line_frame = tb.Frame(self.name_list)
                # line_frame.pack()
                self.current_widget.append(line_frame)
                name_frame = tb.Frame(line_frame)
                name_frame.pack(side=LEFT)
                date_frame = tb.Frame(line_frame)
                date_frame.pack(side=LEFT)
                button_frame = tb.Frame(line_frame)
                button_frame.pack(side=LEFT)
                self.current_widget.append(name_frame)
                name_label = tb.Label(name_frame, text=name, width=25, bootstyle='inverse dark', font=('Helvetica', 12))
                name_label.pack(side=LEFT)
                self.current_widget.append(name_label)
                date_label = tb.Label(date_frame, text=date, width=25, bootstyle='inverse dark', font=('Helvetica', 12))
                date_label.pack(side=LEFT)
                self.current_widget.append(date_label)

                # modify connection buttons for each connection
                modify_button = tb.Button(button_frame, text='Modify', bootstyle='superhero',
                                          command=lambda n=name, d=date: self.modify_screen(n, d))
                modify_button.pack(side=LEFT)
                self.current_widget.append(modify_button)

                # delete buttons for each connection
                delete_button = tb.Button(button_frame, text='Delete', bootstyle='danger',
                                          command=lambda n=name: self.remove_connection(n))
                delete_button.pack(side=LEFT)
                self.current_widget.append(delete_button)

                self.book.add(line_frame)

                entries += 1

        for line in self.book.get_page():
            line.pack()
            self.visible_lines.append(line)

        # next button
        next_button = tb.Button(page_frame, text="Next", command=lambda: self.next_page())
        next_button.pack(side=RIGHT)
        self.current_widget.append(next_button)

        # Page counter
        self.page_label = tb.Label(page_frame, text=str(self.book.current_page + 1) + ' / ' + str(self.book.book_len() + 1))
        self.page_label.pack(side=RIGHT)
        self.current_widget.append(self.page_label)

        # back button
        back_button = tb.Button(page_frame, text="Back", command=lambda: self.previous_page())
        back_button.pack(side=RIGHT)
        self.current_widget.append(back_button)

        # calculate and display time it took to sort and display information
        end_time = time.time()
        sort_time = end_time - start_time
        time_label = tb.Label(menu_frame, text=str(entries) + ' connections found in ' + "%.2f" % sort_time + ' seconds')
        time_label.pack(side=LEFT)
        self.current_widget.append(time_label)

    def next_page(self):
        if self.book.current_page != self.book.book_len():
            self.book.next_page()
            for line in self.visible_lines:
                line.pack_forget()
            self.visible_lines = []
            for line in self.book.get_page():
                line.pack()
                self.visible_lines.append(line)
            self.page_label.config(text=str(self.book.current_page + 1) + ' / ' + str(self.book.book_len() + 1))

    def previous_page(self):
        if self.book.current_page != 0:
            self.book.previous_page()
            for line in self.visible_lines:
                line.pack_forget()
            self.visible_lines = []
            for line in self.book.get_page():
                line.pack()
                self.visible_lines.append(line)
            self.page_label.config(text=str(self.book.current_page + 1) + ' / ' + str(self.book.book_len() + 1))

    # sort all connections by name
    def name_sort(self, inverse=False):
        start_time = time.time()
        self.sorted_names = {}
        pull_connections()
        for name, date in connection_map.items():
            self.sorted_names[name] = date
        self.sorted_names = sorted(self.sorted_names.items(), reverse=inverse)
        self.menu_screen(start_time)

    # sort all connections by date
    def date_sort(self, inverse=False):
        start_time = time.time()
        self.sorted_names = {}
        pull_connections()
        for name, date in connection_map.items():
            self.sorted_names[name] = date
        self.sorted_names = sorted(self.sorted_names.items(), key=lambda x:x[1], reverse=inverse)
        self.menu_screen(start_time)

    # go to the menu for adding new connections
    def add_screen(self):
        self.clear_screen()

        # create the frame for all menu options
        menu_frame = Frame(self.screen, width=width)
        menu_frame.pack(fill=X)
        self.current_widget.append(menu_frame)

        # create the menu options
        menu_button = tb.Button(menu_frame, text="Back To Menu", command=self.name_sort)
        menu_button.pack(side=LEFT)
        self.current_widget.append(menu_button)

        # labels and entry boxes for the first and last names
        first_label = tb.LabelFrame(self.screen, text='* First Name')
        first_label.pack(pady=20)
        self.current_widget.append(first_label)
        first_entry = tb.Entry(first_label)
        first_entry.pack()
        self.current_widget.append(first_entry)
        last_label = tb.LabelFrame(self.screen, text='* Last Name')
        last_label.pack(pady=20)
        self.current_widget.append(last_label)
        last_entry = tb.Entry(last_label)
        last_entry.pack()
        self.current_widget.append(last_entry)

        # create the date entry calendar
        date_label = tb.LabelFrame(self.screen, text='* Date')
        date_label.pack(pady=20)
        self.current_widget.append(date_label)
        date_entry = tb.DateEntry(date_label, dateformat="%Y-%m-%d")
        date_entry.pack()
        self.current_widget.append(date_entry)

        # button to confirm
        confirm_button = tb.Button(self.screen, text="Confirm", command=lambda: self.add_connection(first_entry.get(), last_entry.get(), date_entry.entry.get()))
        confirm_button.pack()
        self.current_widget.append(confirm_button)

    # Add the name and date to the hash map then push it to the CSV
    def add_connection(self, first, last, date):
        change = True
        for n, d in connection_map.items():
            if (first + ' ' + last).lower() == n.lower():
                error_message = Messagebox.yesno(message='A connection with the name ' + n + ' already exist, would you like to override it',
                                                 title='Override Connection', alert=True)

                if error_message == 'No':
                    return

        # error message for missing part of name
        if first == '' or last == '':
            error_message = MessageDialog(message='Invalid First or Last Name', title='Invalid Name', buttons=['OK:superhero'], alert=True)
            error_message.show()
            self.current_widget.append(error_message)

        # Update connection map with new connection
        if change:
            connection_map[first + ' ' + last] = date
            push_connections()
            self.name_sort()

    # update the connection date
    def modify_screen(self, name, date):
        self.clear_screen()

        # create the frame for all menu options
        menu_frame = Frame(self.screen, width=width)
        menu_frame.pack(fill=X)
        self.current_widget.append(menu_frame)

        # create the menu options
        menu_button = tb.Button(menu_frame, text="Back To Menu", command=self.name_sort)
        menu_button.pack(side=LEFT)
        self.current_widget.append(menu_button)

        # Display current connection information
        current_name = tb.Label(text='Current Name: ' + name, font=('Helvetica', 12))
        current_name.pack(pady=20)
        self.current_widget.append(current_name)
        current_date = tb.Label(text='Current Date: ' + date, font=('Helvetica', 12))
        current_date.pack(pady=20)
        self.current_widget.append(current_date)

        # create the date entry calendar for new date
        date_label = tb.LabelFrame(self.screen, text='Select New Date')
        date_label.pack(pady=20)
        self.current_widget.append(date_label)
        date_entry = tb.DateEntry(date_label, dateformat="%Y-%m-%d")
        date_entry.pack()
        self.current_widget.append(date_entry)

        # Button to confirm the change
        confirm_button = tb.Button(self.screen, text="Confirm", command=lambda: self.modify(name, date_entry.entry.get()))
        confirm_button.pack()
        self.current_widget.append(confirm_button)

    def modify(self, name, date):
        connection_map[name] = date
        push_connections()
        self.name_sort()

    # remove the selected connection
    def remove_connection(self, name):
        # message box to verify they want to remove their connection
        error_message = Messagebox.yesno(message='Are You Sure You Want To Remove The Connection for \n' + name, title='Remove Connection')
        if error_message == 'Yes':
            del connection_map[name]
            push_connections()
            self.name_sort()

    # getter for the screen
    def get_screen(self):
        return self.screen


SocialSync().get_screen().mainloop()
