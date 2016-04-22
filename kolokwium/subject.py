class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def addGrade(self, grade):
        self.grades.append(grade)


    def getGrades(self):
        return self.grades

    def getName(self):
        return self.name
