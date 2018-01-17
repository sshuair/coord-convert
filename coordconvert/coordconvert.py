# -*- coding: utf-8 -*-
import fiona
import utils
import pprint
from tqdm import tqdm

import datetime
import logging
import sys
from utils import Transform


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def point_convert(collections, convert_type):
    transform = Transform()
    for fea in collections:
        coords = fea['geometry']['coordinates']
        fea['geometry']['coordinates'] = getattr(transform, convert_type)(coords[0], coords[1])
    return collections

def line_convert(collections, convert_type):
    pass

def converter(in_path, out_path, convert_type):
    with fiona.open(in_path, 'r', encoding='utf-8') as source:
        source_schema = source.schema.copy()
        with fiona.open(out_path, 'w', encoding='utf-8', **source.meta) as target:
            assert source_schema['geometry'] in ('Point', 'LineString', 'Polygon')
            if source_schema['geometry'] == 'Point':
                converted_collection = point_convert(list(source), convert_type)
                for fea in tqdm(converted_collection):
                    target.write(fea)

            elif source_schema['geometry'] == 'LineString':
                for f in source:
                    coords = f['geometry']['coordinates']
                    pass
            # elif source_schema['geometry'] == 'Polygon':
            #     for f in source:
            #         f['geometry']['coordinates']

point_path = './test/data/point/point.shp'
# line_path = './test/data/line/polyline.shp'
out_path = './test/data/point_gcj.shp'
converter(point_path, out_path, 'wgs2gcj')



# def signed_area(coords):
#     """Return the signed area enclosed by a ring using the linear time
#     algorithm at http://www.cgafaq.info/wiki/Polygon_Area. A value >= 0
#     indicates a counter-clockwise oriented ring.
#     """
#     xs, ys = map(list, zip(*coords))
#     xs.append(xs[1])
#     ys.append(ys[1])
#     return sum(xs[i]*(ys[i+1]-ys[i-1]) for i in range(1, len(coords)))/2.0

# with fiona.open('./test/data/point/point.shp', 'r') as source:

#     # Copy the source schema and add two new properties.
#     sink_schema = source.schema.copy()
#     sink_schema['properties']['s_area'] = 'float'
#     sink_schema['properties']['timestamp'] = 'datetime'

#     # Create a sink for processed features with the same format and
#     # coordinate reference system as the source.
#     with fiona.open('oriented-ccw.shp', 'w',crs=source.crs, driver=source.driver,schema=sink_schema,) as sink:
#         for f in source:
#             g = f['geometry']
#             assert g['type'] == "Polygon"
#             rings = g['coordinates']
#             sa = sum(signed_area(r) for r in rings)
#             if sa < 0.0:
#                 rings = [r[::-1] for r in rings]
#                 g['coordinates'] = rings
#                 f['geometry'] = g

#             # Add the signed area of the polygon and a timestamp
#             # to the feature properties map.
#             f['properties'].update(
#                 s_area=sa,
#                 timestamp=datetime.datetime.now().isoformat() )

#             sink.write(f)


        # The sink file is written to disk and closed when its block ends.