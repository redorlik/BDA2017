import GPS_pb2 as pb
from hypothesis import given
from hypothesis.strategies import integers,floats,dates,datetimes

def gen_gps(gps,s,lat,lon,d,sat):

    gps.speed = s
    gps.latitude = lat
    gps.longitude = lon
    gps.date = str(d)
    gps.satellites = sat

@given(s=floats(min_value=0,max_value=330),lat=floats(min_value=-90,max_value=90),
    lon=floats(min_value=-180,max_value=180),d=dates(),
    sat=integers(min_value=0,max_value=24))
def test_gps(s,lat,lon,d,sat):
    gps = pb.GPS()
    gen_gps(gps,s,lat,lon,d,sat)
    gps2 = pb.GPS()
    gps2.ParseFromString(gps.SerializeToString())
    assert gps2.speed == gps.speed
    assert gps2.satellites == gps.satellites
    assert gps2.latitude == gps.latitude
    assert gps2.longitude == gps.longitude
    assert gps2.date == gps.date
    gps2.satellites = gps.satellites+1
    assert gps2 == gps

@given(s=floats(min_value=0,max_value=330),lat=floats(min_value=-90,max_value=90),
    lon=floats(min_value=-180,max_value=180),d=datetimes(),
    sat=integers(min_value=0,max_value=24))
def test_trip(s,lat,lon,d,sat):
    trip = pb.Trip()
    for i in range(10):
        gen_gps(trip.locations.add(),s,lat,lon,d,sat)
    trip2 = pb.Trip()
    trip2.ParseFromString(trip.SerializeToString())
    #gen_gps(trip2.locations.add(),s,lat,lon,d,sat)
    assert trip2 == trip
