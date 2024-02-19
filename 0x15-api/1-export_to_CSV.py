#!/usr/bin/python3
"""Python script to export data in the CSV format"""


import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(api_url, user_id)
    todo_str = '{}todos?userId={}'.format(api_url, user_id)
    employee_str = "Employee {} is done with tasks"
    file = '{}.csv'.format(user_id)

    res = requests.get(user_str)
    username = res.json().get('username')

    res = requests.get(todo_str)
    tasks = []
    for task in res.json():
        tasks.append([user_id, username,
                      task.get('completed'), task.get('title')])

    with open(file, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

        for task in tasks:
            csv_writer.writerow(task)
