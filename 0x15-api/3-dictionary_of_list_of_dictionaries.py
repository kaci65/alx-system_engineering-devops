#!/usr/bin/python3
"""
Using '0-gather_data_from_an_API.py', extend your script to export
data in JSON format (Dictionary - all employees data)
"""

import json
import requests


if __name__ == "__main__":
    userUrl = "https://jsonplaceholder.typicode.com/users"
    todoUrl = "https://jsonplaceholder.typicode.com/todos"

    userList = requests.get(userUrl).json()
    todoList = requests.get(todoUrl).json()

    taskList = []
    tasksDict = {}

    for user in userList:
        for task in todoList:
            if task.get('userId') == user.get('id'):
                taskList.append({"username": user.get("username"),
                                 "task": task.get("title"),
                                 "completed": task.get("completed")})
        tasksDict[user.get('id')] = taskList

    with open("todo_all_employees.json", mode="w") as f_json:
        json.dump(tasksDict, f_json)
