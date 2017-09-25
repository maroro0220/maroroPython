class Student:
      def __init__(self,ID, name, major)
            self.id=ID
            self.name=name
            self.major=major
      def common(self):
            

class MajorPoint(Student):
      def __init__(self,ID,name,major, clist):
            super().__init__(self,ID,name,major)
            self.mlist=[]
            self.clist=clist
            self.Comcnt=2
            self.Electcnt=3
      def mpoint(self):
            if Student.major=='computer':
                  for x in range(self.Comcnt):
                        majorp=int(input('enter major point'))
                        mlist.append(majorp)
            elif Student.major=='Electronic':
                  for x in range(self.Electcnt):
                        majorp=int(input('enter major point'))
                        mlist.append(majorp)
            
                        
class ViewScoreTable:
      MAX=10
      count=0
      def __init__(self):
            self.
      def ViewMenu(self):

      def inputStudentInfo(self):
            print('\n')
            sid=int(input('enter ID number'))
            name=input('enter name')
            major=input('enter major')
            while name!='end' and self.count<=self.MAX:
                  


