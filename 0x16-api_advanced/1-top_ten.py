#!/usr/bin/python3
"""Function queries the Reddit API and prints the titles of the first
10 hot posts"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.
    """
    try:
        headers = {"User-Agent": "Microsoft Edge Version 122.0.2365.66"}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        response = requests.get(url, headers=headers)
        data = response.json()

        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except (KeyError, requests.RequestException):
        print(None)
