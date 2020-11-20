import logging
import csv
import sys

import pandas as pd

#logging.basicConfig(filename='mhp.log', format='%(asctime)s -- %(filename)s -- %(message)s')


# coloredlogs.install(fmt='%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s')


class User:
    def __init__(self,  file_path,username=None, password=None, flag=1):# delete file_path because dont use from customer
        self.username = username
        self.password = password
        self.file_path = file_path
        self.flag = flag

    def show_event(self, file_path):
        try:
            with open("event.csv", mode='a+') as new_file:
                csv_writer = csv.writer(new_file, delimiter=',')
                data = [["name_event", "date_event", "capasity", "time_event", "price"],
                        ["joker", "20nov", "100", "10:00", "10$"],
                        ["green book", "21nov", "100", "10:00", "12$"],
                        ["taste of c herry", "22nov", "100", "10:00", "20$"]]
                for row in data:
                    csv.reader(new_file)
                    print(row)

            new_file.close()
        except Exception:
            logging.exception('this is file error')
        # taghir konad

    def show_detail(self, user_input):  # in show_event methods we can not see some of details
        try:
            with open("event.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                movies = [movie for movie in csv_reader]
                print(f"movie name :", (movies[user_input][0]), ", date_event:", (movies[user_input][1]), ", zarfiat:",
                      (movies[user_input][2]))

        except Exception:
            logging.exception('this is file error')

    def choose_event(self, input_user):
        # input_user = int(input("your selection : "))
        with open("event.csv", 'r') as my_file:
            reader = csv.reader(my_file)
            rows = list(reader)
            print("your selection is :", rows[input_user][0])

    def create_account(self):

        file_path = "account.csv"
        try:
            df_account = pd.read_csv(file_path)
            df_account_indexed = df_account.set_index("id_account", drop=True)
            # df_account = pd.read_csv("account.csv")
            # df_account_indexed = df_account.set_index("id_account", drop=True)
            list_username = list(df_account_indexed["username"])
            while True:
                username_account = input("input your username: ")
                if username_account not in list_username[1:]:
                    print("Your username is created then submit your password . ")
                    break
                else:
                    print("Your name has already been entered with this username TRY ANOTHER ONE . ")
            # username_account = input("Please input username: ")
            password_account = input("Please input password: ")
            print("Please select one of follow choice:")
            print("You are logging in as : \n1-STUDENT \n2-EMPLOYEE \n3-TEACHER \n4-OTHER")
            # in future we want
            while True:
                # USER HAS TO INPUT ONE OF THEM
                try:
                    input_user_type = int(input("1 or 2 or 3: "))
                    if input_user_type in [1, 2, 3, 4]:
                        if input_user_type == 1:
                            print("shomare daneshjoye khod ra vared konid ")
                            type_account = "Student"  # 15%
                            break
                        elif input_user_type == 2:
                            type_account = "Employee"  # 10%
                            break
                        elif input_user_type == 3:
                            type_account = "Teacher"  # 10%
                            break
                        elif input_user_type == 4:
                            type_account = "Other"  # 0%
                            break
                    else:
                        print("Your input is INVALID please try again. ")
                except Exception:
                    print("Your input is INVALID please try again. ")
            row_account = [[df_account_indexed.index[-1] + 1, username_account, str(password_account), type_account, 1]]

            with open(file_path, 'a', newline='') as csv_account:
                csv_writer = csv.writer(csv_account)
                # writing the data row
                csv_writer.writerows(row_account)
        except Exception:
            print("you have not this file please create a file with name account.csv and set first row with this items "
                  "(id_account,username,password,flag)and second row with this item (0,) without parenthesis")
            logging.exception('not completely header in file')

    def log_in(self):

        number_try = 3
        while number_try > 0:  # baraye inke agar eshtebah vared kard dobare azash bkhad ke user pass bzne ya inke bre biron
            print("input your username and password")
            username = input("please enter your username: ")
            password = input("please enter your password: ")
            df_admin = pd.read_csv(self.file_path)
            df_admin_indexed = df_admin.set_index("id_account", drop=True)
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
                                    # Admin.show_event(Admin, 5)
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


a = User("account.csv")
# a.show_event("event.csv")
# a.show_detail(2)
# a.choose_event(2)
# a.create_account()
a.create_account()
a.log_in()
