from datetime import datetime
from ride import Ride

def is_distace_valid(distance: float) -> bool:
    return type(distance) in [float,int] and distance > 0

def is_date_valid(date: datetime) -> bool:
    return date != None and isinstance(date, datetime)

def calculate_ride(rideArray: list[Ride]):
    fare = 0
    for ride in rideArray:
        if (is_distace_valid(ride.distance)):
            if (is_date_valid(ride.date)):

                # // overnight

                if (ride.date.hour >= 22 or ride.date.hour <= 6):
                    
                    # // not sunday            
                    if ride.date.weekday() != 6:  
                        fare += ride.distance * 3.90
                    
                    #sunday
                    else:
                        fare += ride.distance * 5
                else:
 					#// sunday
                    if ride.date.weekday() == 6:
                        fare += ride.distance * 2.9
                    
                    else:
                        fare += ride.distance * 2.10
            else:
                return -2
        
        else:
            return -1

    if	fare < 10:
        return 10
    else:
        return fare