#!/usr/bin/python3
"""
Returns info about todo list based on employee id
"""

import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    # returns user
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    # Sends get request, returns todo items by user id
    to_do = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    # sys.argv[1] will be our input, input = userid
    # from this todos list will return
    total_tasks = len(to_do)
    completed_task = 0
    # counter for tasks
    for task in to_do:
        if task["completed"]:
            completed_task = completed_task + 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed_task, total_tasks))
    # gets info for employee name, then prints

    for task in to_do:
        if task["completed"]:
            print("\t {}".format(task["title"]))
