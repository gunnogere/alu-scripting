#!/usr/bin/python3
"""Queries Reddit API and prints the first 10 hot post titles."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/programming/hot".format(subreddit)
    headers = {"User-Agent": "python:reddit.api:v1.0"}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
