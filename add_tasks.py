from tasks import tasks

tasks_dict = {task["id"]: task["api"] for task in tasks}


def add_task(name):
    # Extract the current highest ID from the tasks and convert to int
    max_id = max(int(task['id']) for task in tasks)
    
    # Create new task with ID incremented by 1 and custom API
    new_task = {
        "id": str(max_id + 1),  # Convert ID back to string if needed
        "name": name,
        "api": f"api/{name.replace(' ', '_')}"  # Replace spaces with underscores for valid URL paths
    }
    
    # Append the new task to the tasks list
    tasks.append(new_task)
    print(f"Added new task: {new_task}")

    # Update the tasks.py file
    with open('tasks.py', 'w') as file:
        file.write('tasks = [\n')
        for task in tasks:
            file.write(f'    {task},\n')
        file.write(']\n')

# Example usage
add_task("Read Books")