#!/usr/bin/env python
# coding=utf-8

import urllib2
import json
import sys

ip_api = urllib2.urlopen(r'http://ip-api.com/json')

ijson = json.loads(ip_api.read())

print ijson[sys.argv[1]]