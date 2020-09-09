#!/usr/bin/python3
from urllib.request import urlopen, Request
import re

page = urlopen('http://olympus.realpython.org/profiles/dionysus').read().decode('utf-8')
start_name = page.find('Name: ') + len('Name: ')
end_name = page.find('</h2>')
strat_color = page.find('Favorite Color: ') + len('Favorite Color: ')
end_color = page.find('</center>')
print(page[start_name:end_name] + '\n' + page[strat_color:end_color - 1])

html_text = urlopen('http://olympus.realpython.org/profiles/dionysus').read().decode('utf-8')
for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)