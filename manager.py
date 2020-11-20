# this library is for work by csv file
import csv
# this library is for import correct date and time to csv file
# from event import Event
from datetime import datetime

# this library is read a csv file in dataframe format
import pandas as pd
# use this library for colored code

from termcolor import colored

from discount import Discount
from event import Event
import pandas as pd
from termcolor import colored

from person import Person


class Admin(Person):
    def __init__(self, status, username=None, password=None, flag=1):
        super().__init__(status, username, password, flag)
        self.username = username
        self.password = password
        self.flag = flag


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




    def remove_event(self, df_first=None):
        id_remove=int(input("please enter row for delete: "))

        while True:
            try:

                df_first = pd.read_csv("event.csv")
                df_first.loc[df_first["id_event"]==id_remove,"Flag_event"]=0
                df_first.to_csv("event.csv", index=False)

            except EOFError:
                print("File is empty. You must add a film first before you can remove it.")

            except KeyError:
                print("That event doesn't exist.")

            df = pd.read_csv(r"event.csv")
            print(df)



            keepLooping = input("\nAnother evet to delete? y/n: ")
            if keepLooping == "n":
                break



    def add_discount(self):
        # we have a csv file at first and csv file have 2 static record that dont delete this first row is my attribute
        # and second row is set first id and add them in future record
        # load csv file
        file_name = "discount.csv"
        # exception handling
        try:
            df_discount = pd.read_csv(file_name)
            # set id_event for index in csv file
            df_discount_indexed = df_discount.set_index("id_discount", drop=True)
            # get info of one event from admin and add to csv file
            name_discount = input("Enter name of discount: ")
            # this while is for that we input correct answer to dataset


            darsad= input("Enter darsad of discount: ")

            obj_discount = Discount(df_discount_indexed.index[-1] + 1, name_discount, darsad)
        # if file not fount
        except FileNotFoundError:
            print("you have not this file please create a file with name event.csv and set first "
                  "row with this items (id_event,Name_event,Date_event,Time_event,"
                  "place_event,Cost_event,Total_capacity,Mod_total_capacity,Flag_event)"
                  "and second row with this item (0,) without parenthesis ")


    def active_evevnt(self):
        with open("event.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for lines in csv_reader:
                print(lines['id_event'], lines['Name_event'],lines['Date_event'],lines['Time_event'],
                      lines['place_event'],lines['Cost_event'],lines['Total_capacity'],lines['Mod_total_capacity'],
                      lines['Flag_event']==1)

    def deactive_event(self):
        with open("event.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for lines in csv_reader:
                print(lines['id_event'], lines['Name_event'], lines['Date_event'], lines['Time_event'],
                      lines['place_event'], lines['Cost_event'], lines['Total_capacity'], lines['Mod_total_capacity'],
                      lines['Flag_event'] == 0)


obj_user = Admin()
a = obj_user.remove_event()
