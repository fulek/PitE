import numpy as np
class CalAverage:
    def __init__(self, gradeBook):
        self.gradeBook = gradeBook

    def printRaport(self):
        f = open('gradeBOOKreport.txt', 'w')
        for x in self.gradeBook.getGradeBook():
            f.write("Name: "+ str(x.getName())+"\n")
            print "Name: "+ str(x.getName()+"\n")
            for l in x.getSubjects():
                f.write("Subject: "+str(l.getName())+"\n")
                print "Subject: "+str(l.getName())
                f.write("Grades: \n")
                print "Grades: \n"
                mean = np.mean(l.getGrades())
                for k in l.getGrades():
                    f.write(str(k)+"\n")
                    print k

                print "Mean "+str(mean)
                f.write("Mean "+str(mean)+"\n")

        f.close()
        return
