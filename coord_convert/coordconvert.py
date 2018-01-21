# -*- coding: utf-8 -*-
import fiona
from tqdm import tqdm

import click

from coordconvert.utils import Transform


def recur_map(f, data):
    return[ not type(x) is list and f(x) or recur_map(f, x) for x in data ]


@click.command()
@click.argument('src_path', type=click.Path(exists=True))
@click.argument('dst_path', type=click.Path(exists=False))
@click.argument('convert_type', type=click.STRING)
def converter(in_path, out_path, convert_type):
    """convert input 
    
    Arguments:
        in_path {} -- [description]
        out_path {[type]} -- [description]
        convert_type {[type]} -- [description]
    
    Raises:
        TypeError -- [description]
    
    Returns:
        [type] -- [description]
    """ 

    with fiona.open(in_path, 'r', encoding='utf-8') as source:
        source_schema = source.schema.copy()
        with fiona.open(out_path, 'w', encoding='utf-8', **source.meta) as out:
            transform = Transform()
            f = lambda x: getattr(transform, convert_type)(x[0], x[1])

            for fea in tqdm(source):
                collections = fea['geometry']['coordinates']
                if type(collections) is tuple:
                    fea['geometry']['coordinates'] = f(collections)
                elif type(collections) is list:
                    fea['geometry']['coordinates'] = recur_map(f, collections)
                else:
                    raise TypeError("collection must be list or tuple")
                out.write(fea)



# if __name__ == '__main__':
#     converter()

#     point_path = './test/data/point/point.shp'
#     line_path = './test/data/line/polyline.shp'
#     poylygon_path = './test/data/polygon/polygon-2.shp'
#     out_path = './test/data/point_gcj.shp'
#     converter(point_path, out_path, 'wgs2gcj')
#     converter(line_path, out_path, 'wgs2gcj')
#     converter(poylygon_path, out_path, 'wgs2gcj')



            # return collections
            
            # for f

            # assert source_schema['geometry'] in ('Point', 'LineString', 'Polygon')

            # if source_schema['geometry'] == 'Point':
            #     converted_collection = point_convert(list(source), convert_type)
            #     for fea in tqdm(converted_collection):
            #         target.write(fea)
            # elif source_schema['geometry'] == 'LineString':
            #     converted_collection = linestring_convert(list(source), convert_type)
            #     for fea in tqdm(converted_collection):
            #         target.write(fea)
            # elif source_schema['geometry'] == 'Polygon':
            #     converted_collection = polygon_convert(list(source), convert_type)
            #     for fea in tqdm(converted_collection):
            #         target.write(fea)
            # elif source_schema['geometry'] == 'Polygon':
            #     for f in source:
            #         f['geometry']['coordinates']
