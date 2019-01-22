#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from codelib.files.read_write import get_file_contents
from codelib.files.storage import WAREHOUSE

from zeug.zeug_tools.logs import ACTIONS, log, error


def parse_sitemap_xml(file, destination):
    """ParserZeug
    Get file contents.
    Load them to BeautifulSoup
    Extract data and save them to file.
    """
    contents = get_file_contents(file)

    page = BeautifulSoup(contents, "html.parser")
    contents = [tag.text for tag in page.find_all('loc')]
    if contents:
        WAREHOUSE.store("\n".join(contents), destination)
        log(ACTIONS.PARSE_SITEMAP_XML, file, destination)
    else:
        error(ACTIONS.PARSE_SITEMAP_XML, file)


if __name__ == "__main__":
    file = "/home/red/WAREHOUSE/zeug/case-wykop/sitemaps/a/H/R/0/c/H/M6Ly93d3cud3lrb3AucGwvc2l0ZW1hcC54bWw=.page"  # noqa
    destination = 'zeug/case-wykop/sitemap-links/main'
    parse_sitemap_xml(file, destination)
