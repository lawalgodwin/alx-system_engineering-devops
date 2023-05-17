#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId
    response = requests.get(url)
    employeeName = response.json().get('name')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done_tasks = [task for task in tasks if task.get('completed')]
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(done_tasks), len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
