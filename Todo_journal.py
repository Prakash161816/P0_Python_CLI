# Todo_journal.py

import json
from datetime import datetime
from Todo import Todo

LOG_FILE = "Todo_log.json"   #each line is one json object


def load_all():
    """Read todos from the file and return a list of Todo objects."""
    todos = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)  

                    #building the dictionary
                    todo = Todo(
                        id=data["id"],
                        priority=data["priority"],
                        name=data["name"],
                        done=data["done"],
                        done_at=data["done_at"]
                    )
                    todos.append(todo)
                except (json.JSONDecodeError, KeyError):
                    print("Skipped a broken line in the file.")
    except FileNotFoundError:
        pass  # file doesn’t exist yet
    return todos

def save_all(todos):
    """Rewrite the file with the list of todos."""
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        for todo in todos:
            file.write(json.dumps(todo.to_dict(), ensure_ascii=False) + "\n")

def add_todo():
    print("\nAdd a new task to your list!")

    while True:
        raw_id = input("Pick an id number for this task: ").strip()
        if raw_id.isdigit():
            todo_id = int(raw_id)
            break
        print("Please enter a number like 1, 2, 3...")

    while True:
        raw_pr = input("Priority (1=high, 2=medium, 3=low): ").strip()
        if raw_pr in {"1", "2", "3"}:
            priority = int(raw_pr)
            break
        print("Please type 1, 2, or 3.")

    name = input("What do you need to do? ").strip()
    if not name:
        print("You did not type anything. Canceling.")
        return

    new_todo = Todo(id=todo_id, priority=priority, name=name)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(new_todo.to_dict(), ensure_ascii=False) + "\n")

    print("Added to your list!")

def list_todos(kind="open"):
    todos = load_all()
    if not todos:
        print("\nYour list is empty.")
        return

    if kind == "open":
        items = [t for t in todos if not t.done]
        title = "Things left to do:"
    elif kind == "done":
        items = [t for t in todos if t.done]
        title = "Things you have finished:"
    else:
        items = todos
        title = "Everything on your list:"

    print(f"\n{title}")
    if not items:
        print("(nothing here)")
        return

    for todo in items:
        print("-", todo)

def mark_done():
    todos = load_all()
    if not todos:
        print("No tasks yet.")
        return

    open_items = [t for t in todos if not t.done]
    if not open_items:
        print("Everything is already done.")
        return

    print("\nOpen tasks:")
    for t in open_items:
        print(f"- id:{t.id}, {t.name}")

    choice = input("Enter the id of the task you finished: ").strip()
    if not choice.isdigit():
        print("That was not a number.")
        return
    target_id = int(choice)

    for t in todos:
        if t.id == target_id and not t.done:
            t.done = True
            t.done_at = datetime.now().isoformat(timespec="seconds")
            save_all(todos)
            print(" Marked as done!")
            return

    print(f"No open task found with id {target_id}.")

def delete_todo():
    todos = load_all()
    if not todos:
        print("Nothing to delete.")
        return

    print("\nAll tasks:")
    for t in todos:
        status = "done" if t.done else "open"
        print(f"- id:{t.id} ({status}) — {t.name}")

    choice = input("Enter the id to delete: ").strip()
    if not choice.isdigit():
        print("That was not a number.")
        return
    target_id = int(choice)

    new_list = [t for t in todos if t.id != target_id]
    if len(new_list) == len(todos):
        print(f"No task found with id {target_id}.")
        return

    save_all(new_list)
    print("Deleted.")

def show_stats():
    todos = load_all()
    total = len(todos)
    done = sum(1 for t in todos if t.done)
    open_count = total - done
    print(f"\nStats → total: {total}, open: {open_count}, done: {done}")


def main():
    while True:
        choice = input(
            "\nWhat do you want to do?\n"
            "1) List open tasks\n"
            "2) List completed tasks\n"
            "3) List all tasks\n"
            "4) Add a new task\n"
            "5) Mark a task as done\n"
            "6) Delete a task\n"
            "7) Show stats\n"
            "8) Quit\n>>> "
        ).strip()

        if choice == "1":
            list_todos("open")
        elif choice == "2":
            list_todos("done")
        elif choice == "3":
            list_todos("all")
        elif choice == "4":
            add_todo()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            delete_todo()
        elif choice == "7":
            show_stats()
        elif choice == "8":
            print("Bye! Have a good day!")
            break
        else:
            print("Invalid choice. Type 1-8.")

if __name__ == "__main__":
    main()
