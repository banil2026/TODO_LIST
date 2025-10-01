def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    print("\n===== Task List =====")
    for task in tasks:
        print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")
