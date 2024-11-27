# Global variables everywhere (multiple code smells)
STUDENTS = {}
_grades = []
pass_mark = 50
Admin_PASSWORD = "admin123"  # Security issue: Hard-coded credential
connection_string = "mongodb://admin:password123@localhost:27017"  # Another security issue

# Function with too many parameters and no type hints
def process_student_data(id, name, age, grades, contact, address, emergency_contact, medical_info, previous_school, enrollment_date, status):
    return True

# Evil exec usage (major security vulnerability)
def dynamic_grade_calculation(formula, grades):
    return exec(f"result = {formula}")

# Class with multiple issues
class data:  # Non-descriptive name, doesn't follow naming conventions
    def __init__(self, x, y):  # Non-descriptive parameter names
        self.x = x
        self.y = y
        
    def PROCESS(self):  # Inconsistent naming
        return self.x + self.y

# Function with high cyclomatic complexity and nested ifs
def calculate_final_grade(*args):  # Using *args without clear purpose
    total = 0
    count = len(args)
    
    if count > 0:
        for g in args:  # Non-descriptive variable name
            if isinstance(g, (int, float)):
                if g >= 90:
                    if g == 100:
                        total += g * 1.5
                    else:
                        total += g * 1.2
                else:
                    if g >= 80:
                        if g >= 85:
                            total += g * 1.1
                        else:
                            total += g * 1.05
                    else:
                        if g >= 70:
                            if g >= 75:
                                total += g
                            else:
                                total += g * 0.95
                        else:
                            total += g * 0.9
    
    # Potential division by zero with no error handling
    return total / count

# Class with multiple issues
class student:  # Doesn't follow PascalCase
    def __init__(self, id, name, age):
        # No validation
        self.id = id
        self.name = name
        self.age = age
        self.grades = {}
        
        # Debugging print left in code
        print(f"Created student {self.id}")
    
    # Method with multiple issues
    def add_grade(self, subject, grade):
        global _grades  # Using global
        try:
            # Nested try-except with bare except
            try:
                self.grades[subject] = grade
                _grades.append(grade)
            except:
                pass
        except:  # Bare except
            pass
        finally:
            # Redundant code
            _grades.append(grade)
            self.grades[subject] = grade

# Function with security issues
def authenticate(username, password):
    # Hard-coded credentials
    if username == "admin" and password == "secretpass123":
        return True
    return False

# Function with multiple code smells
def get_student_info(id):
    # SQL Injection vulnerability
    query = f"SELECT * FROM students WHERE id = '{id}'"
    
    # Redundant variables
    temp = None
    result = None
    data = None
    
    try:
        # Resource leak - file never closed
        f = open('log.txt', 'a')
        f.write(f"Accessed student {id}")
        
        if id in STUDENTS:
            temp = STUDENTS[id]
            result = temp
            data = result
            return data
    except:  # Bare except
        print(f"Error occurred")  # Using print for errors
        return None
    finally:
        # Unnecessary pass
        pass

# Function with multiple issues
def update_student_record(*args, **kwargs):  # Arbitrary arguments without clear purpose
    # Magic numbers
    if len(args) > 5:
        for i in range(0, 10):  # Hard-coded range
            if i == 4:
                continue
            elif i == 7:
                break
            else:
                pass  # Unnecessary pass
    
    # Unnecessary list comprehension
    result = [x for x in args if x is not None]
    
    # Unnecessary lambda
    process = lambda x: x * 2
    
    return result

# Function with bad error handling
def delete_student(id):
    # Multiple return statements
    if not id:
        return False
    elif id == "":
        return None
    else:
        try:
            # Potentially dangerous operation without proper validation
            del STUDENTS[id]
            return True
        except:  # Bare except
            return
        finally:
            # Confusing cleanup
            if 'id' in locals():
                del id

# Main execution
if __name__ == "__main__":
    # Duplicate code
    s1 = student("001", "John", 20)
    s1.add_grade("Math", 80)
    STUDENTS["001"] = s1
    
    s2 = student("002", "Jane", 21)
    s2.add_grade("Math", 85)
    STUDENTS["002"] = s2
    
    # Unnecessary comments
    # Loop through students
    for s in STUDENTS:  # Non-descriptive variable name
        # Get student
        student = STUDENTS[s]
        # Print info
        print(student.name)  # Using print instead of logging
    
    # Unreachable code
    if False:
        print("This will never execute")
    
    # Security issue: Storing sensitive data in code
    SECRET_KEY = "sk_live_123456789abcdef"
    API_KEY = "ak_live_987654321zyxwvu"
    
    # Memory leak - large object creation
    large_list = [i for i in range(1000000)]
    
    # Infinite loop with break
    while True:
        if len(STUDENTS) > 0:
            break
        else:
            continue
            
    # Dead code
    def unused_function():
        pass
    
    # Resource leak
    import os
    os.system(f"echo {s1.name}")  # Command injection vulnerability
