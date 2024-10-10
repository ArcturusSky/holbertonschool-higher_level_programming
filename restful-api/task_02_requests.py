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
    # Make a GET resquest to jsplaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts") 

    print("Status Code: {}".format(response.status_code))

    # Check the status code of the response
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetching and saving as a dictionnary and serialized it into CSV
    """

    # Make a GET resquest to jsplaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts") 

    # If successful converting data into a dictionnary
    if response.status_code == 200:
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"],"body": post["body"]} for post in data]

    # Saving it into CSV
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldname = ["id", "title", "body"]
        savepost = csv.DictWriter(file, fieldnames=fieldname)
        savepost.writeheader() # Write header
        savepost.writerows(posts) # Write multiple rows

if __name__ == "__main__":
    fetch_and_save_posts()
    fetch_and_print_posts()
