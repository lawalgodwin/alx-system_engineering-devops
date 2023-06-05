#!/usr/bin/python3
"""A script that fetches the first ten hot posts in
in a reddit subredit
Requirment:
* If not a valid subreddit, print None.
* Invalid subreddits may return a redirect to search results.
  Ensure that you are not following redirects.
"""
import requests


def top_ten(subreddit):
    """Print the title of the first 10 hot posts in the given
    subreddit
    """
    baseUrl = 'https://www.reddit.com/r/'
    url = baseUrl + subreddit + '/hot.json?limit=10'
    headers = {"User-Agent": "MyApiClient/4.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        topTenPosts = response.json().get("data").get('children')
        [print("{}".format(post['data'].get('title'))) for post in topTenPosts]
    else:
        print('None')
