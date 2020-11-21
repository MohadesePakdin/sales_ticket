# this library is for systemic work
import sys
# this is an interface
from manager import Admin
from user import User
import logging
# #creat and configure logger
logger = logging.getLogger()

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
                                    # select the item and invoke related method
                                    print("please select one of follow choices:\n")
                                    print("1-show all active event \n"
                                          "2-show all event \n"
                                          "3-show all deactivate event\n"
                                          "4-create event \n"
                                          "5-remove event \n"
                                          "6-create discount\n"
                                          "7-Exit ")
                                    try:
                                        admin_input_selected = int(input("select an item: "))
                                        if admin_input_selected in range(1, 8):
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
                                                obj_admin.add_discount()
                                            elif admin_input_selected == 7:
                                                obj_admin.exit()
                                        else:
                                            print("your input is not valid please select other choice")
                                    except ValueError:
                                        print("your input is not valid please select other choice")
                                        logger.error("ValueError: invalid input (your choice should be integer) ")
                                        # if admin dont have an account should input a security code
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
                                              "6-create discount\n"
                                              "7-Exit ")
                                        try:
                                            admin_input_selected = int(input("select an item: "))
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
                                                    obj_admin.add_discount()
                                                elif admin_input_selected == 7:
                                                    obj_admin.exit()
                                            else:
                                                print("your input is not valid please select other choice")
                                        except ValueError:
                                            print("your input is not valid please select other choice")
                                            logger.error("ValueError:invalid input (maybe you wrote string character)")
                                else:
                                    print("security code is wrong!")
                                    # log warning
                                    logger.warning("security code is wrong!")

                                    sys.exit()
                            else:
                                print("your input is not valid please select other choice")
                                # log warning
                                logger.warning("your choices should be between 1 to 3")
                    except ValueError:
                        print("your input is not valid please select other choice")
                        # log error
                        logger.error("ValueError: invalid input")

            elif user_input_selected == 2:
                # if customer select create an object of this
                obj_customer = User("user")
                while True:
                    print(obj_customer.show_event())
                    print("do you want sale an event:\n1-yes\n2-no")
                    try:
                        selected_user = int(input("enter your choice: "))
                        if selected_user in range(1, 3):
                            if selected_user == 1:
                                print("do you have an account:\n1-yes\n2-no")
                                try:
                                    selected_user2 = int(input("enter your choice: "))
                                    if selected_user2 in range(1, 3):
                                        if selected_user2 == 1:
                                            obj_customer.log_in()
                                            print(obj_customer.active_event())
                                            input_user = int(input("your selection : "))
                                            obj_customer.show_details_event(input_user)
                                            obj_customer.choose_event(input_user)
                                            obj_customer.buy_ticket(input_user)
                                            break
                                        elif selected_user2 == 2:
                                            obj_customer.create_account()
                                            obj_customer.log_in()
                                            print(obj_customer.active_event())
                                            input_user = int(input("your selection : "))
                                            obj_customer.show_details_event(input_user)
                                            obj_customer.choose_event(input_user)
                                            obj_customer.buy_ticket(input_user)
                                            break
                                        else:
                                            print("your input is not valid please select other choice")
                                except ValueError:
                                    print("your input is not valid please select other choice")
                                    logger.error("ValueError: invalid input")
                            elif selected_user == 2:
                                print("thank you for see events\nbye")
                                input("enter any key to exit..... ")
                                sys.exit()
                            else:
                                print("your input is not valid please select other choice")
                                # log warning
                                logger.warning("")
                    except ValueError:
                        print("your input is not valid please select other choice")
                        # log error
                        logger.error("ValueError:invalid input")
            elif user_input_selected == 3:
                print("thank you for see events\nbye")
                input("enter any key to exit..... ")
                sys.exit()
            break
        else:
            print("your input is not valid please select other choice")
    except ValueError:
        print("your input is not valid please select other choice")
        logger.error("ValueError:invalid input")
