#!/usr/bin/python3
"""
Module documentation for a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        counts (dict): A dictionary to store the counts of each keyword (default is None).

    Returns:
        None
    """
    if counts is None:
        counts = {}

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
                title = post['data']['title'].lower()

                for word in word_list:
                    # Check if the keyword is in the title and update the counts
                    count = title.count(word.lower())
                    counts[word.lower()] = counts.get(word.lower(), 0) + count

            # Check if there are more pages (pagination) and recursively call the function
            after = response.json().get('data', {}).get('after')
            if after:
                return count_words(subreddit, word_list, counts)
            else:
                # Print the sorted counts
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for keyword, count in sorted_counts:
                    print(f"{keyword}: {count}")
        else:
            print("No posts found for the given subreddit")
    else:
        print("Invalid subreddit or unable to connect to the Reddit API")

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the name of the subreddit: ")
    keywords = input("Enter space-separated keywords: ").split()
    count_words(subreddit_name, keywords)

