#!/usr/bin/python3
"""
Module to start to understand API
"""


import requests
import csv


def fetch_and_print_posts():
    """
    Fetching information, going through it and printing only the titles
    """

    # Request to get the data from jsonplaceholder
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # Printing the current status
    print("Status Code: {}".format(response.status_code))

    # If successful, printing each title in the dict
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    """
    Fetching and saving as a dictionnary and serialized it into CSV
    """

    # Request to get the data from jsonplaceholder
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # If successful converting data into a dictionnary
    if response.status_code == 200:
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"],
                  "body": post["body"]} for post in data]

    # Saving it into CSV
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
        savepost = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        savepost.writeheader()  # Write header
        savepost.writerows(posts)  # Write multiple rows

    print("Posts saved to post.csv")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
