from user import User
from event import Event
import pandas as pd


class Discount:
    def __init__(self, id_discount, name_discount, darsad):
        self.id_discount = id_discount
        self.name_discount = name_discount
        self.darsad = darsad

    def __str__(self):
        return "create discount successfully!"
