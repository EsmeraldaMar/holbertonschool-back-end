#!/usr/bin/python3
"""Records all tasks that are owned by all employees"""

import json
import requests
import sys


if __name__ == "__main__":
    # Base API URL
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user data using employee ID from command line argument
    users = requests.get(url + "/users").json()

    tasks_data = {}
    # Iterate over each user
    for user in users:
        user_id = user["id"]
        username = user["username"]

    # Fetch todo items for the user
        todos = requests.get(url + "/todos", params={"userId": user_id}).json()

        # Prepare data in the required format
        tasks_data[user_id] = [
                {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                for todo in todos
            ]

    # Set the filename for the JSON file
    filename = "todo_all_employees.json"

    # Write data to JSON file
    with open(filename, "w") as json_file:
        json.dump(tasks_data, json_file)
