# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def display_menu():
    print(" STUDENT RECORD SYSTEM MENU")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def add_student(students):
    name = input("Student name: ")
    try:
        student_id = int(input("Student ID: "))
        num_scores = int(input("How many scores? "))
        
        scores = []
        for i in range(1, num_scores + 1):
            score = float(input(f"Enter score {i}: "))
            scores.append(score)
            
        student_record = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        
        students.append(student_record)
        print(f'Student "{name}" added successfully.')
        
    except ValueError:
        print("Error: Invalid input. ID and scores must be numerical values.")

def display_all_students(students):
    if not students:
        print("No student records found.")
        return
        
    print("-" * 65)
    print(f"{'Name':<20} {'ID':<15} {'Scores':<20} {'Average'}")
    print("-" * 65)
    
    for student in students:
        name = student["name"]
        student_id = str(student["id"])
        scores = student["scores"]
        
        scores_str = ", ".join(f"{score:g}" for score in scores)
        
        if scores:
            average = sum(scores) / len(scores)
        else:
            average = 0.0
            
        print(f"{name:<20} {student_id:<15} {scores_str:<20} {average:.2f}")
        
    print("-" * 65)

def calculate_average_score(students):
    try:
        target_id = int(input("Enter student ID: "))
        
        for student in students:
            if student["id"] == target_id:
                scores = student["scores"]
                if scores:
                    average = sum(scores) / len(scores)
                else:
                    average = 0.0
                print(f"{student['name']}'s average score: {average:.2f}")
                return
                
        print("Error: Student ID not found in the system.")
        
    except ValueError:
        print("Error: Invalid input. Please enter a valid numerical ID.")

def main():
    students = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        print()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            calculate_average_score(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
