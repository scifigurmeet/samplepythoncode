# Student records management
# This file contains several issues that Sonarcloud will detect

import time
from typing import List

# Global variable (code smell)
STUDENTS = {}

class student:  # Class name doesn't follow PascalCase convention
    def __init__(self, id, name, age):
        # No type hints
        # No input validation
        self.id = id
        self.name = name
        self.age = age
        self.grades = {}
        
    def add_grade(self, subject, grade):
        # Missing docstring
        # No error handling
        self.grades[subject] = grade
        print(f"Added grade {grade} for {subject}")  # Using print instead of logger
        
    def get_average(self):
        # Potential division by zero
        return sum(self.grades.values()) / len(self.grades)

def add_student(id, name, age):
    # Using global variable
    global STUDENTS
    
    # Duplicate code
    if not isinstance(age, int):
        print("Error: Age must be an integer")
        return False
    
    if age < 0:
        print("Error: Age cannot be negative")
        return False
        
    # Security issue: no input validation for id
    STUDENTS[id] = student(id, name, age)
    return True

def get_student_info(id):
    # No error handling for KeyError
    return STUDENTS[id]

def calculate_complex_grade(grades):
    # Cognitive complexity issue
    total = 0
    count = 0
    for grade in grades:
        if grade > 90:
            total += grade * 1.1
            count += 1
        elif grade > 80:
            total += grade * 1.05
            count += 1
        elif grade > 70:
            total += grade
            count += 1
        else:
            if grade > 60:
                total += grade * 0.95
                count += 1
            else:
                if grade > 50:
                    total += grade * 0.9
                    count += 1
                else:
                    total += grade * 0.85
                    count += 1
    
    # Potential division by zero
    return total / count

def get_all_students() -> List:
    # Unused variable
    timestamp = time.time()
    
    # Hard-coded password (security issue)
    db_password = "admin123"
    
    return list(STUDENTS.values())

def main():
    # Inconsistent return statements
    try:
        add_student("001", "Alice Smith", 20)
        student = get_student_info("001")  # Shadowing built-in name
        student.add_grade("Math", 95)
        return True
    except:  # Bare except clause
        print("An error occurred")
        return
        
    # Unreachable code
    print("This will never be executed")

if __name__ == "__main__":
    # Multiple issues in one file:
    # 1. Global variable usage
    # 2. Inconsistent naming conventions
    # 3. Missing type hints
    # 4. Missing error handling
    # 5. Missing documentation
    # 6. Code duplication
    # 7. Cognitive complexity
    # 8. Security issues
    # 9. Bare except clause
    # 10. Unreachable code
    # 11. Print statements instead of logging
    # 12. Potential division by zero
    # 13. Unused variables
    # 14. Hard-coded credentials
    main()
