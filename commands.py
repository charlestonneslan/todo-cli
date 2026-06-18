import argparse
from store import Task, tasks

def handle_add(args):
    id = max((t.id for t in tasks), default=0) + 1
    task = Task(id, args.title, " ".join(args.description))
    tasks.append(task)

def handle_list(args):
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        if not t.deleted:
            t.display()

def handle_clear(args):
    if not tasks:
        print("No tasks to clear.")
        return
    tasks.clear()

def handle_done(args):
    if not tasks:
        print("No task to mark as done.")
        return
    task = next((t for t in tasks if t.id == args.id), None)
    if task is None:
        print(f"No task with id {args.id}")
        return
    task.mark_done()

def handle_delete(args):
    if not tasks:
        print("No tasks to delete.")
        return
    task = next((t for t in tasks if t.id == args.id), None)
    if task is None:
        print(f"No task with id {args.id}")
        return
    task.delete()

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

done_parser = subparsers.add_parser("done", help="Mark a task as done")
done_parser.add_argument("id", type=int, help="ID of task to mark as done")
done_parser.set_defaults(func=handle_done)

delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id", type=int, help="ID of task to delete")
delete_parser.set_defaults(func=handle_delete)