from tkinter import messagebox
import requests
from tasks import tasks 

class TaskManager:
    def __init__(self, tasks_file):
        self.tasks_file = tasks_file
        self.load_tasks()

    def load_tasks(self):
        # Assuming the tasks are stored in a Python file as a list of dictionaries
        from tasks import tasks as loaded_tasks
        self.tasks = loaded_tasks
        

    def add_task(self, name):
        # Extract the current highest ID from the tasks and convert to int
        max_id = max(int(task['id']) for task in self.tasks)

        # Create new task with ID incremented by 1 and custom API
        new_task = {
            "id": str(max_id + 1),  # Convert ID back to string if needed
            "name": name,
            "api": f"api/{name.replace(' ', '_')}"  # Replace spaces with underscores for valid URL paths
        }

        # Append the new task to the tasks list
        self.tasks.append(new_task)
        print(f"Added new task: {new_task}")

        # Update the tasks file
        with open(self.tasks_file, 'w') as file:
            file.write('tasks = [\n')
            for task in self.tasks:
                file.write(f'    {task},\n')
            file.write(']\n')

        

        print("Tasks file updated.")

    def task_complete(self, task_id):
        # Convert list of tasks to a dictionary for efficient lookups
        tasks_dict = {task["id"]: task["api"] for task in tasks}

         #for free tier, there is 25% chance that server will reject the request. To send requests till they accept the request
        free_tier_offset = True

        while free_tier_offset:
            try:
                response = requests.post(tasks_dict[task_id], json={"task_id": task_id, "status": "done"})
                if response.status_code == 200 and response.text != "Task is not complete due to 25 percent rejection rate. Replace text with appropriate wording":
                    messagebox.showinfo("Success", "Task marked as complete!")
                    free_tier_offset = False
                else:
                    messagebox.showerror("Error", f"Failed to update task. Status code: {response.status_code}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

# Usage
# task_manager = TaskManager('tasks.py')
# task_manager.add_task("Read Books")
