#!/usr/bin/python3
"""This module contains a function that gets
   the number of subscibers in a given redit
"""
import requests


def number_of_subscribers(subreddit):
    """Get the count of subscribers in the given subreddit"""
    headers = {'User-Agent': 'MyAPIConsumer/1.0 by lawalgodwin'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    subreddit_info = response.json()
    subscriber_count = subreddit_info['data']['subscribers']
    return subscriber_count
