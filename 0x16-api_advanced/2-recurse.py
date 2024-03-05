#!/usr/bin/python3
"""Recursive function that returns a list containing the titles
of all hot articles"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    """
    try:
        headers = {"User-Agent": "Microsoft Edge Version 122.0.2365.66"}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        if after:
            url += f"&after={after}"

        response = requests.get(url, headers=headers)
        data = response.json()

        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None
    except (KeyError, requests.RequestException):
        return None
