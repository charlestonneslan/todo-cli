import argparse
import json

tasks = []

class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
    
    def display(self):
        print(f"Task: {self.title} - {self.description}")

def handle_add(args):
    task = Task(args.title, " ".join(args.description))
    tasks.append(task)
    print(task.title, task.description)

def handle_list(args):
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        t.display()

def handle_clear(args):
    global tasks
    if not tasks:
        print("No tasks to clear.")
        return
    tasks = []

FILE_NAME = "tasks.json"
parser = argparse.ArgumentParser(description="A parser for a task cli")

subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")

add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("title", type=str, help="Title of task")
add_parser.add_argument("description", type=str, help="Description of task", nargs="+")
add_parser.set_defaults(func=handle_add)

list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.set_defaults(func=handle_list)

clear_parser = subparsers.add_parser("clear", help="Empty the tasks")
clear_parser.set_defaults(func=handle_clear)

def load_tasks():
    global tasks
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:   
            raw_data = json.load(file)
            tasks = [Task(item["title"], item["description"]) for item in raw_data]
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def write_tasks():
    serializable_tasks = [t.__dict__ for t in tasks]
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(serializable_tasks, file, indent=4)

def main():
    load_tasks()
    args = parser.parse_args()
    args.func(args)
    write_tasks()

if __name__ == "__main__":
    main()

