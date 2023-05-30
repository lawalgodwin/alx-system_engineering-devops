#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

from csv import writer, QUOTE_ALL
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

    with open(f'{employeeId}.csv', 'w', encoding='utf-8') as csvFile:
        csv_writer = writer(csvFile, delimiter=',', quoting=QUOTE_ALL)
        for task in tasks:
            USER_ID = employeeId
            USERNAME = employeeName
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get("title")
            row = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
            csv_writer.writerow(row)
