#!/usr/bin/python3
"""
Using '0-gather_data_from_an_API.py', extend your script to export
data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users/{}"
    todoUrl = "https://jsonplaceholder.typicode.com/todos"

    userList = requests.get(userUrl.format(userId)).json()
    todoList = requests.get(todoUrl.format(userId)).json()

    employeeName = userList.get("name")
    taskList = []

    for task in todoList:
        if task.get('userId') == userList.get('id'):
            taskList.append({"task": task.get("title"),
                             "completed": task.get("completed"),
                             "username": employeeName})

    with open("user_id.json", mode="w") as f_json:
        json.dump(taskList, f_json)
