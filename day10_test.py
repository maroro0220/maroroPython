#class_student_inheritence.py
SUBJECT = 3
import sqlite3
conn=sqlite3.connect("product.db")
curs=conn.cursor()
#class_struct_student.py
class Student:
    SUBJECT = 3
    def __init__( self, ids,name, major,phone, subject ):
        self.ids=ids
        self.name = name
        self.major=major
        self.phone=phone
        self.subject = []
        st=[(self.ids,self.name, self.major,self.phone)]
        for x in subject:
            self.subject.append( x )
        self.total = 0
        self.average = 0.0
        self.grade = ' '
        
        curs.executemany('insert into student values(?,?,?,?)',st)
        conn.commit()
        conn.close()
        self.calculate_total()

    def calculate_total( self ):
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

class StudentComputer( Student ):
    COMPUTER_SUBJECT = 2

    def __init__( self, studentID, name, department, commonSubject, computerSubject ):
        super().__init__(  studentID, name, department, commonSubject )
        self.computerSubject = []
        for x in computerSubject:
            self.computerSubject.append( x )

        self.calculate_total()

    def calculate_total( self ):
        super().calculate_total()

        for x in self.computerSubject:
            self.total += x
            
        self.average = self.total / ( self.COMMON_SUBJECT + self.COMPUTER_SUBJECT )
        super().decision_grade()

    def __repr__( self ):
        s = super().__repr__()
        for x in self.computerSubject:
            s += '{:<3}'.format( x )
        s += '   '
        
        for x in self.commonSubject:
            s += '{:<3}'.format( x )

        s += '{0:<5} {1:6.2f} {2:<10}'.format( self.total, self.average, self.grade )

        return s 

class StudentElectronic( Student ):
    ELECTRONIC_SUBJECT = 3

    def __init__( self, studentID, name, department, commonSubject, electronicSubject ):
        super().__init__(  studentID, name, department, commonSubject )
        self.electronicSubject = []
        for x in electronicSubject:
            self.electronicSubject.append( x )

        self.calculate_total()

    def calculate_total( self ):
        super().calculate_total()

        for x in self.electronicSubject:
            self.total += x
            
        self.average = self.total / ( self.COMMON_SUBJECT + self.ELECTRONIC_SUBJECT )
        super().decision_grade()

    def __repr__( self ):
        s = super().__repr__()
        for x in self.electronicSubject:
            s += '{:<3}'.format( x )

        for x in self.commonSubject:
            s += '{:<3}'.format( x )

        s += '{0:<5} {1:6.2f} {2:<10}'.format( self.total, self.average, self.grade )

        return s 


class ControlScoreTable:
    STUDENT = 10

    def __init__( self ):
        self.students = []
        return

    def inputStudentInfo( self, student):
        self.students.append( student)
        return
    
    def printScoreTable( self ):
        for s in self.students:
            s.printStudentInfo()
            
        return

class ViewScoreTable:
    MAX = 10
    count = 0
    
    def __init__( self ):
        self.controlScoreTable = ControlScoreTable()
        return

    def ViewManu( self ):
        self.inputStudentInfo()
        self.printStudentInfo()
        return

    def inputStudentInfo( self ):
        print( '\n' )
        self.id=int(input('input id'))
        self.name = input( 'Input name : ' )
        while self.name != 'end' and self.count <= self.MAX:
            self.count = self.count + 1
            self.subject = []
            self.major=input('input major')
            self.phone=int(input('input phone'))
           # for x in range( Student.SUBJECT ):
           #     self.input_subject = int( input( 'Input subject[' + str( x + 1 ) + '] : ' ) )
            #    subject.append( input_subject )

            student = Student(self.id, self.name,self.major,self.phone, self.subject )
            self.controlScoreTable.inputStudentInfo( student )
          #  if self.major=='computer':
                  
          #  elif self.major=='Electronic':
                  


            print( '\n' )
            name = input( 'Input name: ' )
        return

    def printScoreTable( self ):
        self.controlScoreTable.printScoreTable()
        return

if __name__ == '__main__':
    viewScoreTable = ViewScoreTable()
    viewScoreTable.ViewManu()

    
    
    
