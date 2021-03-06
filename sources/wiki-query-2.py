# Copyright (C) 2015 Ben Lewis
# Licensed under the MIT license, see ../LICENSE

import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'links',
               'titles' : 'User:Zen-ben',
               'format' : 'json',
               'continue' : '' }

while True:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    for page in response['query']['pages']:
        for link in response['query']['pages'][page]['links']:
            print(link['title'])

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['plcontinue'] = response['continue']['plcontinue']
    else:
        break
