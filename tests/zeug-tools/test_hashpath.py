#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zeug.zeug_tools.hashpath import get_object_hash

__all__ = []


def test_get_object_hash():
    urls = [
        'http://www.onet.pl',
        'https://www.google.pl',
        'ala ma kota, a kot jest glodny'
    ]

    hashes = [
        'afc4901889a95cc63e87cab81e8b19e6dcfacd68109df16d1ec7db8ce57b9b8279c1a1481610e1dd0b7f014183b46083f1302cea67f17fd661b98008b71d17a5',
        'e74fc8c33fe25d370b2ec2ffb3bdd7b7d4986d1167d61170f774aae493bc8df3de6e7cd79aab6b33e2c1f232f4a202fa01bbdcabb01cb95f7d9db9d8870f365e',
        'a7cc4a478180d6742c4fd459565a4b7d7d6145e4b813d3e7c71651ca6d4bf14c6c7e17f3fc8f50049fa9b27b6aef4f58a1ae128aac5d89d074dc8a69301d5bba']

    for value, response in dict(zip(urls, hashes)).items():
        assert response == get_object_hash(value)
