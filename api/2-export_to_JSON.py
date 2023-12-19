#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""

import json
import requests
import sys


if __name__ == "__main__":
    # Base API URL
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user data using employee ID from command line argument
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()

    # Fetch todo items for the user
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    # Prepare data in the required format
    tasks_data = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            }
            for todo in todos
        ]
    }

    # Set the filename for the JSON file
    filename = "{}.json".format(user["id"])

    # Write data to JSON file
    with open(filename, "w") as json_file:
        json.dump(tasks_data, json_file)
