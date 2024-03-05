#!/usr/bin/python3
"""parses the title of all hot titles and prints a sorted count"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """
    Recursively queries the Reddit API, parses titles, and prints a
    sorted count of given keywords.
    """
    try:
        headers = {"User-Agent": "Microsoft Edge Version 122.0.2365.66"}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        if after:
            url += f"&after={after}"

        response = requests.get(url, headers=headers)
        data = response.json()

        titles = [post["data"]["title"] for post in data["data"]["children"]]

        keyword_counts = Counter()
        for title in titles:
            for word in word_list:
                if word.lower() in title.lower():
                    keyword_counts[word.lower()] += 1

        after = data["data"]["after"]
        if after:
            count_words(subreddit, word_list, after)
        else:
            sorted_counts = sorted(
                keyword_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    except (KeyError, requests.RequestException):
        pass
