#class_ex.py
mainmenu = '''
            *** Class Example ***

        1. 계산기 프로그램
        2. 성적 처리 프로그램
        0. 종료
        
        select menu : '''        

class Calculator:
    def __init__( self ):
        self.result = 0
        self.op = { 1:'+', 2:'-', 3:'*', 4:'/' }

    def calculate( self, number1, number2, op_select ):
        result = eval( number1 + self.op[op_select] + number2 )

        return result

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

def calculatorMain():
    op = { 1:'+', 2:'-', 3:'*', 4:'/' }
    calculator = Calculator()

    print( '\n' )
    number1 = input( 'Input number1 (0:end): ' )
    while number1 != '0':       
        number2 = input( 'Input number2 : ' )
        op_select = int( input( 'Input operator( 1:+, 2:-, 3:*, 4:/ ) : ' ) )

        if op_select == 0:
            break;
    
        result = calculator.calculate( number1, number2, op_select )

        print( '\n{0:^6} {2:^3} {1:^6} = {3:<.2f}'.format( number1, number2, op[ op_select ], result ) )
        print( '\n' )
        number1 = input( 'Input number1 (0:end): ' )
        
    return

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

def main():
    func_dict = { 1:calculatorMain, 2:scoreTableMain }
    while True:
        print( mainmenu, end = ' ' )
        selectMenu = int( input() )

        if selectMenu == 0:
            break
        elif 1 <= selectMenu <= 2:
            func_dict[ selectMenu ]()

    return         

if __name__ == '__main__':
    main()
