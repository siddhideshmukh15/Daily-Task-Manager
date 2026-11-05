print("==== DAILY TASK MANAGER ====")
tasks=[]
while True:
    print("1. Add Task")
    print("2.View Task")
    print("3.Complete task")
    print("4.Delete task")
    print("5. Exit")

    choice=input("Enter yor choice:")

    if choice=="1":
        task=input("Enter your task:")
        tasks.append({
            "name":task,
            "status":"pending"
        })
        print("Task added successfully!")

    elif choice=="2":
        if not tasks:
            print("No tasks found!")
        else:
            print("\n=== YOUR TASkS===")
            for i,task in enumerate(tasks,1):
                print(i,task["name"],"-",task["status"])
    elif choice=="3":
        if not tasks:
            print("No task found!")
            continue
        for i,task in enumerate(tasks,1):
            print(i,task["name"],"-",task["status"])
        try:
            number=int(input("Enter task number to complete:"))

            if 1<= number >=len(tasks):
                tasks[number-1]["status"]="completed"
                print("Task completed successfully!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid nmber!")

    elif choice=="4":
        if not tasks:
            print("No tasks available!")

            continue
        for i,task in enumerate(tasks,1):
            print(i,task["name"],"-",task["status"])
            try:
                number=int(input("Enter task number to delete:"))
                if  1 <= number <= len(tasks):
                    deleted=tasks.pop(number-1)
                    print(deleted["name"],"deeted successfully!")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("please enter a valid number!")

    elif choice=="5":
        print("Thank you for using Daily Task Manager!")
        break
    else:
        print("Invalid choice!")


