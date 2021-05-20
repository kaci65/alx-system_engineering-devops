#!/usr/bin/python3
"""
query the Reddit API and return number of subscribers (not 
active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""
    listing = 'about'
    url = f'https://www.reddit.com/r/{subreddit}/{listing}.json'
    req = requests.get(url, headers = {'User-Agent': 'X-Modhash'},
                       allow_redirects=False)
    if req.status_code == 300 or req.status_code == 404:
        return 0
    subs = req.json()
    return subs['data']['subscribers']
