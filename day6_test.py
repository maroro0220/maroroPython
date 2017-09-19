menu='''
=====================프로그램===========================

1.계산기 프로그램 (계산기 클래스)
    (1:'+',2:'-',3:'*',4:'/', 0:end)

2. 학생 클래스를 이용하여 다음과 같이 출력하는 프로그램
'''

class Pro1:
    #Prob #1
    print('Prob. #1'.center(60,'='),'\n')
    
    def __init__(self):
        self.result=0
        self.calfunc={1:self.add,2:self.minu,3:self.prod,4:self.div}   
        self.calc={1:'+',2:'-',3:'*',4:'/'}
        self.main()

    #def start(self):
    def main(self):
          self.cal=int(input('==========select menu===========\n1: +, 2: -, 3: *, 4: /, 0: end\n'))
          self.num1=int(input('enter num1: '))
          self.num2=int(input('enter num2: '))
          print('\n{0} {1} {2} = {3:^3}'.format(self.num1,self.calc[self.cal],self.num2,self.calfunc[self.cal](self.num1,self.num2)))          
    def add(self,a,b):
        self.result=a+b
        return self.result
    def minu(self,a,b):
        self.result=a-b
        return self.result
    def prod(self,a,b):
        self.result=a*b
        return self.result
    def div(self,a,b):
        self.result=a/b
        return self.result
      
    
class Pro2():
#Prob #2
      def __init__(self):
           self.slist=[]
           print('student info ')
           self.insert()
      def insert(self):
            self.name=input('enter student name ')
            if self.name=='end':
                  print('end ')
                  exit
            else:
                  self.slist.append(self.name)
                  for x in range(3):
                        self.slist.append(int(input('subject'+ str(x) +'point')))
                  
            return self.calpoint()
      def calpoint(self):
            
            self.tot=self.slist[1]+self.slist[2]+self.slist[3]
            self.slist.append(self.tot)
            self.avg=self.tot/3
            self.slist.append(self.avg)
            if self.avg>=90:
                  self.re='excellent'
            elif self.avg>=50:
                  self.re='good'
            else:
                  self.re='FFFFFFF'
            self.slist.append(self.re)
            print('Now Insert ')
            return self.printgpa()
      def printgpa(self):
            print('{0:<5} {1:<3} {2:<3} {3:<3} {4:<5} {5:<6.2f} {6:<10}'.\
               format( self.slist[0],self.slist[1],self.slist[2],self.slist[3],self.slist[4],self.slist[5],self.slist[6]))
                        
      
            
cnt=0
s=[]

while True:
      print(menu)
      pnum=int(input('select program '))
      if pnum==1:
            c1=Pro1()
      elif pnum==2:
            if len(s)>10:
                  print('student list full ')
                  continue;            
            else:
                  s.append(Pro2())
                  print('student gpa list ')
                  for x in range(len(s)):
                        s[x].printgpa()
      elif pnum==0:
            exit
