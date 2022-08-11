from datetime import datetime


class Ride:
    def __init__(self, date: datetime, distance: float):
        self.date = date
        self.distance = distance
    