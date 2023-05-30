#!/usr/bin/python3
"""Export to csv all tasks that are owned by this employee
   Usage: ./1-export_to_CSV.py $USER_ID
   Every record in the csv file must be in the format:
       "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
   The csv file should be named in the format:
       $USER_ID.csv
"""

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
