# this library is for write and read from csv file
import csv



class Discount:
    """
    this class used for create a discount that admin create this
    """
    def __init__(self, id_discount, name_discount, percent):
        """
        id_discount: id for discount
        name_discount: name for discount
        percent: percent od discount
        """
        self.id_discount = id_discount
        self.name_discount = name_discount
        self.percent = percent

    def __str__(self):
        """
        this method return a successfully message for create discount
        return: str
        """
        return "create discount successfully!"

    def create_discount(self):
        """
        this method create a discount
        return: an object
        """
        file_path = "discount.csv"
        row = [[self.id_discount, self.name_discount, self.percent]]
        with open(file_path, 'a', newline='') as csv_discount:
            # creating a csv writer object
            csv_writer = csv.writer(csv_discount)
            # writing the data row
            csv_writer.writerows(row)
