# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

list = build_station_list()

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

# To check the stations have inconsistent data
def test_consistent():
    inconsistent = True
    for station in list:
        if station.name == 'Airmyn':
            consistent_bool = station.typical_range_consistent()
            if consistent_bool != False:
                inconsistent = False
    assert inconsistent == True

# Same method in test_geo.py to check the alphabetical order
def test_alphabetical():
    fingers_crossed = True
    station_names = inconsistent_typical_range_stations(list)
    check_sort = [station_names[i] for i in range(len(station_names))]
    check_sort.sort()
    for i in range(len(station_names)):
        if (check_sort[i] != station_names[i]):
            fingers_crossed = False
    assert fingers_crossed == True







