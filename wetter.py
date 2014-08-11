#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script for displaying the weather data (datasource: www.wetter.at)
Usage:

1) Without Arguments: "python wetter.py"
   This displays the weather data for "Graz" (Styria)

2) With Arguments: "python wetter.py feldbach"
   Displays the weather data for the given argument (feldbach in this case).
   If there are more than one locations, the script will display the location names
   and asks the user to choose one by entering a number. When nothing is entered the script exits.
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__created_on__ = "2014-08-06"
__changed_on__ = "2014-08-12"
__version__ = "1.1"
__python_version__ = "2.7.6"

import urllib2
import re
import sys

# default location
locations = [("http://www.wetter.at/wetter/oesterreich/steiermark/graz", "Graz")]
nr = 0

if len(sys.argv) > 1:
	loc = " ".join(sys.argv[1:])
	html_location = urllib2.urlopen("http://www.wetter.at/locationSearch/%s" % urllib2.quote(loc)).read()
	locations = re.findall(r'<a href="(http://www.wetter.at/wetter/oesterreich/[\w-]+/[\w-]+)">\W+(.+?)\W+</a>', html_location, re.DOTALL)
	if len(locations) > 1:
		print "Choose location:"
		print "\n".join("%d: %s" % (i, m[1]) for i,m in enumerate(locations))
		nr = None
		while nr == None:
		    try:
		    	text = raw_input("Enter a location number: ")
		    	if text == "":
		    		sys.exit()
		        nr = int(text)
		        if not (0 <= nr < len(locations)):
		            raise ValueError
		    except ValueError:
		        print "error, try again"
		   # except:
		    #	sys.exit()

print "PROGNOSIS FOR %s:" % locations[nr][1]

html = urllib2.urlopen("%s/prognose/9-tage" % locations[nr][0]).read()
matches = re.findall('class="box">\W+?<div.*?(\w+?, \d+\.\d+\.).*?alt="(.*?)".*?"min">(\d+\xc2\xb0).*?Niederschlag: (.*? mm/h)', html, re.DOTALL)
print "NEXT 9 DAYS:"
for match in matches:
    print '{0:12}{2:5}{3: >11}  {1}'.format(*match)
print "-"*80

html = urllib2.urlopen("%s/prognose/24-stunden" % locations[nr][0]).read()
matches = re.findall('class="box">\W+?<div.*?(\d+:\d+) Uhr.*?alt="(.*?)".*?"min">(\d+\xc2\xb0).*?Niederschlag: (.*? mm/h)', html, re.DOTALL)
print "NEXT 24 HOURS:"
for match in matches:
    print '{0:7}{2:5}{3: >11}  {1}'.format(*match)


