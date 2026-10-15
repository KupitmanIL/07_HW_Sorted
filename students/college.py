from sortedcontainers import SortedSet, SortedKeyList

from students.student import Student


class College:
    def __init__(self, name: str):
        self._students = SortedSet()
        self._students_by_score = SortedKeyList(key=lambda s:(s.score, s.id))

    def add_student(self, student):
        if student in self._students:
            raise ValueError(f"Student {student} already exists")
        self._students.add(student)
        self._students_by_score.add(student.score)

    def remove_student(self, student):
        if student in self._students:
            raise ValueError(f"Student {student} does not exists")
        self._students.remove(student)
        self._students_by_score.remove(student.score)

    def get_students_by_id(self):
        return  list(self._students)

    def get_students_by_score(self):
        return  list(self._students_by_score)

    def get_students_by_scores_between(self, min_score, max_score):
        return list(self._students_by_score.irange_key(min_score, max_score))