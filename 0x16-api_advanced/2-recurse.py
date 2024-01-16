#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
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
