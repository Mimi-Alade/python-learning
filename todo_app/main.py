import os

BASE_DIR = os.path.dirname(__file__)
TASKS_FILE = os.path.join(BASE_DIR, "tasks.txt")


def main():
    while True:
        user_task = input("What task would you like to add? ")

        if user_task == "none":
            view_tasks()
            delete_tasks()
        else:
            add_task(user_task)


def add_task(task):
    with open(TASKS_FILE, "a") as tasks:
        if tasks.tell() != 0:
            tasks.write("\n")
        tasks.write(task)


def view_tasks():
    view_task = input("Would you like to view your tasks? ")
    if view_task == "yes":
        with open(TASKS_FILE, "r") as tasks:
            print(tasks.read())


def delete_tasks():
    delete_task = input("Would you like to delete a task? ")
    if delete_task == "yes":
        with open(TASKS_FILE, "r") as tasks:
            lines = tasks.readlines()
            for position, task in enumerate(lines, start=1):
                print(f"{position}. {task.strip()}")

        response = input("Type the number of the task you would like to delete: ")

        with open(TASKS_FILE, "w") as tasks:
            for position, line in enumerate(lines, start=1):
                if position != int(response):
                    tasks.write(line)
        print("Removed.")



if __name__ == "__main__":
    main()