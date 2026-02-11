import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{branch}\n")

    print("Student added successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, branch = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Branch: {branch}")
    print()


def search_student():
    roll_no = input("Enter roll number: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, branch = line.strip().split(",")
            if roll == roll_no:
                print(f"Found: {name}, {branch}\n")
                found = True
                break

    if not found:
        print("Student not found.\n")


def delete_student():
    roll_no = input("Enter roll number to delete: ")
    lines = []
    deleted = False

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            roll, _, _ = line.strip().split(",")
            if roll != roll_no:
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice\n")


menu()

  
