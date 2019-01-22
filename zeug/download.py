#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from codelib.files.storage import WAREHOUSE
from codelib.files.system import connect_paths

from zeug.zeug_tools.files import path_from_hash_filename
from zeug.zeug_tools.logs import log, error, ACTIONS
from zeug.zeug_tools.url import filename_from_url


def build_filepath(base, url):
    return connect_paths(base, path_from_hash_filename(filename_from_url(url)))


def download(url, destination_dir):
    """Download

    Get an url and download page in
    given location. Return the name
    """
    r = requests.get(url)
    filepath = build_filepath(destination_dir, url)

    if r.status_code == requests.codes.ok:
        WAREHOUSE.store(r.text, filepath)
        log(ACTIONS.DOWNLOAD, url, WAREHOUSE.prefix_path(filepath))
    else:
        error(ACTIONS.DOWNLOAD, url)
        return False

    return WAREHOUSE.prefix_path(filepath)


if __name__ == '__main__':
    dest_dir = "zeug/case-wykop/sitemaps"
    url = "https://www.wykop.pl/sitemap.xml"

    download(url, dest_dir)
