#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from urllib.parse import urlparse


def get_canonical_url(url):
    # return the host part of address
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri)


def filename_from_url(url):
    urlb64 = base64.encodebytes(bytes(url.encode()))
    return ".".join([(urlb64.decode()).strip("\n"), 'page'])


def url_from_filename(filename):
    url, _ = filename.split(".")
    return base64.decodebytes(url.encode()).decode()
