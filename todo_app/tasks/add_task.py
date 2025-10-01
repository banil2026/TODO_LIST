def add_task(tasks):
    if len(tasks) >= 8:
        print("Task limit reached. Cannot add more than 8 tasks.")
        return
    
    task_description = input("Enter task description: ")
    task_id = len(tasks) + 1
    task = {"id": task_id, "task": task_description, "status": "Pending"}
    tasks.append(task)
    print(f"Task '{task_description}' added successfully!")
