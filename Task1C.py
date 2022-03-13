from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    list_needed = []
    stations = build_station_list()
    list_needed = stations_within_radius(stations, (52.2053, 0.1218), 10)
    print("stations within 10km")
    print(list_needed)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
