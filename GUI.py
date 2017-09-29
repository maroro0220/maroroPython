from tkinter import *
#from Ras_module import *
import Ras_module as r
import time
class WINDOW():
      def __init__(self):
            self.win=Tk()
            self.win.title('Maroro Widget')
            self.win.geometry('400x200')

            self.label1=Label(self.win, text='select act',anchor=N)
            self.label1.pack(side=TOP)
            self.Lflag1=0
            self.Lflag2=0
            self.Mflag1=0

            self.rl=r.LED()
            self.rm=r.MOTOR()

      def led1(self,event):

            if self.Lflag1==1:

                self.button1.config(text='led1_off')
                self.rl.led_on(14)
                self.Lflga1=0

            elif self.Lflag1==0:
                self.button1.config(text='led1_on')
               # self.rl.led_off(14)
                self.Lflag1=1
            time.sleep(0.1)


      def led2(self):
            if self.Lflag2==1:
                  self.button2.config(text='led2_off')
                  self.rl.led_on(15)
                  self.Lflag2=0

            elif self.Lflag2==0:
                  self.button2.config(text='led2_on')
                  self.rl.led_off(15)
                  self.Lflag2=1

      def dcm(self):
            self.button3.config(text='motor')
            self.rm.motor_forward()

      def btn(self):

            self.button1=Button(self.win,text='led1_on',width=10,height=3)
            self.button2=Button(self.win,text='led2_on',width=10,height=3, \
                                command=self.led2)
            self.button3=Button(self.win,text='DC_Motor_on',width=10,height=3, \
                                command=self.dcm)
            
            self.button1.pack(side=TOP)
            self.button2.pack(side=TOP)
            self.button3.pack(side=TOP)
            self.button1.bind("<ButtonRelease>",self.led1)
            self.win.mainloop()

if __name__=='__main__':
      w=WINDOW()
      w.btn()
