def tasks():
    task = []
    print("-"*30,"Welcome to task Management APP","-"*30)

    total_tasks = int(input("how many tasks you want to add: "))
    for i in range(1, total_tasks+1):
        task_name = input(f"enter the task-{i}: ")
        task.append(task_name)
    print(task)

    while True:
        print("="*50)
        operation = int(input("Enter your choice:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/\n Enter any number here: "))
        if operation == 1:
            ask = input("enter the task you want to add: ")
            task.append(ask)
            print(f"{ask} has been successfully added")

        elif operation == 2:
            ask = input("enter the task you want to update")
            idx = task.index(ask)
            up = input("Enter the updated task: ")
            task[idx] = up
            print(f"task has been updated")

        elif operation == 3:
            ask = input("Enter the task you want to delete: ")
            idx = task.index(ask)
            del task[idx]
            print(f"requested task has been successfully deleted")
        
        elif operation == 4:
            print(task)

        elif operation == 5:
            print("Application is closing.....")
            break
        
        else:
            print("Invalid Input!")
tasks()