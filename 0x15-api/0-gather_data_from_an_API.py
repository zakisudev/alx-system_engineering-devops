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
    empName = res.json().get('name')

    todoURL = mainURL + "/todos"
    res = requests.get(todoURL)
    todos = res.json()
    done = 0
    done_todos = []

    for todo in todos:
        if todo.get('completed'):
            done_todos.append(todo)
            done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(empName, done, len(todos)))
    for todo in done_todos:
        print("\t {}".format(todo.get("title")))
