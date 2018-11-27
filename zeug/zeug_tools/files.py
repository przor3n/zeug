#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

__all__ = []

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