#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import os

from zeug.download import download, build_filepath
from zeug.sitemap_parser import parse_sitemap_xml
from zeug.zeug_tools.logs import log, ACTIONS


def get_file_generator(path):
    """Get a file generator
    That will yield a file line
    """
    with open(path, "r") as file:
        for line in file:
            yield line


def multiplexer(file):
    """Multiplexer
    This will open file using file que.
    and then process file line by line.
    Then I will download it, and store
    after that parse out the links
    """
    sitemap_destination = 'zeug/case-wykop/sitemap-links'
    pagelinks_destination = 'zeug/case-wykop/page-links'

    for line in get_file_generator(file):
        url = download(line.strip(), sitemap_destination)

        filepath = build_filepath(pagelinks_destination, os.path.basename(url))

        parse_sitemap_xml(url, filepath)
        log(ACTIONS.DOWNLOAD_PARSE, line, filepath)
        sleep(1)


if __name__ == "__main__":
    file = '/home/red/WAREHOUSE/zeug/case-wykop/sitemap-links/main'
    multiplexer(file)
