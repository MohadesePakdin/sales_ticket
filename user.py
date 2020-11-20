# import event
import sys

import coloredlogs, logging
import csv
import pandas as pd
import os
from person import Person

logging.basicConfig(filename='mhp.log', format='%(asctime)s -- %(filename)s -- %(message)s')


class User(Person):
    def __init__(self, event_choice, status):
        super().__init__(status)
        self.event_choice = event_choice

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

    def show_detail(self, user_input):  # in show_event methods we can not see some of details

        # رویدادی را که انتخاب می کند جزییات بیشتری ازش ببیند : کارگردان-سال ساخت-مدت زمان برنامه-ژانر
        try:
            with open("event.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                movies = [movie for movie in csv_reader]
                print(f"movie name :", (movies[user_input][1]), ", date_event:", (movies[user_input][2]), ", zarfiat:",
                      (movies[user_input][3]))

        except Exception:
            logging.exception('this is file error')

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
                            print("shomare daneshjoye khod ra vared konid ")
                            type_account = "Student"
                            persent = 15
                            break
                        elif input_user_type == 2:
                            type_account = "Employee"
                            persent = 10
                            break
                        elif input_user_type == 3:
                            type_account = "Teacher"
                            persent = 12
                            break
                        elif input_user_type == 4:
                            type_account = "Other"
                            persent = 0
                            break
                    else:
                        print("Your input is INVALID please try again. ")
                except Exception:
                    print("Your input is INVALID please try again. ")
            row_account = [
                [df_account_indexed.index[-1] + 1, username_account, str(password_account), type_account, persent, 1]]

            with open(file_path, 'a', newline='') as csv_account:
                csv_writer = csv.writer(csv_account)
                # writing the data row
                csv_writer.writerows(row_account)
        except Exception:
            print("you have not this file please create a file with name account.csv and set first row with this items "
                  "(id_account,username,password,flag)and second row with this item (0,) without parenthesis")
            logging.exception('not completely header in file')

    # def log_in(self):

    # number_try = 3
    # while number_try > 0:
    #     print("input your username and password")
    #     username = input("please enter your username: ")
    #     password = input("please enter your password: ")
    #     df = pd.read_csv("account.csv")  # admin.csv
    #     df_indexed = df.set_index("id_account", drop=True)  # id_admin
    #     try:
    #         if df_indexed.iloc[df_indexed.index[df_indexed['username'] == username].tolist()[0], 1] == int(
    #                 password):
    #             ###################  ta jayee ke bekhad username ro migire mage eenke password dorost bezanim .
    #
    #             print("correct")
    #             break
    #
    #         else:
    #             print("your username or password is wrong please try again")
    #     except IndexError:
    #         if number_try > 1:
    #             print("your username or password is wrong please try again")
    #             number_try -= 1
    #         else:
    #             print("your username or password is wrong")
    #             number_try -= 1
    #
    #     except ValueError:
    #         print("your username or password is WRONG .")
    # else:
    #     input("\n\n you try upper than 3 times your account block print any key to exit: ")
    #     sys.exit()

    def buy_ticket(self, user_choice):

        print("how many tickets do you want ? ")
        many_of_ticket = int(input())
        df_account = pd.read_csv("event.csv")
        df_account_indexed = df_account.set_index("id_account", drop=True)
        prices = [price for price in df_account]
        a = prices[user_choice][5]
        df_account2 = pd.read_csv("account.csv")
        df_account_indexed = df_account.set_index("id_account", drop=True)
        darsaad = [darsad for darsad in df_account2]
        b = darsaad[user_choice][4]
        print("your total payment is : ", a - 1 / b * a)
        print("Do you have any off code ? (if yes please input it )")
        number_try = 3
        while number_try > 0:
            input_user_off_code = input("")
            if input_user_off_code == 'no':
                print("Do you want to continue paying ? y/n ")
                input_user_want_to_buy_or_not = input()
                if input_user_want_to_buy_or_not == 'y':
                    print("-----------------shaparak------------------")
                    d = prices[user_choice][7]-1
                else:
                    print("back to menu")  # how to call menu method ????????
            df = pd.read_csv("discount.csv")
            df_indexed = df.set_index("name_discount", drop=True)
            list_username = list(df_account_indexed["name_discount"])
            darsaadd2 = [darsad2 for darsad2 in df]
            c = darsaadd2[user_choice][2]
            if input_user_off_code not in list_username[1:]:
                print("your input code is not defined !")
                number_try -= 1
                break
            else :
                print("your total payment is : ", a - 1 / b * a - 1 / c * a)

        print("Do you want to continue paying ? y/n ")
        input_user_want_to_buy_or_not = input()
        if input_user_want_to_buy_or_not == 'y':
            print("-----------------shaparak-------------------")
            d = prices[user_choice][7] - 1
        else:
            print("back to menu")  # how to call menu method ????????


    @classmethod
    def menu_user(self):
        print("1-show events \n2-choose event \n3-create account \n4-log in \n")


a = User('k', 'd')
# a.show_event()
# a.show_detail(2)
# a.choose_event(2)
# a.create_account()
# a.log_in()
a.buy_ticket(2)
