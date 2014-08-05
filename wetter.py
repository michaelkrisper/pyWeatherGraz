#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-08-06"
__version__ = "1.0"
__python_version__ = "2.7.6"

import urllib2
import re
html = urllib2.urlopen("http://www.wetter.at/wetter/oesterreich/steiermark/graz/prognose/24-stunden").read()
matches = re.findall('class="box">.*?<div.*?(\d+:\d+) Uhr.*?alt="(.*?)".*?"min">(\d+\xc2\xb0).*?Niederschlag: (.*? mm/h)', html, re.DOTALL)
for match in matches:
    print '{0:7}{2:6}{1}'.format(*match)