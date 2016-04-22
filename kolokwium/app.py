import recordBuilder
import dataWriter
import student
import subject
import gradeBook
'''rb = recordBuilder.RecordBuilder()

rb.readData()'''

aa = dataWriter.DataWriter('grades.txt')
grades = aa.readNamesAndGrades()

gr = gradeBook.GradeBook()
for line in grades:
    a  = line.split()
    std = None
    sub = None
    for k in range(0,len(a)):
        if k==0:
            std = student.Student(str(a[k]))
        elif k> 0 and aa.checkIfFloat(a[k]):
            sub.addGrade(float(a[k]))
            #print a[k]
        else:
            if sub is not None:
                std.addSubject(sub)
                std.getSubjects()
            sub = subject.Subject(str(a[k]))

            #print str(a[k])
                    #namesAndGrades.pop(line.split)

    gr.addStudent(std)

print gr.getGradeBook()