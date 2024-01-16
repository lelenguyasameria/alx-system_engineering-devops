#!/usr/bin/python3
"""
Module documentation for a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles (default is an empty list).

    Returns:
        list or None: A list containing the titles of hot articles or None if no results are found for the given subreddit.
    """
    # Reddit API endpoint for getting the list of hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'CustomUserAgent'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the titles of hot posts
        data = response.json().get('data', {}).get('children', [])

        if data:
            for post in data:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there are more pages (pagination) and recursively call the function
            after = response.json().get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        # Return None for invalid subreddits or other errors
        return None

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the name of the subreddit: ")
    result = recurse(subreddit_name)

    if result is not None:
        print(f"Titles of all hot articles in r/{subreddit_name}:\n")
        for title in result:
            print(f"{title}\n")
    else:
        print(f"No results found for r/{subreddit_name}")

