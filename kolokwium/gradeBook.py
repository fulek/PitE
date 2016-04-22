class GradeBook:
    def __init__(self):
        self.students = []

    def addStudent(self,student):
        self.students.append(student)

    def getGradeBook(self):
        return self.students