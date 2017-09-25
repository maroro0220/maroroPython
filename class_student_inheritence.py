#class_student_inheritence.py
class Student:
    COMMON_SUBJECT = 3

    def __init__( self, studentID, name, department, commonSubject ):
        self.studentID = studentID
        self.name = name
        self.department = department

        self.commonSubject = []
        for x in commonSubject:
            self.commonSubject.append( x )

        self.total = 0
        self.average = 0.0
        self.grade = ' '

    def calculate_total( self ):
        for x in self.commonSubject:
            self.total += x

    def decision_grade( self ):
        if self.average >= 90:
            self.grade = 'Excellent'
        elif self.average < 60:
            self.grade = 'Fail'
        else:
            self.grade = ' '

    def __repr__( self ):
        return '{0:<5} {1:<10} {2:<13}'.format( self.studentID, self.name, self.department ) 
            
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


if __name__ == '__main__':
    common = [ 50, 50, 50 ]
    computer = [ 50, 50 ]
    electronic = [ 70, 70, 70 ]

    computerStudent = StudentComputer( '1701', 'hong', 'computer', computer, common )
    electronicStudent = StudentElectronic( '1702', 'kim', 'electronic', electronic, common )
    
    print( computerStudent )
    print( electronicStudent )



    
    
    
