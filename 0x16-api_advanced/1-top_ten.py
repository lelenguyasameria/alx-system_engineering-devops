#!/usr/bin/python3
"""
Module documentation for querying the Reddit API and printing the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Reddit API endpoint for getting the list of hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'CustomUserAgent'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the titles of the first 10 hot posts
        data = response.json().get('data', {}).get('children', [])

        if data:
            print(f"Top 10 hot posts in r/{subreddit}:\n")
            for post in data:
                title = post['data']['title']
                print(f"{title}\n")
        else:
            print(f"No hot posts found in r/{subreddit}")
    else:
        # Print None for invalid subreddits or other errors
        print(None)

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the name of the subreddit: ")
    top_ten(subreddit_name)

