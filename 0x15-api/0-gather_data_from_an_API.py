#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users/{}"
    todoUrl = "https://jsonplaceholder.typicode.com/todos"

    userList = requests.get(userUrl.format(userId)).json()
    todoList = requests.get(todoUrl.format(userId)).json()

    employeeName = userList.get("name")
    tasksCompleted = 0
    tasksTitles = []

    for task in todoList:
        if task.get('userId') == userList.get('id'):
            tasksTitles.append(task["title"])
            if tasksTitles:
                if task.get('completed'):
                    tasksCompleted += 1
    numTasks = len(tasksTitles)

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, tasksCompleted, numTasks))

    for i in tasksTitles:
        print("\t {}".format(i))
