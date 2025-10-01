def mark_done(tasks):
    if not tasks:
        print("No tasks available to mark as done.")
        return
    
    try:
        task_id = int(input("Enter task ID to mark as done: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "Done":
                    print("Task is already marked as Done.")
                else:
                    task["status"] = "Done"
                    print("Task marked as Done successfully!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
