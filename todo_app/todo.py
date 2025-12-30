tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

if __name__ == "__main__":
    add_task("Learn Git")
    show_tasks()

