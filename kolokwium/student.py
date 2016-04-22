class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def addSubject(self, sub):
        self.subjects.append(sub)

    def getSubjects(self):
        return self.subjects
    def getName(self):
        return self.name