from datetime import datetime
import pytest
from fare_calculator import calculate_ride
from ride import Ride

def test_deve_calcular_uma_corrida_overnight_sunday():
    ride = Ride(date=datetime(year=2022,month=8,day=7,hour=22),distance=10)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == 50

def test_deve_calcular_uma_corrida_sunday():
    ride = Ride(date=datetime(year=2022,month=8,day=7,hour=20),distance=10)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == 29

def test_deve_calcular_uma_corrida_overnight_comum():
    ride = Ride(date=datetime(year=2022,month=8,day=9,hour=22),distance=10)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == 39

def test_deve_calcular_uma_corrida_comum():
    ride = Ride(date=datetime(year=2022,month=8,day=9,hour=20),distance=10)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == 21

def test_deve_calcular_uma_corrida_com_taxa_minima():
    ride = Ride(date=datetime(year=2022,month=8,day=9,hour=22),distance=2)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == 10

def test_nao_deve_calcular_uma_corrida_com_distancia_invalida():
    ride = Ride(date=datetime(year=2022,month=8,day=9,hour=22),distance=-10)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == -1

def test_nao_deve_calcular_uma_corrida_com_data_invalida():
    ride = Ride(date=123,distance=10)
    rideArray = [ride]
    fare = calculate_ride(rideArray)
    assert fare == -2

