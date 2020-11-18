from user import User
from event import Event
import pandas as pd
class Discount :
    ''' az file event.csv gheimat ha ro migirim az user
    hoviateshuno migirim va ro gheimate avalie emal
    mikonim.
    bad ye csv jadid misazim tush code takhfif ba % shun
    tarif konim va ro ghimate nahaie emal konim '''

    file_path = "event.csv"
    df_account = pd.read_csv(file_path)
    df_account_indexed = df_account.set_index("id_account", drop=True)
    list_cost_event = list(df_account_indexed["cost_event"])



    def give_code(self):
        file_path_off = "discount.csv"
        df_account = pd.read_csv(file_path_off)
        df_account_indexed = df_account.set_index("id_account", drop=True)
        list_discount = list(df_account_indexed["off"])
        while True:
            input_give_off_code = input("Please input your code: ")
            if input_give_off_code in list_discount[1:]:
                print("yes")
                break
            else:
                print("invalid")

    '''csv ma 3 ta sutun dashte bashe   code,%,gheimat '''
