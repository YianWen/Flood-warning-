from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # I'm assuming this wanted the hight currently above the maximum typical range?
    list = []
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_highest_rel_level(stations, 10)
    for i in range(len(list)):
        print(list[i][0], list[i][1])

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()