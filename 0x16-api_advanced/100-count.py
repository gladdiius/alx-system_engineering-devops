#!/usr/bin/python3
""" count. """
from collections import Counter
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = Counter()

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit) + "?after={}".format(after)

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return

    data = response.json().get('data', {}).get('children', [])
    after = response.json().get('data', {}).get('after')

    for post in data:
        title = post['data']['title']
        words = title.lower().split()

        for word in word_list:
            if word.lower() in words:
                counts[word.lower()] += 1

    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
