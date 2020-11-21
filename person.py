import sys

import pandas as pd


class Person:
    def __init__(self, status, username=None, password=None, flag=1):
        """
        this class is for create a new person
        status: admin or user
        username: username
        password: password
        flag: person live or not
        """
        self.status = status
        self.username = username
        self.password = password
        self.flag = flag

    def log_in(self):
        """
        this method is for login manager or user
        """
        if self.status == 'admin':
            file_path = "manager.csv"
            id_person = "id_manager"
        else:
            file_path = "account.csv"
            id_person = "id_account"
        number_try = 3
        while number_try > 0:
            print("input your username and password")
            username = input("please enter your username: ")
            password = input("please enter your password: ")
            try:
                df = pd.read_csv(file_path)
                df_indexed = df.set_index(id_person, drop=True)
                try:
                    if df_indexed.iloc[df_indexed.index[df_indexed['username'] == username].tolist()[0], 1] == int(
                            password):
                        print("you log in successfully now you can choice menu!")
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
            except FileNotFoundError:
                print("you dont have this file you can make this by steps 1- create "
                      "a file by name manager.csv and in this row"
                      "row one:id_manager,username,password,flag"
                      "row two:0,")

    def show_event(self):
        """
        this method show a dataframe
        return: a dataframe
        """
        df_first = pd.read_csv("event.csv")
        df_first_2 = df_first[
                         ["id_event", "Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                          "Total_capacity", "Mod_total_capacity", "Flag_event"]].loc[1:, :]
        df_first_2["Cost_event"] = df_first_2["Cost_event"].astype(int)
        df_first_2["Mod_total_capacity"] = df_first_2["Mod_total_capacity"].astype(int)
        df_first_2["Flag_event"] = df_first_2["Flag_event"].astype(int)
        df_first_2["Total_capacity"] = df_first_2["Total_capacity"].astype(int)
        pd.set_option('display.max_columns', None)
        return df_first_2

    @staticmethod
    def exit():
        """
        this method is for exit
        """
        sys.exit()

    @staticmethod
    def show_details_event(index_event):
        """
        this method show a special event with details
        index_event: index of selection event
        return: a row of dataframe
        """
        pd.set_option('display.max_columns', None)
        df_first = pd.read_csv("event.csv")
        df_first_2 = df_first[
                         ["id_event", "Name_event", "Date_event", "Time_event", "place_event", "Cost_event",
                          "Total_capacity", "Mod_total_capacity", "Flag_event"]].loc[1:, :]
        df_first_3 = df_first_2.loc[[index_event]]
        df_first_3["Cost_event"] = df_first_3["Cost_event"].astype(int)
        df_first_3["Mod_total_capacity"] = df_first_3["Mod_total_capacity"].astype(int)
        df_first_3["Total_capacity"] = df_first_3["Total_capacity"].astype(int)
        df_first_3["Flag_event"] = df_first_3["Flag_event"].astype(int)
        print(df_first_3.loc[[index_event]])

    @staticmethod
    def active_event():
        """

        return: a dataframe
        """
        df = pd.read_csv("event.csv")
        df_active_event = df.loc[df['Flag_event'] == 1]
        pd.set_option('display.max_columns', None)
        return df_active_event
