#!/usr/bin/python3
# Return information about a given employee todo list progress
# Using REST API

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [todo for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t{}".format(task.get("title"))) for task in completed]
