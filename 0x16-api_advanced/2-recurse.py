#!/usr/bin/python3
"""
recursive function that queries Reddit API and returns list containing
titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """return list of titles in hot articles"""
    sort = 'hot'
    params = {'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/{sort}.json'
    req = requests.get(url, headers = {'User-Agent': 'X-Modhash'},
                       params=params,
                       allow_redirects=False)
    if req.status_code == 300 or req.status_code == 404:
            return None
    for post in req.json()['data']['children']:
        hot_list.append(post['data']['title'])
    after_param = req.json()['data']['after']
    if after_param is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after_param)
