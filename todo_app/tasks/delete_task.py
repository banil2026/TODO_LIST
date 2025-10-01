def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    
    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
