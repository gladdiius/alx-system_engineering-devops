#!/usr/bin/python3
""" csv formate """

import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    # Fetch employee information
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Fetch employee's TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for todo in todos_data:
            user_id = employee_id
            username = employee_data.get('username', 'Unknown')
            task_completed_status = todo.get('completed', False)
            task_title = todo.get('title', 'No Title')

            # Write task to CSV file
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

if __name__ == "__main__":
    # Example usage: pass the employee ID as a command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
