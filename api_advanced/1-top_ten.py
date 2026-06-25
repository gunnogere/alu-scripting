#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'ALU-Reddit-API'}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data').get('children')

    for post in posts:
        print(post.get('data').get('title'))
