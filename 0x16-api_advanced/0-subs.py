#!/usr/bin/python3
"""A script that queries the reddit api
   and returns the total number of subscribers to a
   particular subreddit/community
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """return the number of subscriber on the subreddit"""
    baseUrl = 'https://www.reddit.com/r'
    subredditUrl = "{}/{}/about.json".format(baseUrl, subreddit)
    request_headers = {"User-Agent": "MyAPIClient/5.0"}
    response = requests.get(
             subredditUrl,
             headers=request_headers,
             allow_redirects=False)
    if response.status_code == 404:
        return 0
    return (response.json().get('data').get('subscribers'))
