from unittest import TestCase, main

from students.student import Student
from college.college import College


class TestCollege(TestCase):

    def setUp(self):
        self.college = College()

        self.student1 = Student(1, "John", 80)
        self.student2 = Student(2, "Alice", 95)
        self.student3 = Student(3, "Bob", 60)
        self.student4 = Student(4, "Mike", 75)
        self.student5 = Student(5, "Anna", 90)

        self.students = [
            self.student1,
            self.student2,
            self.student3,
            self.student4,
            self.student5
        ]

        for student in self.students:
            self.college.add_student(student)

    def test_add_student(self):
        self.assertEqual(len(self.college.get_students_by_id()), 5)

    def test_add_duplicate_student(self):
        with self.assertRaises(ValueError):
            self.college.add_student(self.student1)

    def test_remove_student(self):
        self.college.remove_student(self.student1)

        self.assertNotIn(
            self.student1,
            self.college.get_students_by_id()
        )

    def test_remove_nonexistent_student(self):
        self.college.remove_student(self.student1)

        with self.assertRaises(ValueError):
            self.college.remove_student(self.student1)

    def test_get_students_by_id(self):
        result = self.college.get_students_by_id()

        self.assertEqual(
            result,
            self.students
        )

    def test_get_students_by_score(self):
        result = self.college.get_students_by_score()

        self.assertEqual(
            [student.score for student in result],
            [60, 75, 80, 90, 95]
        )

    def test_get_students_by_scores_between(self):
        result = self.college.get_students_by_scores_between(75, 90)

        self.assertEqual(
            [student.score for student in result],
            [75, 80, 90]
        )

    def test_get_students_by_scores_between_empty(self):
        result = self.college.get_students_by_scores_between(10, 30)

        self.assertEqual(result, [])

    def test_get_students_by_scores_between_all(self):
        result = self.college.get_students_by_scores_between(0, 100)

        self.assertEqual(len(result), 5)

    def test_get_students_by_scores_between_same_score(self):
        result = self.college.get_students_by_scores_between(80, 80)

        self.assertEqual(
            [student.score for student in result],
            [80]
        )


if __name__ == "__main__":
    main()