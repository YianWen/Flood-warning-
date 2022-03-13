from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from haversine import haversine

list = build_station_list() 

def test_call():
    ordered = []
    p = (0,0)
    ordered = station_by_distance(list, p)

def test_order():
    ordered = []
    p = (0,0)
    ordered = station_by_distance(list, p)
    i = 1
    sub = 0 
    while i < (len(ordered) -1):
        if(ordered[i][1] > ordered[i - 1][1]):
            sub = 1
        i += 1
    assert sub == 1

def test_distance():
    in_distance = []
    in_distance = stations_within_radius(list, (52.2053, 0.1218), 10)
    everything_good = True
    if 'Boscadjack' in in_distance:
        everything_good = False
    assert everything_good == True

def test_alphabetical():
    fingers_crossed = True
    rivers = []
    rivers = rivers_with_station(list)
    c = [rivers[i] for i in range(len(rivers))]
    c.sort()
    for i in range(len(rivers)):
        if (c[i] != rivers[i]):
            fingers_crossed = False
    assert fingers_crossed == True

def test_call_two():
    rivers_and_stations = []
    rivers_and_stations = stations_by_river(list)

# To check whether include more rivers with the same number of stations
def test_including():
    same_num_stations = True
    rivers_station = rivers_by_station_number(list, 9)
    num_stations = [river[1] for river in rivers_station]
    if num_stations[8] != num_stations[9]:
        same_num_stations = False
    assert same_num_stations == True
    assert len(rivers_station) == 10

# Check if the numbers are sorted
def test_sorted_number():
    sorted_number = True
    rivers_station = rivers_by_station_number(list, 9)
    previous_num_stations = 0
    for num_stations in rivers_station:
        if previous_num_stations ==0:
            previous_num_stations = num_stations[1]
        if previous_num_stations < num_stations[1]:
            sorted_number = False
            break
    assert sorted_number == True




