#!/usr/bin/python3
"""
Reddit API - Count Words in Subreddit Titles
"""

from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def count_words(subreddit, word_list, after="", word_dic={}):
    """
    Retrieves and counts occurrences of specified
    words in the titles of hot articles
    for a given subreddit. The word counts are printed in descending order.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to be counted.
        after (str, optional): The Reddit API "after"
        parameter for pagination. Defaults to "".
        word_dic (dict, optional): A dictionary to store
        word counts. Defaults to {}.

    Returns:
        None

    Note:
        This function uses the Reddit API to fetch hot articles'
        titles from the specified
        subreddit and counts occurrences of specified words.
        It then prints word counts in descending order.

    Example:
        subreddit_name = "pyyhon"
        words_to_count = ["programming", "code", "tutorial"]
        count_words(subreddit_name, words_to_count)
    """
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    url = REDDIT + "r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    r = get(url, headers=HEADERS, params=params, allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        js = r.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

    except:
        return None

    count_words(subreddit, word_list, after, word_dic)
