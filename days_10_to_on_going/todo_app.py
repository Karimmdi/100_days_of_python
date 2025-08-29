# todo_app.py

while True:
    user_choice = input("Type add, show, edit, complite, or exit to quit: ")
    match user_choice:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index , item in enumerate(todos):
                item = item.strip().title()
                print(f"{index + 1} - {item}")
        case "edit":
            number = int(input("Enter the number of the todo to edit: \n"))
            if 0 < number <= len(todos):
                number = number - 1

                new_todo = input("Enter the new todo: ")

                todos[number] = new_todo.strip()
            else:
                print("Invalid todo number.")
        case "complite":
            number = int(input("Enter the number of the todo to complite: \n"))
            if 0 < number <= len(todos):
                todos.pop(number - 1)

        case "exit":
            break
        case _:
            print("Invalid choice, please try again.")




