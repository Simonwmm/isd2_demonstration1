"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_course.py
"""
import unittest
from course.course import Course
from department.department import Department

class TestClient(unittest.TestCase):
    def test_init_valid(self):
        course = Course("Intermediate Software Deveolopment", Department.COMPUTER_SCIENCE,6)
    
    def test_init_invalid_name_raises_exception(self):
        with self.assertRaises(ValueError):
            course = Course(" ", Department.COMPUTER_SCIENCE, 6)

    def test_init_valid_department_raises_excepetion(self):
        with self.assertRaises(ValueError):
            course = Course("Intermediate Software Development", "invalid", 6)
