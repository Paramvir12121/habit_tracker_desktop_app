import customtkinter as ctk
from tkinter import messagebox
import requests
from tasks import tasks



def api_for_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            print(f"Task ID: {task['id']}, API: {task['api']}")
            return task['api']
            


# Function to handle task completion
def complete_task(task_id):

    for i in range(4):
        try:
            response = requests.post('http://api.example.com/tasks', json={"task_id": task_id, "status": "done"})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Task marked as complete!")
                break
            else:
                messagebox.showerror("Error", f"Failed to update task. Status code: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the main application window
app = ctk.CTk()
app.title('Daily Checklist')
app.geometry('400x300')

# Sample tasks (Replace with your actual tasks)


# Creating task list
for task in tasks:
    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(master=frame, text=task["name"]).pack(side="left")
    ctk.CTkButton(master=frame, text="Done", command=lambda task_id=task["id"]: print("done")).pack(side="right")

app.mainloop()
