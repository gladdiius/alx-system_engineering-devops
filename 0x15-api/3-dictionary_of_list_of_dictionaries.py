#!/usr/bin/python3
""" export all the employees """

import requests
import json

def export_all_employees_todo_to_json():
    """export all employees"""
    all_employees_data = {}

    # Fetch all users
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()

    for user in users_data:
        employee_id = user['id']
        employee_username = user['username']

        # Fetch employee's TODO list
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare data for JSON export
        user_tasks = []

        for todo in todos_data:
            task_title = todo.get('title', 'No Title')
            task_completed_status = todo.get('completed', False)

            user_tasks.append({
                "username": employee_username,
                "task": task_title,
                "completed": task_completed_status
            })

        # Add employee data to the main dictionary
        all_employees_data[employee_id] = user_tasks

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_data, json_file)

if __name__ == "__main__":
    export_all_employees_todo_to_json()
