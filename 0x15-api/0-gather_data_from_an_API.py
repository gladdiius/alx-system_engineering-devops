#!/usr/bin/python3
"""using this REST API, for info about employee."""
import requests
import sys

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
    completed_tasks = sum(todo.get('completed', False) for todo in todos_data)

    # Display information
    print(f"Employee {employee_data.get('name', 'Unknown')} is done with tasks ({completed_tasks}/{total_tasks}):")
    print(f"{employee_data.get('name', 'Unknown')}:")

    # Display completed tasks
    for todo in todos_data:
        if todo.get('completed', False):
            print(f"\t{todo.get('title', 'No Title')}")

if __name__ == "__main__":
    # Example usage: pass the employee ID as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
