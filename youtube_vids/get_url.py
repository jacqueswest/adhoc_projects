#!/usr/bin/python

from json import loads, dumps
import requests

top_rated = "http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc"

def get_youtube_urls(search_url):
    ''' Returns a list of top rated youtube urls in json format '''
    urls = requests.get(search_url)
    if urls.status_code != 200:
        print "No results found with error code %s" % urls.status_code
        sys.exit(-1)
    return urls.json()

def videos_list(data):
    ''' return a list of urls '''
    videos_dict = {"videos":{}}
    for item in data['data']['items']:
        videos_dict['videos'].update({item['id']:{}})
        videos_dict['videos'][item['id']].update({'title': item['title']})
        videos_dict['videos'][item['id']].update({'url': item['player']['default']})
    return dumps(videos_dict)

data = get_youtube_urls(top_rated)

videos_dict = {"videos":{}}
print videos_list(data)


