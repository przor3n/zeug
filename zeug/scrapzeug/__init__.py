#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import logging

import datetime

import os
import requests

from zeug.zeug import Zeug
from zeug.zeug_tools.files import write_binary_file
from zeug.zeug_tools.hashpath import get_hash_path
from zeug.zeug_tools.url import get_canonical_url

__all__ = []

"""
This will be the SCRAPZEUG
"""

logging.basicConfig(filename='/home/red/WAREHOUSE/logs/zeug/scraper.log', level=logging.INFO)

class SCRAPZEUG(Zeug):

    def __init__(self):

        slots = {
            'name': type(self),
            'filename': lambda url: self.filename(url),
            'place' : lambda url: self.place(url),
            'save' : lambda content, address, file: self.save(content, address, file),
            'download': lambda url: requests.get(url),
            'log': lambda what, where, requester: logging.info("{}: {};TO: {}; WHEN: {}; FOR: {}", "scrapzeug", what, where, datetime.datetime.now().isoformat(), requester)
        }


        """
        The SCRAPZEUG will be doing:
        * generate address under which to put the url
        * generate filename under which it will be stored
            filename will be format: URL.content
        * fetches the URL to download
        * downloads it
        * (for now) extracts the content of request (it's binary)
        * saves the content under address as filename,
        * and lastly, send log that the page was downloaded
          and put under the address
          
        """
        inst = """\n
address = place(url)\n
file = filename(url)\n
request = download(url)\n
content = request.content\n
save(content, address, file)\n
log(url, address, 'kuku')\n 
"""

        super(SCRAPZEUG, self).__init__(slots=slots, instructions=inst)
        pass

    def prepare(self, url):
        self.slots['url'] = url
        self.environment['url'] = url

    def place(self, url):
        """
        This function generates the place where to put the
        contents.

        The generation is like this:
        - main part: /scrappings/
        - get canonical url: /scrappings/canonical/
        - generate OBJECT HASH dir part
        - add dir part to url
        - return content
        """
        url = [
            '/scrappings',
            get_canonical_url(url),
            get_hash_path(url)
        ]

        return "/".join(url)

    def save(self, content, address, file):
        """
        Here I will save the contents,
        under the address, with a file name.

        The address and file name will be contacated
        to a file path in the WAREHOUSE folder of the
        HOME directory.

        Content is binary so we will use binary write.
        """
        full_address = "/home/red/WAREHOUSE" + address
        file_path = full_address + "/" + file

        try:
            os.makedirs(full_address, 0o777, True)
        except OSError:
            pass

        write_binary_file(content, file_path)

    def filename(self, url):
        urlb64 = base64.encodebytes(bytes(url.encode()))
        return ".".join([urlb64.decode(), 'content'])

if __name__ == "__main__":
    url = "http://www.onet.pl"

    scrapzeug = SCRAPZEUG()
    scrapzeug.prepare(url)
    scrapzeug.do()
