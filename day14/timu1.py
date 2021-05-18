class Chef:
    __name=None
    __age=None
    def setname(self,name):
        self.__name=name
    def getname(self):
        return  self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return  self.__age
    def zhengfan(self):
        print("爷爷在做饭")
#儿子
class Chefson(Chef):
    def chaocai(self):
        super().zhengfan()
        print("爸爸在做饭")

#孙子
class Chefgrandson(Chefson):
    #方法的重写父类
    def chaocai(self):
        print(self.getname(),"菜单1")
        super().zhengfan()
        # 方法的重写  爷类
    def zhengfan(self):
        print(self.getname(),"菜单2")

chef=Chefgrandson()#创建孙子对象
chef.setname("孙子")
chef.setage(19)
chef.zhengfan()
chef.chaocai()

