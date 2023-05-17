#!/usr/bin/python3
""" A Python script that, using jsonplaceholder REST API,
    for a given employee ID, returns information about his/her
    TODO list progress.
"""
import requests

from sys import argv

base_url = "https://jsonplaceholder.typicode.com/users/"


if __name__ == '__main__':
    try:
        employee_id = argv[1]
        response = requests.get(base_url + "{}".format(employee_id)).json()
        employee_name = response.get('name')
        user_todos = requests.get(base_url + "{}/todos"
                                  .format(employee_id)).json()
        completed_todos = [t for t in user_todos if t.get('completed')]
        completed_tasks = len(completed_todos)
        all_tasks = len(user_todos)
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, completed_tasks, all_tasks))
        for task in completed_todos:
            print("\t {}".format(task.get('title')))
    except IndexError as e:
        pass
    except Exception as e:
        pass
