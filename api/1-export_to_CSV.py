#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Base API URL
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user data using employee ID from command line argument
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()

    # Fetch todo items for the user
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    # Set the filename for the CSV file
    filename = "{}.csv".format(user["id"])

    # Open the CSV file for writing
    with open(filename, mode="w", newline="") as csv_file:
        # Create a CSV writer object
        write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write headers to the CSV file
        write.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Loop through each todo item and write to the CSV file
        for todo in todos:
            write.writerow([user["id"], user["username"],
                            todo["completed"], todo["title"]])
