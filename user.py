# import event
import coloredlogs, logging
import csv
import pandas as pd
#import person

logging.basicConfig(filename='mhp.log', format='%(asctime)s -- %(filename)s -- %(message)s')


# coloredlogs.install(fmt='%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s')

#show event , show detail , exit
class User:
    def __init__(self,event_choice):
        self.event_choice = event_choice


    def show_event(self, file_path):
        try:

            #رویداد های موجود را کاربر هنگام ورود ببیند .

            '''with open("event.csv", mode='a+') as new_file:
                csv_writer = csv.writer(new_file, delimiter=',')
                data = [["name_event", "date_event", "capasity", "time_event", "price"],
                        ["joker", "20nov", "100", "10:00", "10$"],
                        ["green book", "21nov", "100", "10:00", "12$"],
                        ["taste of cherry", "22nov", "100", "10:00", "20$"]]
                for row in data:
                    csv.reader(new_file)
                    print(row)

            new_file.close()'''
        except Exception:
            logging.exception('this is file error')
        # taghir konad

    def show_detail(self, user_input):  #in show_event methods we can not see some of details

        #رویدادی را که انتخاب می کند جزییات بیشتری ازش ببیند : کارگردان-سال ساخت-مدت زمان برنامه-ژانر
        try:
            with open("event.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                movies = [movie for movie in csv_reader]
                print(f"movie name :", (movies[user_input][0]), ", date_event:", (movies[user_input][1]), ", zarfiat:",
                      (movies[user_input][2]))

        except Exception:
            logging.exception('this is file error')

    def choose_event(self):
        #اگر متد قبلی فراخانی شده بود از کاربر بپرسه خروج یا برگشت یا خرید ؟

        # input_user = int(input("your selection : "))
        try :
            with open("event.csv", 'r') as my_file:
                reader = csv.reader(my_file)
                rows = list(reader)
                print("your selection is :", rows[self.event_choice][0])
        except FileNotFoundError :
            logging.exception('couldnt find event file')

    def create_account(self):
        #کاربر اگر قصد خرید داشت یا باید وارد شود یا حساب کاربری بسازد
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
                            # azash shomare daneshjoyee nakhad ?? 123....
                            # ta se bar azash code mikhaym age har se bar avalesh 123 nadasht dige 15% emal nmishe
                            break
                        elif input_user_type == 2:
                            type_account = "Employee"  # 10%
                            # azash shomare karmandi nakhad ?? 456....
                            break
                        elif input_user_type == 3:
                            type_account = "Teacher"  # 10%
                            # azash shomare moalemi nakhad ?? 789....
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
        try :
            df_account = pd.read_csv("account.csv")
            df_account_indexed = df_account.set_index("id_account", drop=True)
            list_username = list(df_account_indexed["username"])
            number_try = 3
            while number_try > 0:
                input_username_login = input("input your username ")
                if input_username_login not in list_username[1:]:
                    print("try again")
                else:
                    list_password = list(df_account_indexed["password"])
                    input_userpass_login = input("input your password ")
                    # when username was ok give password 3 times

                    if input_userpass_login not in list_password[1:]:
                        print("try again")
                        number_try -= 1
                    else:
                        print("You logged in successful")
                    # else:
                    #     print("OOPS You are blocked ")

                    # parisa log in manager t ro neshunam midi
                    # show_event k taghir kard ro ham lotfan
        except FileNotFoundError :
            logging.exception('coudent find account file')

    def buy_ticket(self):
        print("how many tickets do you want ?")
        #tedade ticket ha
        #ghimate kol : ...
        #gheimat ba bon (daneshjoyee,karmandi,moalemi) : ...
        print("Do you have off_code ?")
        #if No pay/cancel
        #if yes calculate last price


a = User('k')
# a.show_event("event.csv")
# a.show_detail(2)
# a.choose_event(2)
# a.create_account()
a.log_in()
