import pytest
from coord_convert.transform import wgs2gcj, wgs2bd, gcj2wgs, gcj2bd, bd2wgs, bd2gcj
from coord_convert.transform import Transform

lon, lat = 120.0, 40.0

def test_gcj_wgs():
    forward_lon, forward_lat = wgs2gcj(lon, lat)
    assert isinstance(forward_lon, float)
    assert isinstance(forward_lat, float)

    reversed_lon, reversed_lat = gcj2wgs(forward_lon, forward_lat)
    assert round(reversed_lon, 6) == lon
    assert round(reversed_lat, 6) == lat


def test_gcj_bd():
    forward_lon, forward_lat = gcj2bd(lon, lat)
    assert isinstance(forward_lon, float)
    assert isinstance(forward_lat, float)

    reversed_lon, reversed_lat = bd2gcj(forward_lon, forward_lat)
    assert round(reversed_lon, 6) == lon
    assert round(reversed_lat, 6) == lat


def test_wgs_bd():
    forward_lon, forward_lat = wgs2bd(lon, lat)
    assert isinstance(forward_lon, float)
    assert isinstance(forward_lat, float)

    reversed_lon, reversed_lat = bd2wgs(forward_lon, forward_lat)
    assert round(reversed_lon, 6) == lon
    assert round(reversed_lat, 6) == lat

def test_Transform():
    transform = Transform()
    forward_lon, forward_lat = getattr(transform, 'wgs2gcj')(lon, lat)
    reversed_lon, reversed_lat = getattr(transform, 'gcj2wgs')(forward_lon, forward_lat)
    assert round(reversed_lon, 6) == lon
    assert round(reversed_lat, 6) == lat

    forward_lon, forward_lat = getattr(transform, 'wgs2bd')(lon, lat)
    reversed_lon, reversed_lat = getattr(transform, 'bd2wgs')(forward_lon, forward_lat)
    assert round(reversed_lon, 6) == lon
    assert round(reversed_lat, 6) == lat

    forward_lon, forward_lat = getattr(transform, 'gcj2bd')(lon, lat)
    reversed_lon, reversed_lat = getattr(transform, 'bd2gcj')(forward_lon, forward_lat)
    assert round(reversed_lon, 6) == lon
    assert round(reversed_lat, 6) == lat