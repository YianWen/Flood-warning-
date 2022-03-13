import datetime
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.utils import sorted_by_key

def run():
    list = []
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.latest_level and station.measure_id != None:
            list += station.measure_id, station.latest_level
            tuple_data = [x for x in zip(*[iter(list)]*2)]
    tuple_data = sorted_by_key(tuple_data, 1, reverse = True)          
    IDs = []
    IDs = tuple_data[:10]
    for i in range(len(IDs)):
        dt = 10
        dates, levels = fetch_measure_levels(IDs[i][0], dt=datetime.timedelta(days=dt))
        for n in stations:
            if n.measure_id == IDs[i][0]:
                station = n
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
