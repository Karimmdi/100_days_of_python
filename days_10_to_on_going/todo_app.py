# todo_app.py
import os

while True:
    user_choice = input("Type add, show, edit, complete, or exit: ").strip().lower()

    match user_choice:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            if not os.path.exists("todos.txt"):
                with open("todos.txt", "w") as file:
                    pass  # create empty file

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            if not todos:
                print("No todos yet!")
            else:
                for index, item in enumerate(todos, start=1):
                    item = item.strip().title()
                    print(f"{index}. {item}")

        case "edit":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Enter the number of the todo to edit: "))
            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ").strip() + "\n"
                todos[number - 1] = new_todo

                with open("todos.txt", "w") as file:
                    file.writelines(todos)
            else:
                print("Invalid todo number.")

        case "complete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Enter the number of the todo to complete: "))
            if 0 < number <= len(todos):
                removed = todos.pop(number - 1)

                with open("todos.txt", "w") as file:
                    file.writelines(todos)

                print(f"Todo '{removed.strip()}' completed and removed!")
            else:
                print("Invalid todo number.")

        case "exit":
            print("Goodbye 👋")
            break

        case _:
            print("Invalid choice, please try again.")