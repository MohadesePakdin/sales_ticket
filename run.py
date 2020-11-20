# this library is for systemic work
import sys
import logging
# this is an interface
from manager import Admin

print("-----------------------------------------------------------------------------------")
print("---------------------------welcome to sales ticket app-----------------------------")
print("---------------------create by parisa , reyhane , mohaddese------------------------")
while True:
    # user has 3 choice she/he can select one of them
    print("please select one of follow choices:")
    print("1-admin \n2-customer\n3-exit ")
    try:
        # user input one of them
        user_input_selected = int(input("enter your choice: "))
        # this if check that input was in range
        if user_input_selected in range(1, 4):
            # if this if True mean user is admin
            if user_input_selected == 1:
                obj_admin = Admin("admin")
                while True:
                    # this line check admin have an account or no
                    print("do you have an account:\n1-yes\n2-no")
                    try:
                        # admin select one of this choice (has account or no)
                        selected_admin = int(input("enter your choice: "))
                        if selected_admin in range(1, 3):
                            if selected_admin == 1:
                                # create an object from admin class
                                # invoke login method
                                obj_admin.log_in()
                                while True:
                                    print("please select one of follow choices:\n")
                                    print("1-show all active event \n"
                                          "2-show all event \n"
                                          "3-show all deactivate event\n"
                                          "4-create event \n"
                                          "5-remove event \n"
                                          "6-Exit ")
                                    try:
                                        admin_input_selected = int(input("output of choose menu "))
                                        if admin_input_selected in range(1, 7):
                                            if admin_input_selected == 1:
                                                print(obj_admin.active_event())
                                            elif admin_input_selected == 2:
                                                print(obj_admin.show_event())
                                            elif admin_input_selected == 3:
                                                print(obj_admin.deactive_event())
                                            elif admin_input_selected == 4:
                                                obj_admin.add_event()
                                            elif admin_input_selected == 5:
                                                obj_admin.remove_event()
                                            elif admin_input_selected == 6:
                                                obj_admin.exit()
                                        else:
                                            print("your input is not valid please select other choice")
                                    except ValueError:
                                        print("your input is not valid please select other choice")
                            elif selected_admin == 2:
                                security_code = input("please enter security code for create account: ")
                                if security_code == "a123a123":
                                    obj_admin.register()
                                    obj_admin.log_in()
                                    while True:
                                        print("please select one of follow choices:\n")
                                        print("1-show all active event \n"
                                              "2-show all event \n"
                                              "3-show all deactivate event\n"
                                              "4-create event \n"
                                              "5-remove event \n"
                                              "6-Exit ")
                                        try:
                                            admin_input_selected = int(input("output of choose menu "))
                                            if admin_input_selected in range(1, 7):
                                                if admin_input_selected == 1:
                                                    print(obj_admin.active_event())
                                                elif admin_input_selected == 2:
                                                    print(obj_admin.show_event())
                                                elif admin_input_selected == 3:
                                                    print(obj_admin.deactive_event())
                                                elif admin_input_selected == 4:
                                                    obj_admin.add_event()
                                                elif admin_input_selected == 5:
                                                    obj_admin.remove_event()
                                                elif admin_input_selected == 6:
                                                    obj_admin.exit()
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
