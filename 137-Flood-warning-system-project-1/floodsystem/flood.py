from logging.config import listen
from .station import MonitoringStation
from .utils import sorted_by_key 

def stations_level_over_threshold(stations, tol):
    list = []
    tuple_data = []
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 0:
                if station.relative_water_level() >= tol:
                    list += station.name, station.relative_water_level()
                    tuple_data = [x for x in zip(*[iter(list)]*2)]
        tuple_data = sorted_by_key(tuple_data, 1)
    return tuple_data

def stations_highest_rel_level(stations, N):
    list = []
    tuple_data = []
    for station in stations:
        if station.latest_level and station.typical_range != None:
            x = station.latest_level - station.typical_range[1]
            list += station.name, x
            tuple_data = [x for x in zip(*[iter(list)]*2)]
    tuple_data = sorted_by_key(tuple_data, 1, reverse = True)
    return tuple_data[:N]