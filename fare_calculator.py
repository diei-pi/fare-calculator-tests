from datetime import datetime
from ride import Ride

def is_distace_valid(distance: float) -> bool:
    return type(distance) in [float,int] and distance > 0

def is_date_valid(date: datetime) -> bool:
    return date != None and isinstance(date, datetime)

def is_sunday(day: datetime) -> bool:
    return day.weekday() == 6

def is_overnight(date: datetime) -> bool:
    return date.hour >= 22 or date.hour <= 6

def is_overnight_sunday(date: datetime) -> bool:
    return is_overnight(date) and is_sunday(date)

def is_overnight_and_not_sunday(date: datetime) -> bool:
    return is_overnight(date) and not is_sunday(date)

OVERNIGHT_SUNDAY_FARE = 5
OVERNIGHT_FARE = 3.90
SUNDAY_FARE = 2.9
COMMON_FARE = 2.10
MINIMUN_FARE = 10

def calculate_ride(rideArray: list[Ride]):
    fare = 0
    for ride in rideArray:
        if not is_distace_valid(ride.distance): raise Exception("Invalid distance")
        if not is_date_valid(ride.date): raise Exception("Invalid date")
        if is_overnight_sunday(ride.date):
            fare += ride.distance * OVERNIGHT_SUNDAY_FARE
        elif is_overnight(ride.date):
            fare += ride.distance * OVERNIGHT_FARE
        elif is_sunday(ride.date):
            fare += ride.distance * SUNDAY_FARE
        else:
            fare += ride.distance * COMMON_FARE
    if	fare < MINIMUN_FARE:
        return MINIMUN_FARE
    else:
        return fare