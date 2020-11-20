import sys

import pandas as pd

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
                while True:
                    print("do you have an account:\n1-yes\n2-no")
                    try:
                        selected_admin = int(input("enter your choice: "))
                        if selected_admin in range(1, 3):
                            if selected_admin == 1:
                                print("login")
                                while True:
                                    print("choose menu")
                                    try:
                                        admin_input_selected = int(input("output of choose menu "))
                                        if admin_input_selected in range(1, 6):
                                            if admin_input_selected == 1:
                                                print("show_all_active_event()")
                                            elif admin_input_selected == 2:
                                                print("show_all_event()")
                                            elif admin_input_selected == 3:
                                                print("show_all_deactivate_event()")
                                            elif admin_input_selected == 4:
                                                print("create_event()")
                                            elif admin_input_selected == 5:
                                                print("exit()")
                                                sys.exit()
                                        else:
                                            print("your input is not valid please select other choice")
                                    except ValueError:
                                        print("your input is not valid please select other choice")
                            elif selected_admin == 2:
                                security_code = input("please enter security code for create account: ")
                                if security_code == "a123a123":
                                    print("create account")
                                    print("login")
                                    while True:
                                        print("choose menu")
                                        try:
                                            admin_input_selected = int(input("output of choose menu "))
                                            if admin_input_selected in range(1, 6):
                                                if admin_input_selected == 1:
                                                    print("show_all_active_event()")
                                                elif admin_input_selected == 2:
                                                    print("show_all_event()")
                                                elif admin_input_selected == 3:
                                                    print("show_all_deactivate_event()")
                                                elif admin_input_selected == 4:
                                                    print("create_event()")
                                                elif admin_input_selected == 5:
                                                    print("exit()")
                                                    sys.exit()
                                            else:
                                                print("your input is not valid please select other choice")
                                        except ValueError:
                                            print("your input is not valid please select other choice")
                                else:
                                    print("security code is wrong!")
                                    # log warning
                                    sys.exit()
                            else:
                                print("your input is not valid please select other choice")
                                # log warning
                    except ValueError:
                        print("your input is not valid please select other choice")
                        # log warning

            elif user_input_selected == 2:
                while True:
                    print("show event")  # invoke a method from user class
                    print("do you want sale a event:\n1-yes\n2-no")
                    try:
                        selected_user = int(input("enter your choice: "))
                        if selected_user in range(1, 3):
                            if selected_user == 1:
                                print("do you have an account:\n1-yes\n2-no")
                                try:
                                    selected_user2 = int(input("enter your choice: "))
                                    if selected_user2 in range(1, 3):
                                        if selected_user2 == 1:
                                            print("login")
                                            print("show_event")
                                            print("choose event")
                                            print("buy thicket")
                                            break
                                        elif selected_user2 == 2:
                                            print("create account")
                                            print("login")
                                            print("show_event")
                                            print("choose event")
                                            print("show detailed")
                                            print("buy thicket")
                                            break
                                        else:
                                            print("your input is not valid please select other choice")
                                except ValueError:
                                    print("your input is not valid please select other choice")
                            elif selected_user == 2:
                                print("thank you for see events\nbye")
                                input("enter any key to exit..... ")
                                sys.exit()
                            else:
                                print("your input is not valid please select other choice")
                                # log warning
                    except ValueError:
                        print("your input is not valid please select other choice")
                        # log warning
            elif user_input_selected == 3:
                print("thank you for see events\nbye")
                input("enter any key to exit..... ")
                sys.exit()
            break
        else:
            print("your input is not valid please select other choice")
    except ValueError:
        print("your input is not valid please select other choice")
