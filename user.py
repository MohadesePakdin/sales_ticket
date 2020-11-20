import csv
import logging
import pandas as pd
from person import Person

LOG_FORMAT = "%(levelname)s  %(filename)s %(message)s"
logging.basicConfig(filename='mhp.log', level = logging.DEBUG , filemode='w')
logger = logging.getLogger('LOG')


class User(Person):
    def __init__(self, event_choice, status):
        super().__init__(status)
        self.event_choice = event_choice

    # def show_event(self):
    #
    #     try:
    #
    #         df_first = pd.read_csv("event.csv")
    #         df_first_2 = df_first[
    #                          ["Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
    #                           "Mod_total_capacity"]].loc[1:, :]
    #         df_first_2["Cost_event"] = df_first_2["Cost_event"].astype(int)
    #         df_first_2["Mod_total_capacity"] = df_first_2["Mod_total_capacity"].astype(int)
    #         pd.set_option('display.max_columns', None)
    #         print(df_first_2)
    #
    #
    #     except Exception:
    #         logging.exception('this is file error')

    # def show_details_event(self, index_event):  # in show_event methods we can not see some of details
    #     try:
    #         pd.set_option('display.max_columns', None)
    #         df_first = pd.read_csv("event.csv")
    #         df_first_2 = df_first[
    #                          [ "Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
    #                           "Mod_total_capacity",]].loc[1:, :]
    #         df_first_3 = df_first_2.loc[[index_event]]
    #         df_first_3["Cost_event"] = df_first_3["Cost_event"].astype(int)
    #         df_first_3["Mod_total_capacity"] = df_first_3["Mod_total_capacity"].astype(int)
    #         df_first_3["Total_capacity"] = df_first_3["Total_capacity"].astype(int)
    #         print(df_first_3.loc[[index_event]])
    #
    #     except Exception:
    #         logging.exception('this is file error')

    def choose_event(self):
        # اگر متد قبلی فراخانی شده بود از کاربر بپرسه خروج یا برگشت یا خرید ؟

        # input_user = int(input("your selection : "))
        try:
            with open("event.csv", 'r') as my_file:
                reader = csv.reader(my_file)
                rows = list(reader)
                print("your selection is :", rows[self.event_choice][0])
        except FileNotFoundError:
            logging.exception('couldnt find event file')

    def create_account(self):
        # کاربر اگر قصد خرید داشت یا باید وارد شود یا حساب کاربری بسازد
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
                            print("enter your id student: ")
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
        try :
            print("how many tickets do you want ? ")
            many_of_ticket = int(input())
            df_account = pd.read_csv("event.csv")
            df_account_indexed = df_account.set_index("id_event", drop=True)
            prices = [price for price in df_account]
            logger.info("we give price of events from price column in event file .")
            price_of_event = prices[user_choice][5]
            price_of_event = many_of_ticket * price_of_event
            df_account2 = pd.read_csv("account.csv")
            df_account_indexed = df_account.set_index("id_account", drop=True)
            logger.info("we give percent of jobs from account file .")
            darsaad = [darsad for darsad in df_account2]
            percent_of_job = darsaad[user_choice][4]
            print("your total payment is : ", price_of_event - (1 / percent_of_job) * price_of_event)
            print("Do you have any off code ? (if yes please input it ) ")
            number_try = 3
            while number_try > 0:
                input_user_off_code = input()
                if input_user_off_code == 'no':
                    print("Do you want to continue paying ? y/n ")
                    input_user_want_to_buy_or_not = input()
                    if input_user_want_to_buy_or_not == 'y':
                        print("-----------------shaparak------------------")
                        mod_of_capacity = prices[user_choice][7]-1
                    else:
                        print("back to menu")  # how to call menu method ????????
                df = pd.read_csv("discount.csv")
                df_indexed = df.set_index("name_discount", drop=True)
                list_username = list(df_account_indexed["name_discount"])
                logger.info("we check code from discount file .")
                darsaadd2 = [darsad2 for darsad2 in df]
                percent_of_code = darsaadd2[user_choice][2]
                if input_user_off_code not in list_username[1:]:
                    print("your input code is not defined !")
                    number_try -= 1
                    break
                else:
                    print("your total payment is : ", price_of_event - (1 / percent_of_job) * price_of_event - (1 / percent_of_code) * price_of_event)

            print("Do you want to continue paying ? y/n ")
            input_user_want_to_buy_or_not = input()
            logger.info("if user wants to buy ticket we will call shaparak .")
            if input_user_want_to_buy_or_not == 'y':
                print("-----------------shaparak-------------------")
                mod_of_capacity = prices[user_choice][7] - 1
            else:
                print("back to menu")  # how to call menu method ????????

        except ValueError :
            print("INVALID input.")
        except KeyError :
            logger.error("Not found in index .")
    @classmethod
    def menu_user(self):
        print("1-show events \n2-choose event \n3-create account \n4-log in \n")

obj=User(2,"A")
# print(obj.show_details_event(1))
obj.buy_ticket(2)