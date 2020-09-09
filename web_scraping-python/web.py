#!/usr/bin/python3
from urllib.request import urlopen, Request
import re

# datos = urlopen('http://olympus.realpython.org/profiles/aphrodite').read().decode("utf-8")
# start_title = datos.find("<title>") + len('<title>')
# end_title = datos.find('</title>')
# print(datos[start_title:end_title])

# new = urlopen('http://olympus.realpython.org/profiles/poseidon').read().decode("utf-8")
# strat_title_new = new.find('<title >') + len('<title >')
# end_title_new = new.find('</title>')
# print(new[strat_title_new:end_title_new])


print(re.findall("ab*c", "holaabbbc"))
page = urlopen('http://olympus.realpython.org/profiles/dionysus').read().decode('utf-8')

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, page, re.IGNORECASE)
print(match_results)
title = match_results.group()
print(title)
title = re.sub("<.*?>", "", title)
print(title)