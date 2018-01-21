# -*- coding: utf-8 -*-
import fiona
from tqdm import tqdm
import click

from coord_convert.utils import Transform


def recur_map(f, data):
    """递归处理所有坐标
    
    Arguments:
        f {function} -- [apply function]
        data {collection} -- [fiona collection]
    """

    return[ not type(x) is list and f(x) or recur_map(f, x) for x in data ]


@click.command()
@click.argument('src_path', type=click.Path(exists=True))
@click.argument('dst_path', type=click.Path(exists=False))
@click.argument('convert_type', type=click.STRING)
def convertor(src_path, dst_path, convert_type):
    """convert input china coordinate to another. 

\b
    Arguments:  

\b
        src_path {string} -- [source file path]  
        dst_path {string} -- [destination file path]  
        convert_type {string} -- [coordinate convert type, e.g. wgs2bd]   

\b
            there are six convert type:   
            wgs2gcj : convert WGS-84 to GCJ-02
            wgs2bd  : convert WGS-84 to DB-09  
            gcj2wgs : convert GCJ-02 to WGS-84  
            gcj2bd  : convert GCJ-02 to BD-09  
            bd2wgs  : convert BD-09 to WGS-84  
            bd2gcj  : convert BD-09 to GCJ-02 

    Example:

\b 
        coord_covert ./test/data/line/multi-polygon.shp ~/temp/qqqq.shp wgs2gcj
    """ 

    with fiona.open(src_path, 'r', encoding='utf-8') as source:
        source_schema = source.schema.copy()
        with fiona.open(dst_path, 'w', encoding='utf-8', **source.meta) as out:
            transform = Transform()
            f = lambda x: getattr(transform, convert_type)(x[0], x[1])  #dynamic call convert func

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
#     dst_path = './test/data/point_gcj.shp'
#     converter(point_path, dst_path, 'wgs2gcj')
#     converter(line_path, dst_path, 'wgs2gcj')
#     converter(poylygon_path, dst_path, 'wgs2gcj')



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
