#!/usr/bin/python3
"""Python script that returns information about his/her TODO list"""


import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(api_url, user_id)
    todo_str = '{}todos?userId={}'.format(api_url, user_id)
    employee_str = "Employee {} is done with tasks"

    res = requests.get(user_str)
    print(employee_str.format(res.json().get('name')), end="")

    res = requests.get(todo_str)
    tasks = [task for task in res.json() if task.get('completed') is True]

    print("({}/{}):".format(len(tasks), len(res.json())))
    for task in tasks:
        print("\t {}".format(task.get("title")))
