class Course:
    __name = ''
    __id = ''
    
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__id
    
    def Print(self):
        print(self.__id + '|' + self.__name)
    
class Student(Course):
    __DateofBirth = '0/0/0'
    __PointDic = {
    }
    
    def __init__(self, name, id, dob):
        super().__init__(name, id)
        self.__DateofBirth = dob
        
    def getPoint(self):
        return self.__PointDic
    
    def getDob(self):
        return self.__DateofBirth
    
    def Print(self):
        print(self.getID() + '|' + self.getName() + '|' + self.getDob())
    
    def PointUpdate(self, CourseID, CoursePoint):
        self.__PointDic.update({CourseID : CoursePoint})
        
class Manager:
    __StudentList = []
    __CourseList = []
    
    def init_Course(self, name, id ):
        C1 = Course(name,id)
        self.__CourseList.append(C1)
    
    def fix(self):
        for e in self.__StudentList:
            for x in self.__CourseList:
                e.PointUpdate(x.getName(), 0.0)
    
    def init_Studnet(self,name, id, DateOfBirth):
        S1 = Student(name, id, DateOfBirth)
        self.__StudentList.append(S1)
    
    def AddStudent(self):
        i = int(input('Enter Number of the Studnet: '))
        for x in range(i):
            self.init_Studnet(self, input('Name: '), input('ID: '), input('Date of Birth: '))
        self.fix(self)
    
    def AddCourse(self):
        i = int(input('Enter Number of the Course: '))
        for x in range(i):
            self.init_Course(self, input('Name: '),input('ID: '))
    
    def listCourse(self):
        for element in self.__CourseList:
            element.Print()
            
    def ListStudent(self):
        for element in self.__StudentList:
            element.Print()
    
    def UpdateScore(self):
        self.listCourse(self)
        str_input = input('Enter Course ID: ')
        
        for element in self.__CourseList:
            if element.getID() == str_input:
                for std in self.__StudentList:
                    f_input = input('Enter Mark for ' + std.getName() + ': ')
                    std.PointUpdate(element.getName(), f_input)
    
    def ListMark(self):
        for x in self.__CourseList:
            print(x.getName() + '|' , end="")
            print()
        for element in self.__StudentList:
            temp = element.getPoint()
            for x in self.__CourseList:
                print(x.getName())
                print(temp[x.getName()], end="|")
                    
MasterManger = Manager
Manager.AddCourse(MasterManger)
Manager.AddStudent(MasterManger)
Manager.UpdateScore(MasterManger)
Manager.ListMark(MasterManger)
    
            