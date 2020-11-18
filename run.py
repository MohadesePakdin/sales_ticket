import sys

import pandas as pd

# this is a welcome message

print("-----------------------------------------------------------------------------------")
print("---------------------------welcome to sales ticket app-----------------------------")
print("---------------------create by parisa , reyhane , mohaddese------------------------")
while True:
    print("please select one of follow choices:\n")
    print("1-admin \n2-customer\n3-exit ")
    try:
        user_input_selected = int(input("enter your choice: "))
        if user_input_selected in range(1,4):
            if user_input_selected == 1:
                number_try = 3
                while number_try > 0:  # baraye inke agar eshtebah vared kard dobare azash bkhad ke user pass bzne ya inke bre biron
                    print("input your username and password")
                    username = input("please enter your username: ")
                    password = input("please enter your password: ")
                    df_admin = pd.read_csv("admin.csv")
                    df_admin_indexed = df_admin.set_index("id_admin", drop=True)
                    try:
                        if str(df_admin_indexed.iloc[
                                   df_admin_indexed.index[df_admin_indexed['username'] == username].tolist()[
                                       0] - 1, 1]) == password:
                            #obj_admin = Admin()
                            while True:
                                print("please select one of follow choices:\n")
                                print("1-show all active event \n"
                                      "2-show all event \n"
                                      "3-show all deactive event\n"
                                      "4-create event \n"
                                      "4-remove event \n"
                                      "5-Exit ")
                                try:
                                    admin_input_selected = int(input("enter your choice: "))
                                    if admin_input_selected in range(1,6):
                                        if admin_input_selected == 1:
                                            print("show_all_active_event()")
                                            #obj_admin.show_all_active_event()
                                        elif admin_input_selected == 2:
                                            print("show_all_event()")
                                            #obj_admin.show_all_event()
                                        elif admin_input_selected == 3:
                                            print("show_all_deactive_event()")
                                            #obj_admin.show_all_deactive_event()
                                        elif admin_input_selected == 4:
                                            print("create_event()")
                                            #obj_admin.create_event()
                                        elif admin_input_selected == 5:
                                            print("exit()")
                                            sys.exit()
                                    else:
                                        print("your input is not valid please select other choice")
                                except ValueError:
                                    print("your input is not valid please select other choice")
                            break
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
        else:
            print("your input is not valid please select other choice")
    except ValueError:
        print("your input is not valid please select other choice")

#         if True:  # read from csv and check/ log in succ
#             print("1-show_details_event 2-add_event3-remove_event4- create_off5-exit()")
#             input_selected = input("select a item: ")
#             if input_selected == 1:
#                 Admin.show_details_event()
#                 # tamrin 2 soal 2 ...... admin modam menu bbinad
#             elif input_selected == 2:
#                 Admin.add_event()
#             elif input_selected == 3:
#                 Admin.remove_event()
#             elif input_selected == 4:
#                 pass
#             else:
#                 sys.exit()
#         print("user or pass is wrong please try again")
#
# elif a == 2:
#     User.show_event()
#     print("aya ghasde kharid darid ? y/n")
#     a = input()
#     if a == 'y':
#         print("1-log in \n 2-sign up")
#         b = int(input("vared kon"))
#         if b == 1:
#             User.log_in()
#
#         elif b == 2:
#             # user o pass ro migire mire add mikone be file csv mun
#             # file ya method bashe?
#             User.log_in()
#
#         User.show_event()
#         print("please select one of them")
#         a = int(input())
#         # 1-x
#         # 2-y
#         # 3-z
#         User.show_detail()
#         # show detail of the chossen event
#         print("tedade blit ra vared konid !!!")
#         c = input()
#         # gheimate kole blit haye shoma 30000 toman mishe
#         print("aya code takhfif darid ?")
#         g = input()
#         if g == 'y':
#         # check in csv va emal takhfif
#         # age nabud begim yaft nashod ya KHARID kone ya CANCEL
#         elif g == 'n':
#             print("pol bede ")
#
#
#     else:
#         sys.exit()
