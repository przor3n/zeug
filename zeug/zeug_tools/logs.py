#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import datetime

logger = logging.getLogger('zeugs')
logger.setLevel(logging.INFO)


class ACTIONS:
    PARSE_SITEMAP_XML = "PARSE_SITEMAP_XML"
    DOWNLOAD = "DOWNLOAD"
    DOWNLOAD_PARSE = "DOWNLOAD AND PARSE"


def log(action, what, where):
    response = "{}: {}, OF: {}, TO: {}".format(
        action,
        datetime.datetime.now().isoformat(),
        what,
        where)
    logger.info(response)
    # print(response)


def error(action, what):
    logger.error("{}: {}, OF: {}".format(action,
                                         datetime.datetime.now().isoformat(),
                                         what))
