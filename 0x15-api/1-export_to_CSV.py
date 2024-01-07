#!/usr/bin/python3
"""
Module to retrieve employee TODO list progress from a REST API and export data in CSV format.
"""

import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display employee TODO list progress.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todos_url = f'{base_url}todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]

        print(f'Employee {user_data["name"]} is done with tasks '
              f'({len(completed_tasks)}/{len(todos_data)}):')
        print(f'\t{user_data["name"]}: {len(completed_tasks)}/{len(todos_data)}')

        for task in completed_tasks:
            print(f'\t{task["title"]}')

        export_to_csv(employee_id, user_data["username"], completed_tasks)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

def export_to_csv(user_id, username, completed_tasks):
    """
    Export data to CSV file.
    """
    csv_filename = f'{user_id}.csv'

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in completed_tasks:
            csv_writer.writerow([user_id, username, "completed", task["title"]])

    print(f'Data exported to {csv_filename}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./employee_todo.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer as the employee ID.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

