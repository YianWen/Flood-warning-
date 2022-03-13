import datetime
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.utils import sorted_by_key


def run():
    stations = build_station_list()
    update_water_levels(stations)

    def score(val):
        risk = ''
        if val < 0.6:
            risk = 'low'
        elif 0.6 < val < 0.8:
            risk = 'moderate'
        elif 0.8 < val < 1:
            risk = 'high'
        else:
            risk = 'severe'
        return risk

    asssess = {'low': [], 'high': [], 'moderate': [], 'severe': []}
    for station in stations:
        if station.relative_water_level():
            risk = score(station.relative_water_level())
            asssess[risk].append(station.name)

    for risk in asssess.keys():
        print(risk)
        for station in asssess[risk]:
            print('\t\t{}'.format(station))


if __name__ == '__main__':
    run()
