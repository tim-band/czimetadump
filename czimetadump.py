#! /usr/bin/env python3
from aicspylibczi import CziFile
import argparse
from sys import stdout
from xml import etree as etree

def dump(path_in):
    czi = CziFile(path_in)
    print(etree.ElementTree.tostring(
        czi.meta, encoding='utf-8'
    ).decode('unicode-escape'))

parser = argparse.ArgumentParser(
    description= 'CZI metadata dumper'
)
parser.add_argument(
    'czifile',
    help='input CZI file to dump',
    metavar='CZI-FILE'
)
options = parser.parse_args()

dump(getattr(options, 'czifile'))
