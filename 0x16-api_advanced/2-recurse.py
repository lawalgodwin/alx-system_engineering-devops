#!/usr/bin/python3
"""This module contains a function that recursively paginate listings"""

import requests


def recurse(subreddit, after_cursor=None, hot_list=[]):
    """Recursively paginate all hot posts"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after_cursor}
    headers = {'User-Agent': 'MyAPIConsumer/1.0 by lawalgodwin'}
    response = requests.get(
                            url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code >= 300:
        return None
    else:
        subreddit_info = response.json()
        posts = subreddit_info['data']['children']
        after_cursor = subreddit_info['data']['after']
        for post in posts:
            hot_list.append(post['data']['title'])
    if after_cursor:
        return recurse(subreddit, after_cursor=after_cursor, hot_list=hot_list)
    return hot_list
