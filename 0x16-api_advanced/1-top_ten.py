#!/usr/bin/python3
"""Top Ten Reddit Posts"""


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch hot posts from.

    Returns:
        None

    Note:
        This function uses the Reddit API to fetch the first 10 hot posts
        from the specified subreddit and prints their titles.
    """
    from requests import get

    # Construct the URL for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    # Make the GET request to the Reddit API
    r = get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if r.status_code != 200:
        print(None)
        return None

    try:
        js = r.json()

    except ValueError:
        print(None)
        return None

    try:
        data = js.get("data")
        children = data.get("children")
        # Print titles of the first 10 hot posts
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except:
        print(None)
