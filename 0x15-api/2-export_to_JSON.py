#!/usr/bin/python3
"""
Fetching todo lists for an employee from a REST API
"""
import requests
import json
import sys


if __name__ == "__main__":
    empId = sys.argv[1]
    apiURL = "https://jsonplaceholder.typicode.com/users"
    mainURL = apiURL + "/" + empId

    res = requests.get(mainURL)
    empUName = res.json().get('username')

    todoURL = mainURL + "/todos"
    res = requests.get(todoURL)
    todos = res.json()

    empDict = {empId: []}
    for todo in todos:
        empDict[empId].append({"task": todo.get('title'),
                               "completed": todo.get('completed'),
                               "username": empUName})
    with open("{}.json".format(empId), 'w') as f:
        json.dump(empDict, f)
