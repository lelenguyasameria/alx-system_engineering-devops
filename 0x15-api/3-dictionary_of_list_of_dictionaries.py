#!/usr/bin/python3
"""
Module to retrieve employee TODO list progress from a REST API and export data for all employees in JSON format.
"""

import requests
import sys
import json

def get_all_employees_todo_progress():
    """
    Retrieve and display TODO list progress for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com/users'
    
    try:
        users_response = requests.get(base_url)
        users_data = users_response.json()

        all_employees_data = {}

        for user in users_data:
            user_id = user['id']
            user_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

            todos_response = requests.get(user_url)
            todos_data = todos_response.json()

            completed_tasks = [
                {"username": user['username'], "task": task["title"], "completed": task["completed"]}
                for task in todos_data
            ]

            all_employees_data[user_id] = completed_tasks

        export_to_json(all_employees_data)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

def export_to_json(data):
    """
    Export data to JSON file.
    """
    json_filename = 'todo_all_employees.json'

    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f'Data exported to {json_filename}')

if __name__ == "__main__":
    get_all_employees_todo_progress()

