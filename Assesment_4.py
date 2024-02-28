class Task:
    def __init__(self, description, status="Incomplete"):
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task.description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. [{task.status}] {task.description}")

    def update_task_status(self, task_number, new_status):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.status = new_status
            print(f"Task updated: {task.description} - Status: {task.status}")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task deleted: {deleted_task.description}")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            new_task = Task(description)
            todo_list.add_task(new_task)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_status = input("Enter the new status (e.g., Incomplete, Complete): ")
            todo_list.update_task_status(task_number, new_status)

        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)

        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
