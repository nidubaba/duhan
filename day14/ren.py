class Person:
    __age=None
    __sex=None
    __name=None
    def setage(self,age):
        self.__age=age
    def setsex(self,sex):
        self.__sex=sex
    def setname(self,name):
        self.__name=name
    def getage(self):
        return self.__age
    def getsex(self):
        return self.__sex
    def getname(self):
        return self.__name

class  Worker(Person):
    def ganhuo(self,):
        print(self.getname(),"在上班")
class Student(Person):
    def study(self):
        print(self.getname(),"在搬砖")
    def sing(self):
        print(self.getname(),"在ktv")
a=Student()
a.setname("卑微人")
a.study()
a.sing()