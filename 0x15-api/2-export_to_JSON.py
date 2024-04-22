#!/usr/bin/python3
"""
Export data of a given user-id to csv format
"""

import json
import requests
import sys

if __name__ == "__main__":
    # set up base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the user ID from command line
    employee_id = sys.argv[1]

    # Get user data and to-do list for the given ID
    user = requests.get(url + "users/{}".format(employee_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Write todo list data to json file
    with open("{}.json".format(employee_id), mode='w') as jsonfile:
        json.dump(
                {
                    employee_id: [
                        {
                            "task": todo.get("title"),
                            "completed": todo.get("completed"),
                            "username": username
                        }
                        for todo in todos
                        ]
                },
                jsonfile,
                indent=4
                )
