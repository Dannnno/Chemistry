# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import os
from collections import deque


endings = ['.pyc']


def extract_files(start_dir=os.getcwd(), excludes=[]):
    to_crawl = deque([filename
                      for filename in os.listdir(start_dir)
                      if not filename.startswith('.') and
                      not filename in excludes])
    extracted = set()

    while to_crawl:
        current = to_crawl.popleft()

        if current in extracted:
            continue

        if os.path.isdir(current):
            to_crawl.extendleft(
                map(lambda x: os.path.join('', current, x),
                    extract_files(os.path.join(start_dir, current))))
            continue

        extracted.add(current)

    return filter(lambda x: any(x.endswith(i) for i in endings), extracted)


def delete_files(files):
    map(os.remove, files)


def make_clean(*except_):
    delete_files(extract_files(excludes=except_))


if __name__ == '__main__':
    make_clean()
