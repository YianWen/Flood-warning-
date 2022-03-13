from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    list = []
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_level_over_threshold(stations, 0.8)
    for i in range(len(list)):
        print(list[i][0], list[i][1])
    

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()