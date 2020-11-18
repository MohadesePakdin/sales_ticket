# this library is for work by csv file
import csv
# this library is for import correct date and time to csv file
# from event import Event
from datetime import datetime

# this library is read a csv file in dataframe format
import pandas as pd
# use this library for colored code
from termcolor import colored

from event import Event


class Admin:
    def __init__(self, username, password,flag=1):
        self.username = username
        self.password = password
        self.flag = flag
    def login(self):
        number_try = 3
        while number_try > 0:  # baraye inke agar eshtebah vared kard dobare azash bkhad ke user pass bzne ya inke bre biron
            print("input your username and password")
            username = input("please enter your username: ")
            password = input("please enter your password: ")
            df_admin = pd.read_csv("admin.csv")
            df_admin_indexed = df_admin.set_index("id_admin", drop=True)
            try:
                if str(df_admin_indexed.iloc[
                           df_admin_indexed.index[df_admin_indexed['username'] == username].tolist()[
                               0] - 1, 1]) == password:
                    # obj_admin = Admin()
                    while True:
                        print("please select one of follow choices:\n")
                        print("1-show all active event \n"
                              "2-show all event \n"
                              "3-show all deactivate event\n"
                              "4-create event \n"
                              "4-remove event \n"
                              "5-Exit ")
                        try:
                            admin_input_selected = int(input("enter your choice: "))
                            if admin_input_selected in range(1, 6):
                                if admin_input_selected == 1:
                                    print("show_all_active_event()")
                                    Admin.show_event(Admin, 5)
                                    # obj_admin.show_all_active_event()
                                elif admin_input_selected == 2:
                                    print("show_all_event()")
                                    # obj_admin.show_all_event()
                                elif admin_input_selected == 3:
                                    print("show_all_deactive_event()")
                                    # obj_admin.show_all_deactive_event()
                                elif admin_input_selected == 4:
                                    print("create_event()")
                                    # obj_admin.create_event()
                                elif admin_input_selected == 5:
                                    print("exit()")
                                    sys.exit()
                            else:
                                print("your input is not valid please select other choice")
                        except ValueError:
                            print("your input is not valid please select other choice")
                    break
            except IndexError:
                if number_try > 1:
                    print("your username or password is wrong please try again")
                    number_try -= 1
                else:
                    print("your username or password is wrong")
                    number_try -= 1
        else:
            input("\n\nyou try upper than 3 times your account block print any key to exit: ")
            sys.exit()

    def signup(self):
        pass

    def add_event(self):
        # we have a csv file at first and csv file have 2 static record that dont delete this first row is my attribute
        # and second row is set first id and add them in future record
        # load csv file
        file_name = "event.csv"
        # exception handling
        try:
            df_events = pd.read_csv(file_name)
            # set id_event for index in csv file
            df_events_indexed = df_events.set_index("id_event", drop=True)
            # get info of one event from admin and add to csv file
            name_event = input("Enter title of event: ")
            # this while is for that we input correct answer to dataset
            while True:
                try:
                    date_event = str(datetime.strptime(input('Enter date of event with this format 1399/08/26 : '),
                                                       "%Y/%m/%d")).split()[0]
                    break
                except ValueError:
                    print("your date event is not valid please input with this format: 1399/08/26")
            while True:
                try:
                    time_event = str(datetime.strptime(input('Enter time of event with this format 20:00 : '),
                                                       "%H:%M")).split()[1]
                    break
                except ValueError:
                    print("your time event is not valid please input with this format", colored("20:00", "red"))
            place_event = input("Enter place of event: ")
            cost_event = input("Enter cost of event in Rial: ")
            total_capacity, mod_total_capacity = input("Enter total capacity of event: ")
            obj_event = Event(df_events_indexed.index[-1] + 1, name_event, date_event, time_event, place_event,
                              cost_event, total_capacity, mod_total_capacity, 1)
        # if file not fount
        except FileNotFoundError:
            print("you have not this file please create a file with name event.csv and set first "
                  "row with this items (id_event,Name_event,Date_event,Time_event,"
                  "place_event,Cost_event,Total_capacity,Mod_total_capacity,Flag_event)"
                  "and second row with this item (0,) without parenthesis ")
        obj_event.create_event()
