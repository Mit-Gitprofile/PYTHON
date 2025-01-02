student={  }

def add_student(name,grade):
    student[name]=grade
    print(f"added {name} with grade {grade} ")


def update_student(name,grade):
    if name in student:
        student[name]=grade
        print(f"updated {name} with grade {grade}")

    else:
        print(f"{name} is not found in dictionary")

def delete_student(name):
    if name in student:
        del student[name]
        print(f"deleted {name} successfully from dictionary")

    else:
        print(f"{name} is not found in dictionary")

def display_students():
    if student:
        for name,grade in student.items():
            print(f"{name}:{grade}")

    else:
        print("No students found in dictionary")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Add a student")
        print("2. Update a student")
        print("3. Delete a student")
        print("4. Display students")
        print("5. Exit")

        ch=int(input("Enter your choise:"))

        if ch==1:
            name=input("Enter student name:")
            grade=int(input("Enter student grade:"))
            add_student(name, grade)

        elif ch==2:
            name=input("Enter student name:")
            grade=int(input("Enter updated student grade:"))
            update_student(name, grade)

        elif ch==3:
            name=input("Enter student name to delete:")
            delete_student(name)

        elif ch==4:
            display_students()

        elif ch==5:
            print("programm exiting...")
            break

        else:
            print("Invalid choise!")    

main()        