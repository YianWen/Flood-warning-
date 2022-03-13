import datetime
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.utils import sorted_by_key

def test_call():
    stations = build_station_list()
    update_water_levels(stations)
    station_name = "Cam"
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break
    dt = 10
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    
    plot_water_levels(station_cam, dates, levels)