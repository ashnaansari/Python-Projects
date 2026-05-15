tasks = []

try:
    with open("tasks.txt", 'r') as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []


while True:

    print("\n-----TO DO APP------")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")
    print(" ")

    choice = input("Enter Choice : ")


# ADD Tasks
    if choice == "1":
        task = input("Enter task : ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        
        print("Task Added!!")


#   VIEW Tasks  
    elif choice == "2":
        if len(tasks) == 0:
            print("No task found")
        else:
            print("\nYour task :")
            i = 1
            for t in tasks:
                print(f'{i}. {t}')
                i += 1


# DELETE Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            print("\n Select task number to delete")
            i = 1
            for t in tasks:
                print(f'{i}. {t}')
                i += 1

            
            try:
                num = int(input("Enter number: "))

                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)

                    with open("tasks.txt", "w") as file:
                        for t in tasks:
                            file.write(t + "\n")

                    print(f"Deleted: {removed}")
                else:
                    print("Invalid number")

            except ValueError:
                print("Please enter a valid number!")


#   EXIT
    elif choice == "4":
        print("Goodbye!!")
        break

    else:
        print("Invalid Choice")


