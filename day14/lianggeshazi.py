class  Oldphoe:
    __pinpai=None
    def setpinpai(self,pinpai):
        self.__pinpai=pinpai
    def getpinpai(self):
        return self.__pinpai
    def da(self,name):
        print("正在给",name,"打电话")
class   Newphone(Oldphoe):
    def  da(self,name):
        print("语音拨号中.....名字是",name)
        super().da(name)
    def jieshao(self):
        print("品牌为",self.getpinpai(),"Good")
old = Oldphoe()
new=Newphone()
new.setpinpai("vivo")
new.jieshao()
new.da("毛爷爷")


