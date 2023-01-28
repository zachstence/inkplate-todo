from lib import clickup

if __name__ == "__main__":
    tasks = clickup.get_tasks()
    print(tasks)
