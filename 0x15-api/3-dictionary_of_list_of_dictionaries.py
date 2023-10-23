#!/usr/bin/python3
"""
Fetching todo lists for an employee from a REST API
"""
import json
import requests
import sys


if __name__ == "__main__":
    apiURL = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(apiURL)
    emps = res.json()
    empDict = {}
    for emp in emps:
        emp_id = emp.get('id')
        emp_name = emp.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
        url = url + '/todos'
        res = requests.get(url)
        todos = res.json()
        empDict[emp_id] = []
        for todo in todos:
            empDict[emp_id].append({"task": todo.get('title'),
                                    "completed": todo.get('completed'),
                                    "username": emp_name})
    with open("todo_all_employees.json", 'w') as f:
        json.dump(empDict, f)
