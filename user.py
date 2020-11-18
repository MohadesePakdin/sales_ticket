# import event
import coloredlogs,logging
import csv
import pandas as pd

logging.basicConfig(filename='mhp.log', format='%(asctime)s -- %(filename)s -- %(message)s')
coloredlogs.install(fmt='%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s')


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show_event(self):
        try:
            with open("events.csv", mode='a+') as new_file:
                csv_writer = csv.writer(new_file, delimiter=',')
                data = [["name_event", "date_event", "capasity", "time_event", "price"],
                        ["joker", "20nov", "100", "10:00", "10$"],
                        ["green book", "21nov", "100", "10:00", "12$"],
                        ["taste of cherry", "22nov", "100", "10:00", "20$"]]
                for row in data:
                    csv_writer.writerow(row)
            new_file.close()
        except Exception:
            logging.exception('this is file error')

    def show_detail(self, user_input):
        try:
            with open("events.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                movies = [movie for movie in csv_reader]
                print(f"movie name :", (movies[user_input][0]), ", date_event:", (movies[user_input][1]), ", zarfiat:",
                      (movies[user_input][2]))

        except Exception:
            logging.exception('this is file error')

    def choose_event(self, input_user):
        input_user = int(input("your selection : "))
        with open("events.csv", 'r') as my_file:
            reader = csv.reader(my_file)
            rows = list(reader)
            print("your selection is :", rows[input_user][0])

    def create_account(self):

        file_path = "account.csv"
        try:
            df_account = pd.read_csv(file_path)
            df_account_indexed = df_account.set_index("id_account", drop=True)
            username_account = input("Please input username: ")
            password_account = input("Please input password: ")
            print("Please select one of follow choice:")
            print("You are logging in as : \n1-STUDENT \n2-EMPLOYEE \n3-TEACHER \n")
            #in future we want
            while True:
                #USER HAS TO INPUT ONE OF THEM
                try:
                    input_user_type = int(input("1 or 2 or 3: "))
                    if input_user_type in [1, 2, 3]:
                        if input_user_type == 1:
                            type_account = "Student"
                            break
                        elif input_user_type == 2:
                            type_account = "Employee"
                            break
                        elif input_user_type == 3:
                            type_account = "Teacher"
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
        df_account = pd.read_csv("account.csv")
        print(df_account)
        df_account_indexed = df_account.set_index("id_account", drop=True)
        print(df_account_indexed)
        list_username = list(df_account_indexed["username"])
        print(list_username[1:])
        while True:
            username = input("input your username: ")
            if username not in list_username[1:]:
                print("add")
                break
            else:
                print("your username duplicated ")
        password = input()



a = User('s', 'm')
# a.show_event()
# a.show_detail(1)
# a.choose_event(2)
a.create_account()
