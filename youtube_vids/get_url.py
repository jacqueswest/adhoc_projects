#!/usr/bin/python

from json import loads
import requests

urls = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
print loads(urls.text)
