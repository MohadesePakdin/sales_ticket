import sys

import pandas as pd

# this is a welcome message
from v1.admin import Admin
from v1.user import User

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
                break
            elif user_input_selected == 2:
                obj_user = User()
                obj_user.show_event("event.csv")
                user_event_select=input("please select one of events: ")
                obj_user.show_detail(user_event_select)
                break
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
