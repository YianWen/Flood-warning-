from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level


list = build_station_list()
update_water_levels(list) 

def no_none_test():
    set = []
    set = stations_level_over_threshold(list, 0.8)
    for i in range(len(set)):
        assert set[i][1] != None
    
def correct_length():
    x = []
    x = stations_highest_rel_level(list, 20)
    assert len(x) == 20

def cmon():
    assert True == False