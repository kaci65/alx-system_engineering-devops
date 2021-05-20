#!/usr/bin/python3
"""
queries the Reddit API and prints titles of first 10 hot posts listed
for a given subreddit
"""

import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts"""
    sort = 'hot'
    limit = 10
    url = 'https://www.reddit.com/r/{}/{}.json?limit={}'.format(subreddit,
                                                                sort, limit)
    req = requests.get(url, headers={'User-Agent': 'X-Modhash'},
                       allow_redirects=False)
    if req.status_code == 300 or req.status_code == 404:
        print('None')
    for post in req.json()['data']['children']:
        print(post['data']['title'])
