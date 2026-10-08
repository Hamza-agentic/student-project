import json
from config import APP_NAME, DEBUG
def load_student():
    with open("data/student.json", "r") as file:
        student = json.load(file)

    return student
def main():
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print()
    student = load_student()
    print("Student Information")
    print("-------------------")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Program: {student['program']}")
    print(f"Semester: {student['semester']}")
    print(f"Marks: {student['marks']}")
    
if __name__ == "__main__":
    main()