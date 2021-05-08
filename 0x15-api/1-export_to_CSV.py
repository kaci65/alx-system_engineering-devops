#!/usr/bin/python3
"""
Using '0-gather_data_from_an_API.py', extend your script to export
data in CSV format
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users/{}"
    todoUrl = "https://jsonplaceholder.typicode.com/todos"

    userList = requests.get(userUrl.format(userId)).json()
    todoList = requests.get(todoUrl.format(userId)).json()

    employeeName = userList.get("name")
    tasksCompleted = 0
    numTasks = 0
    tasksTitles = []

    with open('{}.csv'.format(userId), mode='w') as file:
        csvFormat = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todoList:
            if task.get('userId') == userList.get('id'):
                csvFormat .writerow([userId, employeeName,
                                    task.get('completed'), task.get('title')])
