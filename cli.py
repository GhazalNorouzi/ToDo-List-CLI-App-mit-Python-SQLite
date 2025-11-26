
from task import Tasks

def cli():
    while True:
        print("1. add task")
        print("2. show tasks")
        print("3. edit tasks")
        print("4. delete task")
        print("5. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            task = Tasks(title, description)
            task.save()
            print("Task added")


        elif choice == "2":
            tasks = Tasks.get_all()

            if not tasks:
                print("No tasks found")
            else:
                print("\n--- TASK LIST ---")

            for task in tasks:
                print(f"{task.id} | {task.title} | {task.description} | {task.status}")
            print("-----------------\n")


        elif choice == "3":
            task_id = int(input("Enter task ID to edit: "))
            task = Tasks.get_by_id(task_id)

            if not task:
                print("Task not found")
            else:
                new_title = input(f"Enter new title ({task.title}): ") or task.title
                new_description = input(f"Enter new description ({task.description}): ") or task.description
                new_status = input(f"Enter new status ({task.status}): ") or task.status

                task.title = new_title
                task.description = new_description
                task.status = new_status
                task.update()

                print("Task updated")

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task = Tasks.get_by_id(task_id)

            if not task:
                print("Task not found")
            else:
                task.delete()
                print("Task deleted")

        elif choice == "5":
            print("exit")
            break

        else:
            print("Invalid choice")






