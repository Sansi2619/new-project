from pythonlearning import Student
import unittest
from io import StringIO
import sys

class TestStudent(unittest.TestCase):
   def test_student_details(self):
       stud = Student("Santhoshi", "B.COM")
       #self.assertEqual() Hint: Check for name equality
       #self.assertEqual() Hint: Check for qualification equality

if __name__ == '__main__':
    unittest.main()
