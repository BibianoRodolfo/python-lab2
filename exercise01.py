temp = 0
todo =[]
while temp < 1:
    print(" ")
    print("1- insert new task")
    print("2- remove a task")
    print("3- show tasks")
    print("4- close the program")
    print("choose a task: ")
    aux = int(input())

    if aux == 1:
        print ("write the new task:")
        todo.append(input())
    elif aux == 2:
        print(todo)
        print("write the task to remove")
        todo.remove(input())
    elif aux == 3:
        print(sorted(todo))
    elif aux == 4:
        temp = 1





