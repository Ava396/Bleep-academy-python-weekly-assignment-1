# Q10. Student Record Management System

FILENAME = "students.txt"


def add_student():
    try:
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))

        file = open(FILENAME, "a")
        file.write(f"{name},{roll},{marks}\n")
        file.close()

        print("Student Record Added Successfully.")

    except ValueError:
        print("Invalid marks! Please enter a number.")


def view_students():
    try:
        file = open(FILENAME, "r")

        print("\n----- Student Records -----")

        for line in file:
            name, roll, marks = line.strip().split(",")
            print("Name :", name)
            print("Roll :", roll)
            print("Marks:", marks)
            print("--------------------------")

        file.close()

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    try:
        file = open(FILENAME, "r")

        found = False

        for line in file:
            name, r, marks = line.strip().split(",")

            if r == roll:
                print("\nStudent Found")
                print("Name :", name)
                print("Roll :", r)
                print("Marks:", marks)
                found = True
                break

        file.close()

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number.")