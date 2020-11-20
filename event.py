import csv


class Event:
    def __init__(self, id_event, name_event, date_event, time_event, place_event, cost_event, total_capacity,
                 mod_total_capacity, flag_event=1):
        self.id_event = id_event
        self.name_event = name_event
        self.date_event = date_event
        self.time_event = time_event
        self.place_event = place_event
        self.cost_event = cost_event
        self.total_capacity = total_capacity
        self.mod_total_capacity = mod_total_capacity
        self.flag_event = flag_event

    def __str__(self):
        return "create event successfully!"

    def create_event(self):
        file_path = "event.csv"
        row = [[self.id_event, self.name_event, self.date_event, self.time_event, self.place_event, self.cost_event,
                self.total_capacity, self.total_capacity, 1]]
        with open(file_path, 'a', newline='') as csv_events:
            # creating a csv writer object
            csv_writer = csv.writer(csv_events)
            # writing the data row
            csv_writer.writerows(row)
