import customtkinter as ctk
from tkinter import messagebox
import requests

# Function to handle task completion
def complete_task(task_id):
    try:
        # Replace 'http://api.example.com/tasks' with the actual API endpoint
        response = requests.post('http://api.example.com/tasks', json={"task_id": task_id, "status": "done"})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Task marked as complete!")
        else:
            messagebox.showerror("Error", f"Failed to update task. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the main application window
app = ctk.CTk()
app.title('Daily Checklist')
app.geometry('400x300')

# Sample tasks (Replace with your actual tasks)
tasks = [
    {"id": "1", "name": "Coded Today?"},
    {"id": "2", "name": "AWS"},
    {"id": "3", "name": "GCP"},
    {"id": "4", "name": "Azure"},
    {"id": "5", "name": "Project" },
]

# Creating task list
for task in tasks:
    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(master=frame, text=task["name"]).pack(side="left")
    ctk.CTkButton(master=frame, text="Done", command=lambda task_id=task["id"]: print("done")).pack(side="right")

app.mainloop()
