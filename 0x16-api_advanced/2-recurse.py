#!/usr/bin/python3
"""Consuming Reddit API"""

import requests
import sys


def recurse(subreddit, after='', hot_list=[]):
    """return paginated hot list"""
    headers = {"User-Agent": "MyAPIConsumer/2.0"}
    p = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    res = requests.get(url, headers=headers, params=p, allow_redirects=False)
    if res.status_code > 299:
        return None
    else:
        posts = res.json()['data']['children']
        after = res.json()['data']['after']
        for post in posts:
            hot_list.append(post['data'].get('title'))
    if (after):
        return recurse(subreddit, after=after, hot_list=hot_list)
    return hot_list
