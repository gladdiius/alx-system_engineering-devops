#!/usr/bin/python3
""" returns number of subscripion."""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
        Returns 0 if the subreddit is invalid or if any other error occurs.
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

