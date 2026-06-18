import json

class Task:

    def __init__(self, id: int, title: str, description: str, done = False, deleted = False):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.deleted = deleted

    def mark_done(self):
        self.done = True
    
    def delete(self):
        self.deleted = True
        
    def edit_description(self, new_description: str):
        self.description = new_description

    def display(self):
        print("-------------------------------------")
        print(f"Task: {self.title} (ID: {self.id})")
        print(f"Description: {self.description}")
        print(f"Done: {"[x]" if self.done else "[]"}")
        print("-------------------------------------")
        print()

tasks = []
FILE_NAME = "tasks.json"

def load_tasks():
    global tasks
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:   
            raw_data = json.load(file)
            tasks.clear()
            tasks.extend([Task(item["id"], item["title"], item["description"], item["done"], item["deleted"]) for item in raw_data])
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def write_tasks():
    serializable_tasks = [t.__dict__ for t in tasks]
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(serializable_tasks, file, indent=4)