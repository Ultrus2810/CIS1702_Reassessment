import csv
import os
from datetime import datetime
 

def load_data(filename): 
    """Loads student data from CSV file.""" 
    # BUG WARNING: Logic here seems fragile 
    
    try:
        students = []
    # If file doesn't exist, we should probably handle that... currently it crashes. FIXED
        with open(filename, "r") as file:
            reader = csv.reader(file) 
            for row in reader: 
             # simple format: ID, Name, Score 
                students.append({'id': row[0], 'name': row[1], 'score': int(row[2])})
        print("Data loaded successfully.")
        return students
    except:
        print("Error in loading")

def save_data(data):
    """Saves student data to CSV file.""" 
    # BUG WARNING: Check the file mode carefully. FIXED
    with open("STUDENT_FILE.csv", 'w') as file:  
        writer = csv.writer(file) 
        for student in data: 
            writer.writerow([student['id'], student['name'], student['score']]) 
    print("Data saved.")


def determine_grade(score):
    """Returns Pass or Fail based on score.""" 
    # BUG WARNING: Something is wrong with this logic. FIXED
    if score > 40:
        return "Pass"
    else:
        return "Fail"

def add_student(data):
    """Adds a new student to the list."""
    print("\n--- Add New Student ---")
    s_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    
    # BUG WARNING: No error handling if user types "fifty" instead of 50
    score = int(input("Enter Score (0-100): "))

    new_student = {'id': s_id, 'name': name, 'score': score}
    data.append(new_student)
    
    # Note: We are adding to the list, but are we saving it?
    print(f"Student {name} added!")

def view_students(data):
    """Displays all students."""
    print("\n--- Student List ---")
    print(f"{'ID':<10} {'Name':<20} {'Score':<10} {'Result':<10}")
    print("-" * 50)
    for s in data:
        result = determine_grade(s['score'])
        print(f"{s['id']:<10} {s['name']:<20} {s['score']:<10} {result:<10}")

def main_menu(data):
    while True:
        print("\n=== GRADE MANAGER v0.1 (BETA) ===")
        print("1. View Students")
        print("2. Add Student")
        print("3. Save & Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            view_students(data)
        elif choice == '2':
            add_student(data)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    data = load_data("students.csv")
    main_menu(data)