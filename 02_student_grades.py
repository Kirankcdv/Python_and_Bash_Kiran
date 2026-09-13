student = {
    "Rahul": "A",
    "Priya": "B",
    "Amit": "C",
}
while True:
    print("\n---Student Grades---")
    print("1. Add new student name")
    print("2. Update existing students grade")
    print("3. Display all students and grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ").upper()
        if name in student:
            print("Student already exists. Use option 2 to update the grade.")
        else:
            student[name] = grade
            print("Student added sucessfully")
    elif choice == "2":
        name = input("Enter student name: ")
        if name in student:
            grade = input("Enter new student grade: ").upper()
            student[name] = grade
            print("Student grade updated successfully.")
        else:
            print("Student not found.")
    elif choice == "3":
        print("\n---Student Grades---")
        for name, grade in student.items():
            print(f"{name}: {grade}")
    elif choice == "4": 
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


