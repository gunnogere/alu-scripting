#!/usr/bin/python3
"""Queries Reddit API and prints the first 10 hot post titles."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    # Use {} placeholder so .format() can dynamically insert the subreddit
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    
    # Custom User-Agent to prevent getting blocked/rate-limited (429)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Optional: explicitly ask Reddit for only 10 items to save bandwidth
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    # If the subreddit is invalid or an error occurs, print None
    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
