from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    list_we_need = []
    list = build_station_list()
    list_we_need = rivers_with_station(list)
    print(len(list_we_need), "First 10 rivers: ", list_we_need[:10])

    other_we_need = {}
    other_we_need = stations_by_river(list)
    print(other_we_need['River Aire'])
    print(other_we_need['River Cam'])
    print(other_we_need['River Thames'])
    


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()