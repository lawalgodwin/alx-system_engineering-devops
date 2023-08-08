#!/usr/bin/python3
"""This module contains a function that fetches first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Fetch first 10 hot post"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    headers = {'User-Agent': 'MyAPIConsumer/1.0 by lawalgodwin'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code >= 300:
        print('None')
    else:
        subreddit_info = response.json()
        topTenHotPosts = subreddit_info['data']['children']
        for post in topTenHotPosts:
            print(post['data']['title'])
