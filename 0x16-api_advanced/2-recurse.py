#!/usr/bin/python3
""" recurseion"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieve the titles of hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of
            hot posts (optional, default is an empty list).

        after (str): A token used for pagination to retrieve the next set
            of results (optional, default is None).

        Returns:
            list: A list containing the titles of hot posts in the subreddit.
            None: If the subreddit is invalid or any other error occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {}).get('children', [])
    after = response.json().get('data', {}).get('after')

    for post in data:
        hot_list.append(post['data']['title'])

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
