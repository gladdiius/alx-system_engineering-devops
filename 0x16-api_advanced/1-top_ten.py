#!/usr/bin/python3
"""returns the top 10 title"""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts in a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        # If the subreddit is invalid or any other error occurs, print None
        print(None)
