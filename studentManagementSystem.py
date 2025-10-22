students = []

def add_student(name, student_id):
    student = {"name": name, "id": student_id, "grades": {}}
    students.append(student)
    print(f"Student '{name}' added successfully!\n")

def add_grades(student_id, **subjects):
    for student in students:
        if student["id"] == student_id:
            for sub, marks in subjects.items():
                student["grades"][sub] = marks
            print(f"Grades added for student ID {student_id}.\n")
            return
    print("Student ID not found!\n")

def calculate_average(student):
    total = sum(student["grades"].values())
    count = len(student["grades"])
    if count == 0:
        return 0
    return total / count

def grade_letter(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

def print_report(student_id):
    for student in students:
        if student["id"] == student_id:
            print(f"\n--- Report for {student['name']} (ID: {student['id']}) ---")
            if not student["grades"]:
                print("No grades available.")
            else:
                for sub, marks in student["grades"].items():
                    print(f"{sub}: {marks}")
                avg = calculate_average(student)
                print(f"Average: {avg:.2f}")
                print(f"Grade: {grade_letter(avg)}")
            print("---------------------------------\n")
            return
    print("Student ID not found!\n")


def list_students():
    if not students:
        print("No students in the system.\n")
    else:
        print("All Students:")
        for student in students:
            print(f"Name: {student['name']}, ID: {student['id']}")
        print()

def main_menu():
    while True:
        print("===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. Add Grades")
        print("3. Print Student Report")
        print("4. List All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            add_student(name, student_id)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            print("Enter grades (subject and marks). Type 'done' when finished.")
            subjects = {}
            while True:
                subject = input("Subject: ")
                if subject.lower() == "done":
                    break
                try:
                    marks = float(input("Marks: "))
                    subjects[subject] = marks
                except:
                    print("Invalid marks! Enter a number.")
            add_grades(student_id, **subjects)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            print_report(student_id)
        elif choice == "4":
            list_students()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

main_menu()
