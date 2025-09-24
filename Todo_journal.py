from Todo import Todo
import json

LOG_FILE= "Todo_log.json"

# Function to write to the json file
def enterTodo():
    try:
        while True:
            id=input("please enter the id: ")
            if id.isdigit():
                id=int(id)
                break
            else:
                print("Please enter an Integer value: ")
        while True:
            name=input("please enter todo name: ").strip()
            if name:
                break
            else:
                print("Name of the task cannot be empty!")

        while True:
            priority=input("please enter the priority(normal,urgent): ").strip().lower()
            if priority in ("normal","urgent"):
                break
            else:
                print("Priority must be either 'normal' of 'urgent'!")
        new_todo=Todo(id,priority,name)
        with open(LOG_FILE,"a") as f:
            f.write(json.dumps(new_todo.to_dict())+"\n")
        print(new_todo)

    except OSError:
        print("WARNING: Could not write to a file")

# Function to read from the json file 

def readJournal():
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                todo=json.loads(line)
                print(f"id:{todo['id']}, priority:{todo['priority']},name:{todo['name']}")
    except FileNotFoundError:
        print("No todos yet.")
def main():
    while True:
        choice = input("\n1) Read todos\n2) Add todo\n3) Quit\n>>> ")
        if choice == "1":
            readJournal()
        elif choice == "2":
            enterTodo()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()