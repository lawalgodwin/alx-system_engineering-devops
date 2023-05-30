#!/usr/bin/python3
"""Export to json file all tasks that are owned by this employee
   Usage: ./2-export_to_JSON.py $USER_ID
   Every record in the csv file must be in the format:
   { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
     "username":"USERNAME"},
   {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
     "username": "USERNAME"}, ... ]
   }
   The json file should be named in the format:
       $USER_ID.json
"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId
    response = requests.get(url)
    employeeName = response.json().get('username')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open(f'{employeeId}.json', 'w', encoding='utf-8') as jsonFile:
        userTasks = []
        for task in tasks:
            USER_ID = employeeId
            USERNAME = employeeName
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get("title")
            row = {
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            }
            userTasks.append(row)
        json.dump({employeeId: userTasks}, jsonFile)
