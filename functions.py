def get_todos(filepath='todos.txt'):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    test_todos = get_todos()
    print(test_todos)
    test_todo = input()
    test_todos2 = get_todos() + '\n'
    test_todos2.append(test_todo)
    write_todos(test_todos2)