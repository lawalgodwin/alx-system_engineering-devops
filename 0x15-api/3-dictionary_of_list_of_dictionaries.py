#!/usr/bin/python3
"""Export to json file all tasks that are owned by all employees
   Usage: ./3-dictionary_of_list_of_dictionaries.py
   Every record in the csv file must be in the format:
   { "USER_ID": [ {"username":"USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
   {"username":"USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ]
   }
   The json file should be named:
       todo_all_employees.json
"""

import json
import requests
import sys


if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com/"
    todoUrl = baseUrl + "todos"
    response = requests.get(todoUrl)
    tasks = response.json()
#   print(tasks)

    with open('todo_all_employees.json', 'w', encoding='utf-8') as jsonFile:
        usersTasks = {}
        U_ID = ''
        for task in tasks:
            USER_ID = task.get('userId')
            U_ID = USER_ID
            userInfo = requests.get('{}users/{}'.format(baseUrl, USER_ID))
            USERNAME = userInfo.json().get('username')
            # get the todos for this user
            userTasks = []
            userTodos = requests.get('{}users/{}/todos'
                                     .format(baseUrl, USER_ID)).json()
            for todo in userTodos:
                TASK_COMPLETED_STATUS = todo.get('completed')
                TASK_TITLE = todo.get("title")
                row = {
                    "username": USERNAME,
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS
                }
                userTasks.append(row)
#            print(userTasks)
            usersTasks['{}'.format(U_ID)] = userTasks
        json.dump(usersTasks, jsonFile)
