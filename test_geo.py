from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import random
from haversine import haversine
from floodsystem.station import MonitoringStation

'''
Tests to see if all values are smaller than the next one in list
'''
def test_geo_list():
    stations = build_station_list()
    assert stations != None
    p = (random.randint(0,5), random.randint(0,5))
    assert p != None
    station_list=stations_by_distance(stations, p)
    for i in range (0, (len(station_list)-2)):
        stat1=station_list[i]
        stat2=station_list[i+1]
        stat1=stat1[1]
        stat2=stat2[1]
        assert stat1<=stat2

'''
Tests to see if station within radius is classed as within radius
'''

def test_geo_rad():
    coord1 = (9.9, 9.9)
    coord2 = (10,10)
    stat = "stat"
    measure = "measure"
    name = "label"
    trange = None
    river = "River"
    town = "Town"
    center = (0,0)

    s1 = MonitoringStation(stat, measure, name, coord1, trange,
                 river, town)
    s2 = MonitoringStation(stat, measure, name, coord2, trange,
                 river, town)
    stations=[s1,s2]
    rad = haversine(center, coord1)+1
    radius = stations_within_radius(stations, center, rad)
    assert len(radius) == 1
    assert radius[0][0] == s1

'''
Tests to see if both types of invalid range data is flagged as so
'''

def test_validity_valuation():
    coord1 = (9.9, 9.9)
    coord2 = (10,10)
    stat = "stat"
    measure = "measure"
    name = "label"
    trange1 = (10,9)
    trange2 = None
    river = "River"
    town = "Town"
    center = (0,0)

    s1 = MonitoringStation(stat, measure, name, coord1, trange1,
                 river, town)
    s2 = MonitoringStation(stat, measure, name, coord2, trange2,
                 river, town)
    stations=[s1,s2]

    assert s1.typical_range_consistent() == False
    assert s2.typical_range_consistent() == False





test_geo_list()
test_geo_rad()
test_validity_valuation()