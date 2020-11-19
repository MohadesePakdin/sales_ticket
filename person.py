import csv
import sys

import pandas as pd


class Person:
    def __init__(self, status, username=None, password=None, flag=1):
        self.status = status
        self.username = username
        self.password = password
        self.flag = flag

    def log_in(self):
        number_try = 3
        while number_try > 0:
            print("input your username and password")
            username = input("please enter your username: ")
            password = input("please enter your password: ")
            df= pd.read_csv("account.csv")#admin.csv
            df_indexed = df.set_index("id_account", drop=True)#id_admin
            try:
                if df_indexed.iloc[df_indexed.index[df_indexed['username'] == username].tolist()[0], 1] == int(password):
                    print("correct")
                    break
                else:
                    print("your username or password is wrong please try again")
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

    def crate_account(self):
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
            print("Please select one of follow choice:")
            print("You are logging in as : \n1-STUDENT \n2-EMPLOYEE \n3-TEACHER \n4-OTHER")
            # in future we want
            while True:
                input_user_type = input("1 or 2 or 3: ")
                try:
                    input_user_type_int=int(input_user_type)
                    if input_user_type_int in [1, 2, 3, 4]:
                        if input_user_type_int == 1:
                            type_account = "Student"
                            break
                        elif input_user_type_int == 2:
                            type_account = "Employee"
                            break
                        elif input_user_type_int == 3:
                            type_account = "Teacher"
                            break
                        elif input_user_type_int == 4:
                            type_account = "Other"
                            break
                    else:
                        print("Your input is INVALID please try again. ")

                except ValueError:
                    print("Your input is INVALID please try again. ")
            row_account = [[df_indexed.index[-1] + 1, username_account, str(password_account), type_account, 1]]

            with open(file_path, 'a', newline='') as csv_account:
                csv_writer = csv.writer(csv_account)
                # writing the data row
                csv_writer.writerows(row_account)
        except Exception:
            print("you have not this file please create a file with name account.csv and set first row with this items "
                  "(id_account,username,password,flag)and second row with this item (0,) without parenthesis")
            # logging.exception('not completely header in file')



    def show_event(self):
        pass

    def exit(self):
        sys.exit()

    def show_details_event(self):
        pass

