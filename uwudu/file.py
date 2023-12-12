""" (U w U)_/××××××  File Operations  ××××××\_(U w U) """

import os

UWUDU_FILE = os.path.expanduser("~/.uwudu.txt")


def read_todo_list():
    try:
        with open(UWUDU_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def write_todo_list(todo_list):
    with open(UWUDU_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(todo_list))
