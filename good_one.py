"""
Student Management System
A simple system to manage student records with proper error handling,
documentation, and following best practices.
"""
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Student:
    """Class representing a student with their details and grades."""
    
    def __init__(self, student_id: str, name: str, age: int):
        """
        Initialize a student with their basic information.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            age: Age of the student
        
        Raises:
            ValueError: If age is negative or student_id is empty
        """
        if not student_id:
            raise ValueError("Student ID cannot be empty")
        if age < 0:
            raise ValueError("Age cannot be negative")
            
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades: Dict[str, float] = {}
        
    def add_grade(self, subject: str, grade: float) -> None:
        """
        Add or update a grade for a subject.
        
        Args:
            subject: Name of the subject
            grade: Grade value between 0 and 100
            
        Raises:
            ValueError: If grade is not between 0 and 100
        """
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
            
        self.grades[subject] = grade
        logger.info(f"Added grade {grade} for subject {subject} to student {self.student_id}")
        
    def get_average_grade(self) -> Optional[float]:
        """Calculate and return the student's average grade across all subjects."""
        if not self.grades:
            return None
            
        return sum(self.grades.values()) / len(self.grades)

class StudentManagement:
    """Class to manage multiple student records."""
    
    def __init__(self):
        """Initialize an empty student management system."""
        self.students: Dict[str, Student] = {}
        
    def add_student(self, student: Student) -> None:
        """
        Add a new student to the system.
        
        Args:
            student: Student object to be added
            
        Raises:
            ValueError: If student with same ID already exists
        """
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists")
            
        self.students[student.student_id] = student
        logger.info(f"Added new student: {student.name} (ID: {student.student_id})")
        
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieve a student by their ID.
        
        Args:
            student_id: ID of the student to retrieve
            
        Returns:
            Student object if found, None otherwise
        """
        return self.students.get(student_id)
        
    def get_top_performers(self, count: int = 3) -> List[Student]:
        """
        Get the top performing students based on average grades.
        
        Args:
            count: Number of top students to return
            
        Returns:
            List of top performing students
        """
        students_with_grades = [
            student for student in self.students.values()
            if student.get_average_grade() is not None
        ]
        
        return sorted(
            students_with_grades,
            key=lambda x: x.get_average_grade() or 0,
            reverse=True
        )[:count]

def main():
    """Example usage of the student management system."""
    system = StudentManagement()
    
    # Add some students
    try:
        student1 = Student("001", "Alice Smith", 20)
        student1.add_grade("Math", 95.0)
        student1.add_grade("Physics", 88.5)
        system.add_student(student1)
        
        student2 = Student("002", "Bob Johnson", 21)
        student2.add_grade("Math", 78.0)
        student2.add_grade("Physics", 92.0)
        system.add_student(student2)
        
        # Get and print top performers
        top_students = system.get_top_performers(2)
        for student in top_students:
            avg_grade = student.get_average_grade()
            if avg_grade is not None:
                print(f"{student.name}: {avg_grade:.2f}")
                
    except ValueError as e:
        logger.error(f"Error occurred: {str(e)}")
        
if __name__ == "__main__":
    main()
