import csv



class Discount:
    def __init__(self, id_discount, name_discount, percent):
        self.id_discount = id_discount
        self.name_discount = name_discount
        self.percent = percent

    def __str__(self):
        return "create discount successfully!"

    def create_discount(self):
        file_path = "discount.csv"
        row = [[self.id_discount, self.name_discount, self.percent]]
        with open(file_path, 'a', newline='') as csv_discount:
            # creating a csv writer object
            csv_writer = csv.writer(csv_discount)
            # writing the data row
            csv_writer.writerows(row)
