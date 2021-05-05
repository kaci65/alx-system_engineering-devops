#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

from sys import argv
import requests


if __name__ == "__main__":
    userId = argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users/{}"
    todoUrl = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(userUrl.format(userId))
    todo = requests.get(todoUrl.format(userId))
    userList = users.json()
    todoList = todo.json()

    employeeName = userList.get("name")
    tasksCompleted = 0
    tasksTitles = []
    numTasks = len(todoList)

    for task in todoList:
        if task['completed']:
            tasksCompleted += 1
            tasksTitles.append(task["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, tasksCompleted, numTasks))

    for i in tasksTitles:
        print("\t {}".format(i))
