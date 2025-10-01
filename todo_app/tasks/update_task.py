def update_task(tasks):
    if not tasks:
        print("No tasks available to update.")
        return
    
    try:
        task_id = int(input("Enter task ID to update: "))
        for task in tasks:
            if task["id"] == task_id:
                new_desc = input("Enter new task description: ")
                task["task"] = new_desc
                print("Task updated successfully!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
