#function2_ex.py
mainmenu = '''
            *** Function Example ***

        1. 5와 입력된 정수와의 합(함수 클로저)

        2. a * x + b식의 계산 결과(함수 클로저)

        3. total = total + a * x + b의 계산 결과(함수 클로저 )

        4. 문자열을 반대로 출력(재귀 함수)

        5. Countdown 프로그램(재귀 함수)

        6. 판매 정보 관리 프로그램

        7. 성적 처리 프로그램

        0. 종료

        select menu : '''

salemenu = '''
1. 품목 정보 등록
2. 판매 정보 등록
3. 판매 현황표 출력
0. 종료
select menu : '''

scoremenu = '''
1. 학생 정보 등록
2. 성적 정보 등록
3. 학생 정보 조회
4. 성적 일람표
0. 종료
select menu : '''

def main():
    func_dict = { 1:sumClosureMain, 2:expClosureMain, 3:totalClosureMain, \
                  4:reverseStringMain, 5:countdownMain, 6:salesMain, 7:scoreMain }
    while True:
        print( mainmenu, end = ' ' )
        selectMenu = int( input() )

        if selectMenu == 0:
            break
        elif 1 <= selectMenu <= 7:
            func_dict[ selectMenu ]()

    return

def makeSumClosure():
    number = 5

    def sumClosure( x ):
        total = number + x
        return total
    
    return sumClosure

def makeExpClosure():
    a = 3
    b = 5

    def expClosure( x ):
        result = a * x + b
        return result

    return expClosure

def makeTotalClosure():
    a = 3
    b = 5
    total = 0

    def totalClosure( x ):
        nonlocal total
        total = total + a * x + b
        return total
        
    return totalClosure

def reverseString( string, index ):
    if index <= len( string ) - 1:
        reverseString( string, index + 1 )
    if index - 1 > -1:    
        print( string[index - 1], end = '' )

    return

def countdown( count ):
    if count < 0:
        print( '발사\n' )
        return
    else:
        print( 'count down : {:<5}'.format( count ) )
        countdown( count - 1 )

def sumClosureMain():
    f = makeSumClosure()

    print( '\n' )
    number = int( input( 'Input number : ' ) )
    while number != 0:    
        print( '5 + {0:^5} = {1:<5}'.format( number, f( number ) ) )
        number = int( input( 'Input number : ' ) )
        
    return

def expClosureMain():
    f = makeExpClosure()

    print( '\n' )
    x = int( input( 'Input x : ' ) )
    while x != 0:    
        print( '3  * {0:^5} + 5 = {1:<5}'.format( x, f( x ) ) )
        x = int( input( 'Input x : ' ) )

    return

def totalClosureMain():
    f = makeTotalClosure()

    print( '\n' )
    x = int( input( 'Input x : ' ) )
    while x != 0:    
        print( '{1:^5} = {1:^5} + 3  * {0:^5} +  5'.format( x, f( x ) ) )
        x = int( input( 'Input x : ' ) )

    return

def reverseStringMain():
    print( '\n' )
    string = input( 'Input string : ' )
    while string != 'end':
        reverseString( string, 0 )
        print( '\n' )
        string = input( 'Input string : ' )
    return

def countdownMain():
    print( '\n' )
    n = int( input( 'Input n : ' ) )
    while n != 0:
        countdown( n )
        n = int( input( 'Input n : ' ) )
        
    return

def inputItem( item_dict ):
    itemInfo = []

    print( '\n' )
    item = input( 'Input item name : ' )
    price = int( input( 'Input price : ' ) )

    itemInfo.append( item )
    itemInfo.append( price )
    itemInfo.append( 0 )
    itemInfo.append( 0 )
    
    item_dict[ item ] = itemInfo
    
    return

def inputSalesInfo( sales_dict ):
    print( '\n' )
    item = input( 'Input item name : ' )
    quantity = int( input( 'Input quantity : ' ) )

    itemInfo = sales_dict.get( item )
    if itemInfo != None:
        itemInfo[2] = itemInfo[2] + quantity
        itemInfo[3] = itemInfo[1] * itemInfo[2]
    else:
        print( 'Error : {:<10} not found!!!'.format( item ) )
        
    return

def printSalesTable( sales_dict ):
    print( '\n' )
    for key in sales_dict:
        print( '{0:<10} {1:>6} {2:>3} {3:>8}'\
               .format( sales_dict[key][0], sales_dict[key][1], sales_dict[key][2], sales_dict[key][3] ) )
        
    return

def salesMain():
    func_dict = { 1:inputItem, 2:inputSalesInfo, 3:printSalesTable }
    item_dict = {}
    
    while True:
        print( salemenu, end = ' ' )
        selectMenu = int( input() )

        if selectMenu == 0:
            break
        elif 1 <= selectMenu <= 3:
            func_dict[ selectMenu ]( item_dict )
    return

SUBJECT = 3

def inputStudentInfo( student_dict ):
    studentInfo = []

    print( '\n' )
    studentID = input( 'Input student ID : ' )
    name = input( 'Input name : ' )
    department = input( 'Input department : ' )

    studentInfo.append( studentID )
    studentInfo.append( name )
    studentInfo.append( department )
    studentInfo.append( 0 )
    studentInfo.append( 0 )
    studentInfo.append( 0 )
    studentInfo.append( 0 )
    studentInfo.append( 0.0 )
    studentInfo.append( ' ' )
    
    student_dict[ studentID ] = studentInfo
    return

def inputScoreInfo( student_dict ):
    print( '\n' )
    studentID = input( 'Input student ID : ' )

    studentInfo = student_dict.get( studentID )
    if studentInfo != None:
        print( '\n{0:<5} {1:<10}'.format( studentInfo[0], studentInfo[1] ) )

        for x in range( SUBJECT ):
            subject = int( input( 'Input subject[' + str( x + 1 ) + '] : ' ) )
            studentInfo[x + 3] = subject
            studentInfo[6] = studentInfo[6] + subject

        studentInfo[7] = studentInfo[6] / SUBJECT

        if studentInfo[7] >= 90:
            studentInfo[8] = 'Excellent'
        elif studentInfo[7] <= 50:
            studentInfo[8] = 'Fail'
        else:
            studentInfo[8] = ' '
    else:
        print( 'Error : {:<10} not found!!!'.format( studentID ) )    
    return

def searchStudentInfo( student_dict ):
    print( '\n' )
    studentID = input( 'Input student ID : ' )

    studentInfo = student_dict.get( studentID )
    if studentInfo != None:
        print( '{0:<5} {1:<10} {2:<10} {3:<3} {4:<3} {5:<3} {6:<5} {7:6.2f} {8:<10}'.\
               format( studentInfo[0], \
                       studentInfo[1], \
                       studentInfo[2], \
                       studentInfo[3], \
                       studentInfo[4], \
                       studentInfo[5], \
                       studentInfo[6], \
                       studentInfo[7], \
                       studentInfo[8] ) )
    else:
        print( 'Error : {:<10} not found!!!'.format( studentID ) )    
    
    return

def printScoreTable( student_dict ):
    print( '\n' )
    for key in student_dict:
        print( '{0:<5} {1:<10} {2:<10} {3:<3} {4:<3} {5:<3} {6:<5} {7:6.2f} {8:<10}'.\
               format( student_dict[key][0], \
                       student_dict[key][1], \
                       student_dict[key][2], \
                       student_dict[key][3], \
                       student_dict[key][4], \
                       student_dict[key][5], \
                       student_dict[key][6], \
                       student_dict[key][7], \
                       student_dict[key][8] ) )
    return

def scoreMain():
    func_dict = { 1:inputStudentInfo, 2:inputScoreInfo, 3:searchStudentInfo, \
                  4:printScoreTable }
    student_dict = {}
    
    while True:
        print( scoremenu, end = ' ' )
        selectMenu = int( input() )

        if selectMenu == 0:
            break
        elif 1 <= selectMenu <= 4:
            func_dict[ selectMenu ]( student_dict )

    return
if __name__=='__main__':
    main()
