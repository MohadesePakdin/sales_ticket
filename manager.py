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
import logging
# #creat and configure logger
logger = logging.getLogger()

class Admin(Person):
    def __init__(self, status, username=None, password=None, flag=1):
        super().__init__(status, username, password, flag)
        self.username = username
        self.password = password
        self.flag = flag


    def signup(self):
        file_path = "account.csv"# admin.csv
        try:
            df= pd.read_csv(file_path)
            df_indexed = df.set_index("id_account", drop=True)# id_admin
            # df_account = pd.read_csv("account.csv")
            # df_account_indexed = df_account.set_index("id_account", drop=True)
            list_username = list(df_indexed["username"])
            while True:
                username_account = input("input your username: ")
                if username_account not in list_username[1:]:
                    print("Your username is created then submit your password . ")
                    break
                else:
                    print("Your name has already been entered with this username TRY ANOTHER ONE . ")
            # username_account = input("Please input username: ")
            password_account = input("Please input password: ")
            # print("Please select one of follow choice:")
            # print("You are logging in as : \n1-STUDENT \n2-EMPLOYEE \n3-TEACHER \n4-OTHER")
            # in future we want
            # while True:
            #     input_user_type = input("1 or 2 or 3: ")
            #     try:
            #         input_user_type_int=int(input_user_type)
            #         if input_user_type_int in [1, 2, 3, 4]:
            #             if input_user_type_int == 1:
            #                 type_account = "Student"
            #                 break
            #             elif input_user_type_int == 2:
            #                 type_account = "Employee"
            #                 break
            #             elif input_user_type_int == 3:
            #                 type_account = "Teacher"
            #                 break
            #             elif input_user_type_int == 4:
            #                 type_account = "Other"
            #                 break
            #         else:
            #             print("Your input is INVALID please try again. ")
            #
            #     except ValueError:
            #         print("Your input is INVALID please try again. ")
            # row_account = [[df_indexed.index[-1] + 1, username_account, str(password_account), type_account, 1]]

            # with open(file_path, 'a', newline='') as csv_account:
            #     csv_writer = csv.writer(csv_account)
            #     # writing the data row
            #     csv_writer.writerows(row_account)
        except Exception:
            print("you have not this file please create a file with name account.csv and set first row with this items "
                  "(id_account,username,password,flag)and second row with this item (0,) without parenthesis")
            # logging.exception('not completely header in file')

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
                    logger.error("not valid")
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
        #Which event do you want to delete
        id_remove=int(input("please enter row for delete: "))

        while True:
            try:
                #read csv file
                df_first = pd.read_csv("event.csv")
                #access  a specific few rows/columns from DataFrame
                df_first.loc[df_first["id_event"]==id_remove,"Flag_event"]=0
                #Write object to a (csv) file
                df_first.to_csv("event.csv", index=False)
                logger.info("event %s is removed." % id_remove)

            except EOFError:
                # raised when a built-in function  do not read any data before encountering
                print("File is empty. You must add a event first before you can remove it.")
                logger.error("File is empty")
            except KeyError:
                #raised when you try to access a key that dose not exist
                print("That event doesn't exist.")
                logger.error("doesn't exist")

            df = pd.read_csv(r"event.csv")
            print(df)
            #Do you want to continue deleting or not
            keepLooping = input("\nAnother evet to delete? y/n: ")
            if keepLooping == "n":
                break



    def add_discount(self):
        # we have a csv file at first and csv file have 2 static record
        # load csv file
        file_name = "discount.csv"
        # exception handling
        try:
            df_discount = pd.read_csv(file_name)
            # set id_event for index in csv file
            df_discount_indexed = df_discount.set_index("id_discount", drop=True)
            # get info of discount
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
            logger.error("file not fount")


    def active_evevnt(self):
        #Show current events
        #open csv file
        with open("event.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            #In this loop we want to display events whose flag is 1
            for lines in csv_reader:
                obj_event = Event(lines['id_event'], lines['Name_event'],lines['Date_event'],lines['Time_event'],
                    lines['place_event'],lines['Cost_event'],lines['Total_capacity'],lines['Mod_total_capacity'],
                    lines['Flag_event'])
                if obj_event.flag_event == 1:
                    print(obj_event)


    def deactive_event(self):
        #
        # open csv file
        with open("event.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            # In this loop we want to display events whose flag is 1
            for lines in csv_reader:
                obj_event = Event(lines['id_event'], lines['Name_event'], lines['Date_event'], lines['Time_event'],
                                  lines['place_event'], lines['Cost_event'], lines['Total_capacity'],
                                  lines['Mod_total_capacity'],
                                  lines['Flag_event'])
                if obj_event.flag_event == 0:
                    print(obj_event)


obj_user = Admin()
a = obj_user.remove_event()
