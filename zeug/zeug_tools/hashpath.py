#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

__all__ = ['get_hash_path']


def get_object_hash(string_to_make_hash):
    # function creates sha3_512 hash from the string passed
    h = hashlib.sha256()
    h.update(bytes(string_to_make_hash.encode()))
    return h.hexdigest()


def get_hash_path(url):
    """
    - generate sha3_512 hash of the URL object (it will be his object)
    - take 5 characters of hash and make them subdirs
    - return hash
    
    five characters cause i want to have 34^6(1.5 mld) elements, before there will be 35 objects in 
    one of the nodes, from level 5(if I haven't made a mistake)
    """
    object_hash = get_object_hash(url)

    first_part = list(object_hash[0:5])
    first_part.append(object_hash)

    return "/".join(first_part)

