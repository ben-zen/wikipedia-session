# Autumn 2015 sources, the end product.

import requests

ENDPOINT = "https://en.wikipedia.org/w/api.php"

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Python (programming language)',
               'rvlimit' : 100,
               'rvprop' : 'timestamp|user',
               'format' : 'json',
               'continue' : '' }

logged_in_editors = {}
anon_editors = {}
counter = 0
done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()
    print ("iteration {0}".format(counter))
    for page in response['query']['pages']:
        if 'revisions' in response['query']['pages'][page]:
            for rev in response['query']['pages'][page]['revisions']:
                if 'anon' in rev:
                    if rev['user'] in anon_editors:
                        anon_editors[rev['user']] += 1
                    else:
                        anon_editors[rev['user']] = 1
                else:
                    if rev['user'] in logged_in_editors:
                        logged_in_editors[rev['user']] += 1
                    else:
                        logged_in_editors[rev['user']] = 1

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True
    counter += 1

print("Anonymous editors:")
print(anon_editors)
print("Logged in editors:")
print(logged_in_editors)
