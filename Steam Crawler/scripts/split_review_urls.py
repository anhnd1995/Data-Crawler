"""
Load scraped product items into DataFrame, write review urls into N text files.

Run example:
    $ python split_review_urls.py \
        --scraped-products $(pwd)/../output/products_.jl \
        --output-dir $(pwd)/../output
"""
import argparse
import json
import math
import os
from random import shuffle

import numpy as np
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--scraped-products',
        help='$(pwd)/../Data-Crawler/output/products_all.jl'
    )
    parser.add_argument(
        '--output-dir',
        help='$(pwd)/../Data-Crawler/output'
    )
    parser.add_argument(
        '--pieces',
	help='1',
        default=10
    )
    return parser.parse_args()


def main():
    args = parse_args()
    fx = open('url.txt','a')
    
    with open('products_all.jl') as f:
        rows = [json.loads(l) for l in f]

    for i in rows:
	if 'user reviews' in i["sentiment"]
		fx.write('\n' + i["reviews_url"])

    fx.close()

if __name__ == "__main__":
    main()
