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

from colorlog.colorlog import ColoredFormatter


# #creat and configure logger
logger = logging.getLogger()


class Admin(Person):
    def __init__(self, status, username=None, password=None, flag=1):
        super().__init__(status, username, password, flag)
        self.username = username
        self.password = password
        self.flag = flag

    @staticmethod
    def register():
        """
        The Method is for the admin to enter the event.

        """
        file_path = "manager.csv"
        try:
            df = pd.read_csv(file_path)
            df_indexed = df.set_index("id_manager", drop=True)  # id_admin
            list_username = list(df_indexed["username"])
            while True:
                username_account = input("input your username: ")
                if username_account not in list_username[1:]:
                    print("Your username is created then submit your password . ")
                    break
                else:
                    print("Your name has already been entered with this username TRY ANOTHER ONE . ")
            password_account = input("Please input password: ")
            row_account = [[df_indexed.index[-1] + 1, username_account, str(password_account), 1]]
            with open(file_path, 'a', newline='') as csv_account:
                csv_writer = csv.writer(csv_account)
                # writing the data row
                csv_writer.writerows(row_account)
                print("your registering is  successful now you can log in")
                logger.info("info:admin could register successfully")
        except Exception:
            print("you have not this file please create a file with name account.csv and set first row with this items "
                  "(id_account,username,password,flag)and second row with this item (0,) without parenthesis")
            logger.error("Exception:file not found")

    def add_event(self):
        """
        This is a method for adding an event by the admin.

        :return: New event in  Data frame
        """
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
                    logger.error("ValueError:not valid")
            while True:
                try:
                    time_event = str(datetime.strptime(input('Enter time of event with this format 20:00 : '),
                                                       "%H:%M")).split()[1]
                    break
                except ValueError:
                    print("your time event is not valid please input with this format", colored("20:00", "red"))
                    logger.error("you didn't follow the roles (format)")
            place_event = input("Enter place of event: ")
            cost_event = input("Enter cost of event in Rial: ")
            total_capacity, mod_total_capacity = input("Enter total capacity of event: ")
            obj_event = Event(df_events_indexed.index[-1] + 1, name_event, date_event, time_event, place_event,
                              cost_event, total_capacity, mod_total_capacity, 1)
            obj_event.create_event()
            print(obj_event.__str__())

        # if file not fount
        except FileNotFoundError:
            print("you have not this file please create a file with name event.csv and set first "
                  "row with this items (id_event,Name_event,Date_event,Time_event,"
                  "place_event,Cost_event,Total_capacity,Mod_total_capacity,Flag_event)"
                  "and second row with this item (0,) without parenthesis ")
            logger.error(" FileNotFoundError:file didn't found")

    def remove_event(self):
        """This method is for the admin to delete the event.


        :return:Data frame
        """
        # Which event do you want to delete
        id_remove = int(input("please enter row for delete: "))

        while True:
            try:
                # read csv file
                df_first = pd.read_csv("event.csv")
                # access  a specific few rows/columns from DataFrame
                df_first.loc[df_first["id_event"] == id_remove, "Flag_event"] = 0
                # Write object to a (csv) file
                df_first.to_csv("event.csv", index=False)
                print("delete successfully")
                break
                logger.info("event %s is removed." % id_remove)
            except EOFError:
                # raised when a built-in function  do not read any data before encountering
                print("File is empty. You must add a event first before you can remove it.")
                logger.error("EOFError:File is empty")
                break
            except KeyError:
                # raised when you try to access a key that dose not exist
                print("That event doesn't exist.")
                logger.error("KeyError: There is no event to delete ")
                break

    def add_discount(self):
        """
        Define types of discounts for the user by the admin

        :return: darsad
        """
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

            darsad = input("Enter darsad of discount: ")

            obj_discount = Discount(df_discount_indexed.index[-1] + 1, name_discount, darsad)
        # if file not fount
        except FileNotFoundError:
            print("you have not this file please create a file with name event.csv and set first "
                  "row with this items (id_event,Name_event,Date_event,Time_event,"
                  "place_event,Cost_event,Total_capacity,Mod_total_capacity,Flag_event)"
                  "and second row with this item (0,) without parenthesis ")
            logger.error("FileNotFoundError: No file found Create it first")

    def deactive_event(self):
        """
        Show active events to admin.

        :returns:Data frame
        """
        df = pd.read_csv("event.csv")
        df_active_event = df.loc[df['Flag_event'] == 0]
        pd.set_option('display.max_columns', None)
        return df_active_event
