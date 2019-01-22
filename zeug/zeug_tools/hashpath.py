#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib


def get_object_hash(object):
    # function creates md5 hash from the string passed
    h = hashlib.md5()
    h.update(bytes(object.encode()))
    return h.hexdigest()
