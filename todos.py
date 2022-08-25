def print_begin():
    header = """
      _____         _           
     |_   _|__   __| | ___  ___ 
       | |/ _ \ / _` |/ _ \/ __|
       | | (_) | (_| | (_) \__ \\
       |_|\___/ \__,_|\___/|___/
    """
    print(header)
    print("*" * 35)


def print_todos(lst):
    for i in range(len(lst)):
        print(f"{i+1}) {lst[i]}")


def print_completed_todos(lst):
    print(f"Today you completed {len(lst)} todos:")
    for el in lst:
        print(f"* {el}")


def print_help():
    print("TODO LIST HELP")
    print("Type 'q' to quit")
    print("To add a todo to the list, type it and hit enter")
    print("To complete a todo enter its number")


def start_to_do():
    print_begin()

    to_do_list = []
    completed_list = []

    print("Enter a command. Type 'h' for help:")
    command = input("> ")

    while True:
        if command == "h":
            print_help()
        elif command in ("q", "quit"):
            print_completed_todos(completed_list)
            break
        elif command.isnumeric():
            idx = int(command) - 1
            if idx >= len(to_do_list) or idx <= 0:
                print("Not in list")
            else:
                completed_list.append(to_do_list.pop(idx))
            print_todos(to_do_list)
        else:
            to_do_list.append(command)
            print_todos(to_do_list)
        print("Enter a command. Type 'h' for help:")
        command = input("> ")


if __name__ == '__main__':
    start_to_do()