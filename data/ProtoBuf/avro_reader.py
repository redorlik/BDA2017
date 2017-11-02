from avro.datafile import DataFileReader
from avro.io import DatumReader

import sys,os

if __name__ == '__main__':
    f = open("trip.avro","rb")
    reader = DataFileReader(f,DatumReader())
    for gps in reader:
        print(gps)
