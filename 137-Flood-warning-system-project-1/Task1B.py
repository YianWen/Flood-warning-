
from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance


def run():
    list_needed = ()
    stations = build_station_list()
    list_needed = station_by_distance(stations, (53,22))
    print("CLOSEST 10 STATIONS: \n")
    print(list_needed[:10])
    print("FURTHEST 10 STATIONS: \n")
    print(list_needed[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
