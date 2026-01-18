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

def save_data(filename, data):
    """Saves student data to CSV file.""" 
    try:
        with open(f"{filename}", 'w') as file:
            writer = csv.writer(file)
            for student in data:
                writer.writerow([student['id'], student['name'], student['score']])
        print("Data saved.")
    except:
        print("Error in saving")


def determine_grade(score):
    """Returns Pass or Fail based on score."""
    if score > 40:
        return "Pass"
    else:
        return "Fail"

def add_student(data):
    """Adds a new student to the list."""
    print("\n--- Add New Student ---")
    s_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    
    while True:
        try:
            score = int(input("Enter Score (0-100): "))
            break
        except:
            print("Invalid Score")

    new_student = {'id': s_id, 'name': name, 'score': score}
    data.append(new_student)
    
    print(f"Student {name} added!")

def view_students(data):
    """Displays all students."""
    print("\n--- Student List ---")
    print(f"{'ID':<10} {'Name':<20} {'Score':<10} {'Result':<10}")
    print("-" * 50)
    for s in data:
        result = determine_grade(s['score'])
        print(f"{s['id']:<10} {s['name']:<20} {s['score']:<10} {result:<10}")

def module_statistics(data):
    score_list = []
    highest_score = []
    lowest_score = []
    temp1 = []
    temp2 = []
    total = 0
    for score in data:
        score_list.append(score["score"])
    for number in range(len(score_list)):
        total += score_list[number]
    total /= len(score_list)
    print(f" The average score is {total}")
    for i in range(len(score_list)):
        if score_list[i] < 50:
            lowest_score.append(score_list[i])
        else:
            highest_score.append(score_list[i]) 
    for j in range(len(lowest_score)):
        while len(lowest_score) > 1:
            if lowest_score[j] < lowest_score[j + 1]:
                lowest_score.remove(lowest_score[j + 1])
            else:
                lowest_score.remove(lowest_score[j])
    for j in range(len(highest_score)):
        while len(highest_score) > 1:
            if highest_score[j] > highest_score[j + 1]:
                highest_score.remove(highest_score[j + 1])
            else:
                highest_score.remove(highest_score[j])
    temp1.append(next(student for student in data if student['score'] == lowest_score[0]))
    for s in temp1:
        print(f"{s['name']} has the lowest score of {s['score']}")
    temp2.append(next(student for student in data if student['score'] == highest_score[0]))
    for s in temp2:
        print(f"{s['name']} has the highest score of {s['score']}")
    for n in range(len(temp2)):
        temp1.append(temp2[n])
    temp1.append(datetime.now())
    save_data("module_report.txt", temp1)


def main_menu(data):
    while True:
        print("\n=== GRADE MANAGER v1.1 ===")
        print("1. View Students")
        print("2. Add Student")
        print("3. View Module Statistics")
        print("4. Save & Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            view_students(data)
        elif choice == '2':
            add_student(data)
        elif choice == '3':
            module_statistics(data)
        elif choice == '4':
            save_data("STUDENT_FILE.csv", data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    data = load_data("students.csv")
    main_menu(data)