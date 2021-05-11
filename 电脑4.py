class Computer:
    #属性
    __screenSize=""
    __price=0.0
    __cpuModel=""
    __memSize=""
    __time=0.0
    def setscreensize(self,sets):
        self.__screenSize=sets
    def getscreensize(self):
        return  self.__screenSize
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def setcpu(self,cpu):
        self.__cpuModel=cpu
    def getprice(self):
        return self.__cpuModel

    def setmem(self, mem):
        self.__memSize = mem
    def getmem(self):
        return self.__memSize
    def settime(self, time):
        self.__time = time
    def gettime(self):
        return self.__time
    #行为
    def write(self):
        print("我是打字行为")
    def playgame(self):
        print("我是玩游戏")
    def watchTv(self):
        print("我看电视")
    def show(self):
        print("尺寸",self.__screenSize,"价格",self.__price,"cpu",self.__cpuModel,"内存",self.__memSize,"时长",self.__time)
c=Computer()
c.setscreensize("32寸")
c.setprice(119.0)
c.setcpu("3080")
c.setmem("1tb")
c.settime(193199.99)
c.show()
c.setscreensize("103寸")
print(c.getscreensize())