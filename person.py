import sys

import pandas as pd


class Person:
    def __init__(self, status, username=None, password=None, flag=1):
        self.status = status
        self.username = username
        self.password = password
        self.flag = flag

    def log_in(self):
        if self.status == 'admin':
            file_path = "admin.csv"
            id_person = "id_admin"
        else:
            file_path = "account.csv"
            id_person = "id_account"
        number_try = 3
        while number_try > 0:
            print("input your username and password")
            username = input("please enter your username: ")
            password = input("please enter your password: ")
            df = pd.read_csv(file_path)
            df_indexed = df.set_index(id_person, drop=True)
            try:
                if df_indexed.iloc[df_indexed.index[df_indexed['username'] == username].tolist()[0], 1] == int(
                        password):
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

            except ValueError:
                print("your username or password is WRONG .")
        else:
            input("\n\nyou try upper than 3 times your account block print any key to exit: ")
            sys.exit()

    def show_event(self):
        df_first = pd.read_csv("event.csv")
        df_first_2 = df_first[
                         ["id_event", "Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                          "Total_capacity", "Mod_total_capacity", "Flag_event"]].loc[1:, :]
        df_first_2["Cost_event"] = df_first_2["Cost_event"].astype(int)
        df_first_2["Mod_total_capacity"] = df_first_2["Mod_total_capacity"].astype(int)
        pd.set_option('display.max_columns', None)
        print(df_first_2)

    @staticmethod
    def exit():
        sys.exit()

    def show_details_event(self):
        # admin : zarfiate baghi mande
        # user : detail of event
        pass

# obj_person = Person('d')
# obj_person.log_in()
