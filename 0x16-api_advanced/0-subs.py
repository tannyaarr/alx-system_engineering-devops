#!/usr/bin/python3
""""function that queries the Reddit API and
returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Retreieve the number of subscribers for a given subreddit"""
    try:
        headers = {"User-Agent": "Microsoft Edge Version 122.0.2365.66"}
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(url, headers=headers)
        data = response.json()

        subscribers = data["data"]["subscibers"]
        return subscribers
    except (KeyError, requests.RequestException):
        return 0
