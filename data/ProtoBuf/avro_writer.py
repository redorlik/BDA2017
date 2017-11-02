import avro
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

import datetime
import sys,os

schema_trip = '''{"namespace":"bda2017.trip",
                    "type": "record",
                     "name": "Trip",
                     "fields": [
                         {"name": "date", "type":"long","logicalType": "timestamp-micros"},
                         {"name": "speed",  "type": ["float", "null"]},
                         {"name": "latitude", "type": "float"},
                         {"name": "longitude", "type": "float"},
                         {"name": "satellites", "type": "int"}
 ]
}'''

def writer(f,dat):
    schema = avro.schema.Parse(schema_trip)

    writer = DataFileWriter(f,DatumWriter(),schema)
    writer.append(dat)
    writer.close()

if __name__ == '__main__':
    dat = {"date":int(datetime.datetime.now().timestamp()*10**6),"latitude":9.899,
                      "longitude":57.9090,"speed":2.5,"satellites":8}
    f = open("trip.avro","wb")
    writer(f,dat)
    f.close()
