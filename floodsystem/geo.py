
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    distances = []
    for station in stations:
        cdist = haversine(station.coord, p)
        distances.append((station, cdist))
    distances=sorted_by_key(distances, 1)
    return distances
