#!/usr/bin/python3
""" json file"""

import requests
import sys
import json

def export_employee_todo_to_json(employee_id):
    # Fetch employee information
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Fetch employee's TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data for JSON export
    user_id = employee_id
    username = employee_data.get('username', 'Unknown')
    user_tasks = []

    for todo in todos_data:
        task_title = todo.get('title', 'No Title')
        task_completed_status = todo.get('completed', False)

        user_tasks.append({
            "task": task_title,
            "completed": task_completed_status,
            "username": username
        })

    # Export to JSON
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump({user_id: user_tasks}, json_file)

if __name__ == "__main__":
    # Example usage: pass the employee ID as a command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_to_json(employee_id)
