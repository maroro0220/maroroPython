#class_ex.py
class Student:
    SUBJECT = 3

    def __init__( self, name, subject ):
        self.name = name
        self.subject = []
        for x in subject:
            self.subject.append( x )
        self.total = 0
        self.average = 0.0
        self.grade = ' '
        
        self.calculate()

    def calculate( self ):
        for x in self.subject:
            self.total += x

        self.average = self.total / self.SUBJECT

        if self.average >= 90:
            self.grade = 'Excellent'
        elif self.average < 60:
            self.grade = 'Fail'
        else:
            self.grade = ' '

    def printStudentInfo( self ):
         print( '{0:<10}'.format( self.name ), end = '' )
         for x in self.subject:
             print( '{:<3}'.format( x ), end = '' )

         print( '{0:<5} {1:6.2f} {2:<10}'.format( self.total, self.average, self.grade ) )



def scoreTableMain():
    MAX = 10
    count = 0

    student_list = []

    print( '\n' )
    name = input( 'Input name : ' )
    while name != 'end' and count <= MAX:
        count = count + 1
        subject = []
        for x in range( Student.SUBJECT ):
            input_subject = int( input( 'Input subject[' + str( x + 1 ) + '] : ' ) )
            subject.append( input_subject )

        student = Student( name, subject )
        student_list.append( student )

        print( '\n' )
        name = input( 'Input name: ' )

    for x in student_list:
        x.printStudentInfo()
    
    return


class ControlScoreTable:
      def __init__(self, name, subject):
            self.scoreTable=Student(name, subject)
      def student(self, name, subject):
            self.scoreTable.printStudentInfo()
            

      
class ViewScoreTable:
      STUDENT=10
      count=0
      def __init__(self):
            self.controlStable=ControlScoreTable()
      def DisplayST:

      def 
            print('\n')
            self.name=input('enter name:')
            while self.name!='end' and count<=STUDENT:
                  count+=1
                  for x in range( Student.SUBJECT ):
                        input_subject = int( input( 'Input subject[' + str( x + 1 ) + '] : ' ) )
                        subject.append( input_subject )
                  student = self.controlStable.student(self,name, self.subject)
                  student_list.append( student ) print( '\n' )
                  name = input( 'Input name: ' )
                  

if __name__ == '__main__':
    viewScoreTable=ViewScoreTable()
    viewScoreTable.DisplayST
    
