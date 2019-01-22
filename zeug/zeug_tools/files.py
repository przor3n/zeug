#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv


def read_csv(file):
    with open(file, 'r') as f:
        return list(csv.reader(f, delimiter=';'))


def write_csv(content, file):
    with open(file, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        for row in content:
            writer.writerow(row)


def write_binary_file(contents, file_name):
    with open(file_name, 'wb') as f:
        f.write(contents)


def path_from_hash_filename(filename):
    """ What it does:
    - filename is a hash filename: aHR0cDovL3d3d3cud3lrb3AucGw=.page or
    md5 hash or any other alfanum hash
    - take 7 characters of hash and separate them with "/"
    - add rest of the string
    - return path that was created, that looks like:
    a/H/R/0/c/D/ovL3d3d3cud3lrb3AucGw=.page

    This gives me this:
    <alphanum>/<alphanum>/<alphanum>/<alphanum>/<alphanum>/<alphanum>/


    Six characters, in an alphanum set of characters give me 36^6(~2 mld)
    elements as leaf nodes of a, before there will be 36 objects in all of the nodes. this allowes
    me to
    """
    return (filename[:7]).replace("", "/").strip("/") + filename[7:]
