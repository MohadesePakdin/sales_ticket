# this library is for read and write csv file
import csv
# this library is for submit logging
import logging
# this library is for read dataframe file
import pandas as pd
# this is parent of user
from person import Person

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s %(message)s", filename='mhp.log',
                    level=logging.DEBUG, filemode='a', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger('LOG')


class User(Person):
    def __init__(self, status, username=None, password=None):
        """
        this class is for create a user
        status: status of user
        username: username
        password: password
        """
        super().__init__(status)
        self.username = username
        self.password = password
        self.status = status

    def show_event(self):
        """
        this method show all of event for user
        return: a dataframe
        """
        try:

            df = pd.read_csv("event.csv")
            df_2 = df[
                       ["Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                        "Mod_total_capacity", "Flag_event"]].loc[1:, :]
            df_2["Cost_event"] = df_2["Cost_event"].astype(int)
            df_2["Mod_total_capacity"] = df_2["Mod_total_capacity"].astype(int)
            df_2["Flag_event"] = df_2["Flag_event"].astype(int)
            pd.set_option('display.max_columns', None)
            df_active_event = df_2.loc[df_2['Flag_event'] == 1]
            pd.set_option('display.max_columns', None)
            print(df_active_event)


        except Exception:
            logging.exception('this is file error')

    def show_details_event(self, index_event):
        """
        this method show details of event for user
        param index_event: index of selection event
        return: a dataframe
        """
        try:
            pd.set_option('display.max_columns', None)
            df_first = pd.read_csv("event.csv")
            df_first_2 = df_first[
                             ["Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                              "Mod_total_capacity", ]].loc[1:, :]
            df_first_3 = df_first_2.loc[[index_event]]
            df_first_3["Cost_event"] = df_first_3["Cost_event"].astype(int)
            df_first_3["Mod_total_capacity"] = df_first_3["Mod_total_capacity"].astype(int)
            df_first_3["Total_capacity"] = df_first_3["Total_capacity"].astype(int)
            print(df_first_3.loc[[index_event]])

        except Exception:
            logging.exception('this is file error')

    @staticmethod
    def choose_event(event_choice):
        """
        this method id for select an item
        :return: index of row
        """
        try:
            with open("event.csv", 'r') as my_file:
                reader = csv.reader(my_file)
                rows = list(reader)
                print("your select ", int(rows[event_choice][0]), "event")
        except FileNotFoundError:
            logging.exception("could\'t find event file")

    @staticmethod
    def create_account():
        file_path = "account.csv"
        try:
            df_account = pd.read_csv(file_path)
            df_account_indexed = df_account.set_index("id_account", drop=True)
            list_username = list(df_account_indexed["username"])
            while True:
                username_account = input("input your username: ")
                if username_account not in list_username[1:]:
                    print("Your username is created then submit your password . ")
                    break
                else:
                    print("Your name has already been entered with this username TRY ANOTHER ONE . ")
            password_account = input("Please input password: ")
            print("Please select one of follow choice:")
            print("You are logging in as : \n1-STUDENT \n2-EMPLOYEE \n3-TEACHER \n4-OTHER")
            while True:
                # USER HAS TO INPUT ONE OF THEM
                try:
                    input_user_type = int(input("1 or 2 or 3: "))
                    if input_user_type in [1, 2, 3, 4]:
                        if input_user_type == 1:
                            type_account = "Student"
                            percent = 15
                            break
                        elif input_user_type == 2:
                            type_account = "Employee"
                            percent = 10
                            break
                        elif input_user_type == 3:
                            type_account = "Teacher"
                            percent = 12
                            break
                        elif input_user_type == 4:
                            type_account = "Other"
                            percent = 0
                            break
                    else:
                        print("Your input is INVALID please try again. ")
                except Exception:
                    print("Your input is INVALID please try again. ")
            row_account = [
                [df_account_indexed.index[-1] + 1, username_account, str(password_account), type_account, percent, 1]]

            with open(file_path, 'a', newline='') as csv_account:
                csv_writer = csv.writer(csv_account)
                # writing the data row
                csv_writer.writerows(row_account)
        except Exception:
            print("you have not this file please create a file with name account.csv and set first row with this items "
                  "(id_account,username,password,flag)and second row with this item (0,) without parenthesis")
            logging.exception('not completely header in file')

    @staticmethod
    def buy_ticket(user_choice, user_id):

        """
        this method select a vent for sale
        param user_choice: user select a event and buy it
        return: if sale is successully return True else return False
        """
        df_event = pd.read_csv("event.csv")
        df_sales=pd.read_csv("sales.csv")
        df_sales_indexed=df_sales.set_index("id_sales", drop=True)
        df_account = pd.read_csv("account.csv")
        df_discount = pd.read_csv("discount.csv")
        event_cap = df_event.values.tolist()[user_choice - 1][7]
        job_person_percent = df_account.values.tolist()[user_id][4]
        list_off = df_discount['name_discount'].to_list()
        while True:
            try:
                number_of_ticket = int(input("how many tickets do you want? "))
                if number_of_ticket > event_cap:
                    print("this event dont have capacity")
                else:
                    initial_cost = number_of_ticket * df_event.values.tolist()[user_choice - 1][5]
                    event_cost = initial_cost - (initial_cost * (job_person_percent / 100))
                    discount = input("do you have discount:(please enter it or enter ENTER KEY: ")
                    if discount == "":
                        print("total paid= {} ".format(event_cost))
                        print("_______________shaparak_______________")
                        cap = df_event.at[user_choice, 'Mod_total_capacity'] - number_of_ticket
                        df_event.loc[df_event["id_event"] == user_choice, "Mod_total_capacity"] = cap
                        df_event.to_csv("event.csv", index=False)
                        row = [[df_sales_indexed.index[-1] + 1, user_id, user_choice]]
                        with open("sales.csv", 'a', newline='') as csv_events:
                            # creating a csv writer object
                            csv_writer = csv.writer(csv_events)
                            # writing the data row
                            csv_writer.writerows(row)
                        logger.info("we check code from discount file .")
                        break
                    else:
                        if discount in list_off:
                            darsad_discount = df_discount.iloc[list_off.index(discount)]["darsad"]
                            total_off = event_cost - (event_cost * (darsad_discount / 100))
                            if event_cost <= 0:
                                print("this event is free")
                                cap = df_event.at[user_choice, 'Mod_total_capacity'] - number_of_ticket
                                df_event.loc[df_event["id_event"] == user_choice, "Mod_total_capacity"] = cap
                                df_event.to_csv("event.csv", index=False)
                                row = [[df_sales_indexed.index[-1] + 1,user_id,user_choice]]
                                with open("sales.csv", 'a', newline='') as csv_events:
                                    # creating a csv writer object
                                    csv_writer = csv.writer(csv_events)
                                    # writing the data row
                                    csv_writer.writerows(row)
                                logger.info("we check code from discount file .")
                            else:
                                print("total paid= {} ".format(total_off))
                                print("_______________shaparak_______________")
                            cap = df_event.at[user_choice, 'Mod_total_capacity'] - number_of_ticket
                            df_event.loc[df_event["id_event"] == user_choice, "Mod_total_capacity"] = cap
                            df_event.to_csv("event.csv", index=False)
                            row = [[df_sales_indexed.index[-1] + 1, user_id, user_choice]]
                            with open("sales.csv", 'a', newline='') as csv_events:
                                # creating a csv writer object
                                csv_writer = csv.writer(csv_events)
                                # writing the data row
                                csv_writer.writerows(row)
                            logger.info("we check code from discount file .")
                            break
            except ValueError:
                print("your input is not valid please enter correct event. ")

