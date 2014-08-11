# -*- coding: utf-8 -*-
import urllib2
import re

url = "http://warnungen.zamg.at/html/en/today/thunderstorm/at/steiermark/graz_stadt/graz/"
html = urllib2.urlopen(url).read()
matches = re.findall("(?:title=\")(\d\d:\d\d) - \d\d:\d\d.*?\"><span class=\"ntxt\">(\d*?)</span></td>", html, re.DOTALL)

title = "Wetterwarnung für Graz:"
print("%s\n%s" % (title, "-"*len(title)))
weathertext = ["",
               "Potentially dangerous. (Thunderstorms)",
               "Dangerous. (Heavy Thunderstorm, Strong Winds)",
               "Very dangerous. (Orcans, Taifuns, Blizzards)"]
print("\n".join([m[0] + ": " + weathertext[int(m[1])] for m in matches]))