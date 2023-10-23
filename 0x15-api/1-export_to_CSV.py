#!/usr/bin/python3
"""
Fetching todo lists for an employee from a REST API
"""
import requests
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

    with open("{}.csv".format(empId), 'w') as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'
                      .format(empId, empUName, todo.get('completed'),
                              todo.get('title')))
