# Name: Lya Nadya | Class QF2204A

class CalUtils:
    def __init__(self):
        self.names = list()
        self.heights = list()
        self.totalStudentHeight = 0.0
        self.totalStudentCount = 0

    def calAvgHeight(self):
        f = open("listOfStudentHeight.txt","r")
        for x in f:
            self.names.append(x.split()[0])
            self.heights.append(x.split()[1])
            self.totalStudentCount += 1
            self.totalStudentHeight += float(x.split()[1])
        print(self.names)
        print(self.heights)
        print("total student is", self.totalStudentCount)
        print("total height: {:.2f}m".format(self.totalStudentHeight))
        f.close()
        avgHeight = self.totalStudentHeight/self.totalStudentCount
        print("student's average height is: {:.2f}m".format(avgHeight))
        self.add()

    def add(self):
        y = open("listOfStudentHeight.txt", "a")
        self.totalStudentCount = 0
        self.totalStudentHeight = 0
        tempName = input("Enter new student name:")
        tempHeight = 0
        while True:
            try:
                tempHeight = float(input("Enter new student height:"))
                break
            except:
                print("Please input valid height in 2 d.p")
        y.write("\n")
        y.write(tempName)
        y.write("   ")
        y.write(str(tempHeight))
        y.close()
        return(self.calAvgHeight())


task1 = CalUtils()
task1.calAvgHeight()
