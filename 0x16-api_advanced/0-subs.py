#!/usr/bin/python3
"""
Module documentation for querying the Reddit API and returning the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'CustomUserAgent'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    else:
        # Return 0 for invalid subreddits or other errors
        return 0

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the name of the subreddit: ")
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers for r/{subreddit_name} is: {subscribers_count}")
