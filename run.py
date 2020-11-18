import sys

import pandas as pd

# this is a welcome message
from manager import Admin
from user import User

print("-----------------------------------------------------------------------------------")
print("---------------------------welcome to sales ticket app-----------------------------")
print("---------------------create by parisa , reyhane , mohaddese------------------------")
while True:
    print("please select one of follow choices:")
    print("1-admin \n2-customer\n3-exit ")
    try:
        user_input_selected = int(input("enter your choice: "))
        if user_input_selected in range(1, 4):
            if user_input_selected == 1:
                obj_admin = Admin()
                obj_admin.log_in()
                # menu(add_event  ,  add_off  ,  show_detail , update/remove_event)
                #add_event : define a new event
                #add_off :
                break
            elif user_input_selected == 2:
                obj_user = User()
                obj_user.show_event("event.csv") #hameye detail ro neshun nadim (masalan price)
                input_user = int(input("select one of them :"))
                obj_user.choose_event(input_user)
                obj_user.show_detail(input_user)  #eenja hame ye jozeiat dide she
                print("Do you want to buy it ?")
                input_user_want_to_buy = input("y/n")
                if input_user_want_to_buy == 'y' :
                    print("log in OR sign in ?")
                    input_user_log_or_sign = int(input("1 or 2"))
                    if input_user_log_or_sign == 1:
                        obj_user.log_in()
                    elif input_user_log_or_sign == 2:
                        obj_user.create_account()

                    #agar ba movafaghiat vared shod marahele kharid ra edame dahad

                elif input_user_want_to_buy == 'n':
                    print("Do you want to exit or back to menu ?")
                    input_user_exit_or_continue = input("exit or continue")
                    if input_user_exit_or_continue == 'exit':
                        sys.exit()
                    elif input_user_exit_or_continue == 'continue':
                        obj_user.show_event("event.csv")

                break #exit
        else:
            print("your input is not valid please select other choice")
    except ValueError:
        print("your input is not valid please select other choice")



