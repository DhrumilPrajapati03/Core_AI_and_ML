def tasks():
    task = []
    print("--Welcome to task Management APP--")

    total_tasks = int(input("how many tasks you want to add: "))
    for i in range(1, total_tasks+1):
        task_name = input(f"enter the task-{i}: ")
        task.append(task_name)
    print(task)

tasks()