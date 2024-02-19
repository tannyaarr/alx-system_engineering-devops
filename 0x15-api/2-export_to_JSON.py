#!/usr/bin/python3
"""Python script to export data in the JSON format"""


import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/{}'
    todo_str = 'https://jsonplaceholder.typicode.com/todos?'
    user = requests.get(api_url.format(user_id))

    name = user.json().get('username')
    todos = requests.get(todo_str)

    todos_user = {}
    tasks = []

    for task in todos.json():
        if task.get('userId') == int(user_id):
            task_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')
                    }
            tasks.append(task_dict)
        todos_user[user_id] = tasks

        file = user_id + 'json'

        with open(file, mode='w') as user_file:
            json.dump(todos_user, user_file)
