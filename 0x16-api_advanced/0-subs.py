#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers of the subreddit.
    Returns 0 if the subreddit is invalid or if any other error occurs.
    """

    # Reddit API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the number of subscribers from the response
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid or any other error occurs, return 0
        return 0
