import argparse

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
    for t in tasks:
        t.display()

def main():
    parser = argparse.ArgumentParser(description="A parser for a task cli")
    
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("title", type=str, help="Title of task")
    add_parser.add_argument("description", type=str, help="Description of task", nargs="+")
    add_parser.set_defaults(func=handle_add)

    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=handle_list)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
