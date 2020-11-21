import csv
import logging
import pandas as pd
from person import Person

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s %(message)s", filename='mhp.log',
                    level=logging.DEBUG, filemode='a', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger('LOG')


class User(Person):
    def __init__(self, status):
        super().__init__(status)

    def show_event(self):

        try:

            df_first = pd.read_csv("event.csv")
            df_first_2 = df_first[
                             ["Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                              "Mod_total_capacity"]].loc[1:, :]
            df_first_2["Cost_event"] = df_first_2["Cost_event"].astype(int)
            df_first_2["Mod_total_capacity"] = df_first_2["Mod_total_capacity"].astype(int)
            pd.set_option('display.max_columns', None)
            print(df_first_2)


        except Exception:
            logging.exception('this is file error')

    def show_details_event(self, index_event):  # in show_event methods we can not see some of details
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
        this method choose one of the events
        """
        try:
            with open("event.csv", 'r') as my_file:
                reader = csv.reader(my_file)
                rows = list(reader)
                print("your selection is :", int(rows[event_choice][0]) + 1)
        except FileNotFoundError:
            logging.exception('couldnt find event file')

    def create_account(self):
        """
         if user didnt have account she/he can create an account
        """
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

    def buy_ticket(self, user_choice):
        """
        user choose one event to buy ticket for that
        """
        try:
            many_of_ticket = int(input("how many tickets do you want ?"))
            df_event = pd.read_csv("event.csv")
            df_event_2 = df_event[
                             ["id_event", "Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                              "Total_capacity", "Mod_total_capacity", "Flag_event"]].loc[1:, :]
            cost = df_event_2.iloc[user_choice]["Cost_event"]
            mod_capacity = df_event_2.iloc[user_choice]["Mod_total_capacity"]

            df_first_account = pd.read_csv("account.csv")
            df_first_3 = df_first_account[
                             ["id_account", "username", "password", "type_account", "percent", "flag"]].loc[1:, :]
            job_percent = df_first_3.iloc[user_choice]["percent"]

            df_first_discount = pd.read_csv("discount.csv")
            df_first_4 = df_first_discount[
                             ["id_discount", "name_discount", "darsad"]].loc[1:, :]
            discount_persent = df_first_4.iloc[user_choice]["darsad"]
            name_of_discount = df_first_4.iloc[user_choice]["name_discount"]

            if mod_capacity > 1:
                price_of_event = many_of_ticket * cost
                logger.info("we give percent of jobs from account file .")
                print("your total payment is : ", price_of_event - (job_percent / 100) * price_of_event)

                input_user_off_code = input("Do you have any off code ? (if yes please input it): ")
                if input_user_off_code == 'no':
                    input_user_want_to_buy_or_not = input("Paying")
                    print("-----------------shaparak------------------")
                    cap = df_event.loc[df_event["id_event"] == user_choice, "Flag_event"]
                    df_event.loc[df_event["id_event"] == user_choice, "Flag_event"] = cap - many_of_ticket
                    # Write object to a (csv) file
                    df_event.to_csv("event.csv", index=False)
                    mod_capacity = df_event_2.iloc[user_choice]["Mod_total_capacity"]

                else :
                    if job_percent + discount_persent >= 100:
                        print("raygan")
                    else :
                        logger.info("we check code from discount file .")
                        print("your total payment is : ", price_of_event - ((job_percent / 100) * price_of_event + (
                                    discount_persent/100) * price_of_event))

                        logger.info("if user wants to buy ticket we will call shaparak .")
                        print("-----------------shaparak-------------------")
                        cop = df_event_2.iloc[user_choice]["Mod_total_capacity"]
                        df_event_2.iloc[user_choice]["Mod_total_capacity"] = cop - many_of_ticket

            else:
                print("this event dont have capacity ")
        except ValueError:
            print("INVALID input.")
        except KeyError:
            logger.error("Not found in index .")

    @classmethod
    def menu_user(self):
        print("1-show events \n2-choose event \n3-create account \n4-log in \n")

obi = User('k')
obi.buy_ticket(2)
