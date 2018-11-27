#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urlparse

__all__ = ['get_canonical_url']

def get_canonical_url(url):
    # return the host part of address
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri)

