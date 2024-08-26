import random
from department.department import Department

class Student:
    """
    Student class.  Represents a student in a school.
    """
    def __init__(self, student_number: int, name: str, department: Department):
        """
        Initializes a course object based on received arguments (if valid).
        args:
            student_number (int): The student's unique id.
            name (str): The name of the student.
            department (Department): The name of the department in which student is enrolled.
        raises:
            ValueError: if any of the arguments are invalid.
        """
        if isinstance(student_number, int):
            self.__student_number = student_number
        else:
            raise ValueError("Student Number must be a whole number.")

        if len(name.strip()) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be blank.")

        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError("Department must be one of the predefined Departments.")

        self.__grade_point_average = random.uniform(0, 4.5)
        
    @property
    def student_number(self) -> int:
        """
        Accessor for the student_number attribute.
        Returns: int - The unique id associated with the Student instance.
        """
        return self.__student_number

    @property
    def name(self) -> str:
        """
        Accessor for the name attribute.
        Returns: str - The name of the Student instance.
        """
        return self.__name

    @property
    def department(self) -> Department:
        """
        Accessor for the department attribute.
        Returns: Department - A specific Department enum value associated with the Student instance.
        """
        return self.__department
    
    @property
    def grade_point_average(self) -> float:
        """
        Accessor for the grade point average attribute.
        Returns: float - The grade point average value associated with the Student instance.
        """
        return self.__grade_point_average
    
    
    def __str__(self) ->str:
        """
        Returns a string representation of the Student instance.
        Returns: str - The Student instance as a formatted string.
        """
        # Note: For departments containing more than one word
        # replace the _ with a blank.
        return (f"Student: {self.__student_number}"
                + f"\nName: {self.__name}"
                + f"\nDepartment: {self.__department.name.replace('_', ' ').title()}")