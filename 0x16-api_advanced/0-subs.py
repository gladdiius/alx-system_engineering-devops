#!/usr/bin/python3
""" number fo subscriber"""
import requests


if __name__ == '__main__':
    def number_of_subscribers(subreddit):
        """Return the number of subscribers for a given subreddit.

        Args:
        subreddit (str): The name of the subreddit.

        Returns:
        int: The number of subscribers for the subreddit.
        0: If the subreddit is invalid or any other error occurs.
        """

        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': 'MyRedditBot/1.0'}

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
