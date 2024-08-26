from enum import Enum, auto

class Department(Enum):
    """
    An enumeration listing each of the departments
    in a school.
    To use:  Department.DEPARTMENT_NAME.  
    Example: Department.MEDICINE
    """
    COMPUTER_SCIENCE = auto()
    EDUCATION = auto()
    ENGINEERING = auto()
    MEDICINE = auto()


    
