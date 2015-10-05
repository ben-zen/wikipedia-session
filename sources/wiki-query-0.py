# Copyright (C) 2015 Ben Lewis
# Licensed under the MIT license, see ../LICENSE

import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

wp_call = requests.get(ENDPOINT + '?'
                       + 'action=query&'
                       + 'prop=links&'
                       + 'titles=User:Zen-ben&'
                       + 'continue=&'
                       + 'format=json')

response = wp_call.json()

for page in response['query']['pages']:
    for link in response['query']['pages'][page]['links']:
        print(link['title'])
