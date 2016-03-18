#Store data. Save to file and tar it if #entries == 10k. Also here read data and draw plots.
import tarfile
import os
class DataStore:
    def __init__(self,flightNumber):
        self.flightNumber=flightNumber

    def openNewFile(self, number):
        #check if plane landed or open new file
        self.target = open(self.flightNumber+"_"+str(number)+".txt", 'w')

    def writeToFile(self,parameters):
        self.target.write(str(parameters))
        self.target.write("\n")

    def closeFile(self):
        self.target.close()

    def targzFile(self):
        tar = tarfile.open(self.flightNumber+".tar.gz", "w:gz")
        for name in self.findAlltextFile():
            tar.add(name)
        tar.close()
        self.removeTxt()

    def findAlltextFile(self):
        files = []
        for file in os.listdir("./"):
            if file.endswith(".txt"):
                files.append(file)
        return files

    def removeTxt(self):
        for file in os.listdir("./"):
            if file.endswith(".txt"):
                os.remove(file)
