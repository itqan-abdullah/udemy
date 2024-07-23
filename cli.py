import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        
        todos.append(todo)
        functions.write_todos(todos)
        

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()   

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Command not valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            number = number - 1 
            removed = todos.pop(number).strip('\n')
            functions.write_todos(todos)
            print(f"Todo {removed} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not valid!")
    

print("Bye!")