# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from codecs import ignore_errors
from tokenize import Ignore
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine

def station_by_distance(stations, p):
    station_data = []
    for station in stations:
        station_data += station.name, haversine(station.coord, p)
        tuple_data = [x for x in zip(*[iter(station_data)]*2)]
        tuple_data = sorted_by_key(tuple_data, 1)
    return tuple_data

def stations_within_radius(stations, centre, r):
    stations_in_range = []
    for x in stations:
        if haversine(x.coord, centre) < r:
            stations_in_range.append(x.name)
    return sorted(stations_in_range)
    
def rivers_with_station(stations):
    rivers = []
    for riv in stations:
        rivers.append(riv.river)
    rivers = set(rivers)
    rivers = sorted(rivers)
    return rivers

def stations_by_river(stations):
    dict = {}
    for x in stations:
        dict[x.river] = []
    for n in stations:
        if n.river in dict:
            dict[n.river].append(n.name)
            dict[n.river] = sorted(dict[n.river])
    return dict

def rivers_by_station_number(stations, N):
    rivers_station = []
    # The list of river names
    river_lis = []
    # The list of number of stations
    num_lis = []
    num_rivers = N
    for riv in stations:
        num_stations = 0
        if riv.river not in river_lis:
            for station in stations:
                if riv.river == station.river:
                    num_stations += 1
            rivers_station.append((riv.river, num_stations))
            river_lis.append(riv.river)
            num_lis.append(num_stations)
        else:
            pass

    rivers_station = sorted_by_key(rivers_station, 1, reverse=True)
    num_lis = sorted(num_lis, reverse=True)
    # check any other rivers with the same number of stations
    for index in (num_rivers, len(num_lis)):
        if num_lis[num_rivers-1] == num_lis[num_rivers]:
            num_rivers += 1
        else:
            break

    return rivers_station[:num_rivers]
