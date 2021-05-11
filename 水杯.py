class Cup:
    __color=""
    __height=0
    __name=""
    __caizhi=""
    def setcolor(self,color):
        self.__color=color
    def getcloor(self):
        return  self.__color
    def setheight(self,height):
        self.__height=height
    def getheight(self):
        return  self.__height
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setcaizhi(self,caizhi):
        self.__caizhi=caizhi
    def getcaizhi(self):
        return self.__caizhi
    def save(self):
        print("杯子名字是",self.__name,"颜色",self.__color,"高度",self.__height,"材质",self.__caizhi)
c=Cup()
c.setcaizhi("sss+")
c.setname("飞机杯")
c.setheight(119)
c.setcolor("紫黑色")
c.save()