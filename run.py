# import event
import logging
import csv


logging.basicConfig(filename='mhp.log', format='%(asctime)s -- %(filename)s -- %(message)s')


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
        flag = 0
        print("please input username and password")
        user_name = input("username : ")
        pass_word = input("password : ")
        print("you are logging in as : \n 1-student \n 2-employee \n 3-teacher \n")
        user_job = input()
        if user_job == 1:
            type = "student"
        elif user_job == 2:
            type = "employee"
        elif user_job == 3:
            type = "teacher"
        else :
            return exit()
        try:
            with open("accountts.csv", mode='a+') as account_file:
                csv_writer = csv.writer(account_file, delimiter=',')
                # data = [["username", "password", "type"]]

                csv_writer .writerow([user_name, pass_word,type])


        except Exception:
            logging.exception('ERROR')

    # def log_in(self):
    #     username = input()
    #     password = input()
    #     # input user and pass
    #     if True:
    #         print("your logging is successfully")
    #     else:
    #         return False
    #         # halgheye while ezafe shavad ya eenke exit ra vared konad va kharej shavad


a = User('s', 'm')
# a.show_event()
# a.show_detail(1)
# a.choose_event(2)
a.create_account()