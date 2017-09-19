menu='''
=====================프로그램===========================

1. 5와 입력된 정수와의 합을 구하는 함수를 함수 클로저로 작성하고
   실행하는 프로그램( 입력값이 0이면 종료 )
2. a * x + b 식을 계산하는 함수를 함수 클로저로 작성하고 실행하는
   프로그램(  a = 3, b = 5, x가 0이면 종료 )
3. total = total + a * x + b의 결과를 출력하는 함수를 함수 클로저로 작성하고
   실행 하는 프로그램( a = 3, b = 5, x가 0 이면 종료 )

4. 문자열을 반대로 출력하는 함수를 재귀 함수로 작성하고 동작하는 프로그램
   (  'end'가 입력 되면 종료 )
5. n을 입력하면 0까지 count한 후 '발사'라는 문자열을 출력하는 함수를 재귀 함수로 작성하고
   동작하는 프로그램( n이 0이면 종료 )
   
6. 품목 정보는 품목명, 단가이고, 판매 정보는 품목명, 판매 수량이며 판매 내역은 품목명, 단가,
   판매 수량, 판매 금액일 때 다음 메뉴를 이용하여 동작하는 프로그램
		1. 품목 정보 등록
		2. 판매 정보 등록
		3. 판매 현황표 출력
		0. 종료	
7. 학생 정보는 학번, 이름, 학과, 성적 정보는 학번, 3과목 점수, 성적 일람표는 학번, 이름, 학과,
   3과목 점수, 총점, 평균, 판정일 때 다음 메뉴를 이용하여 동작하는 프로그램
      		1. 학생 정보 등록
		2. 성적 정보 등록
		3. 학생 정보 조회
		4. 성적 일람표
		0. 종료
'''


def pro1():
#Prob #1
    print('Prob. #1'.center(60,'='),'\n')
    def sumbase(a):
        sum5=0
        def sumfive():
            sum5=5+a
            return sum5
        return sumfive
    n=int(input('enter number'))
    if n==0:
        exit    
    f1=(sumbase(n));
    print('{0} + 5 = {1}'.format(n,f1()))
    return
def pro2():
#Prob #2
    print('Prob. #2'.center(60,'='),'\n')
    def func(a=3, b=5):
        a; b
        def funclo(x):
            cal=a*x+b
            return cal
        
        return funclo
    n=int(input('enter number'))
    if n==0:
        exit
    f2=func()
    print('3 * {0:} + 5 = {1:<3}'.format(n,f2(n)))
    return

def pro3():
#Prob #3
    print('Prob. #3'.center(60,'='),'\n')
    def tot(a=3, b=5):
        total=0
        def totcal(x):
            nonlocal total
            total=total+a*x+b
            return total
        return totcal
    n=int(input('enter number(0:exit)'))
    f3=tot()
    while n!=0:
        print('total = total+ 3 * {0:} + 5 = {1:<3}'.format(n,f3(n)))
        n=int(input('enter number(0:exit)'))
    return


def pro4():
#Prob #4
    print('Prob. #4'.center(60,'='),'\n')
    def revstr(stri):
        if len(stri)==1:
            return stri[0]
        return stri[len(stri)-1] + revstr(stri[0:len(stri)-1])
    s=input('enter string')
    print('reverse string : {0}'.format(revstr(s)))

    
def pro5():
#Prob #5
    print('Prob. #5'.center(60,'='),'\n')
    def revcount(nc):
        print(nc)
        if nc==0:
            print('발사')
            return 0
        return revcount(nc-1)
    num=int(input('enter number(0:exit)'))
    if num==0:
        exit
    revcount(num)
    #if revcount(num)==0:
    #    exit
    return 

from collections import namedtuple

def pro6():        
#Prob #6
    print('Prob. #6'.center(60,'='),'\n')
    def menuprint():
        menu='''
1. 품목 정보 등록
2. 판매 정보 등록
3. 판매 현황표 출력
0. 종료
        '''
        menufunc={1:prodinfo,2:soldinfo,3:soldprint}
        print(menu)
        selm=int(input('select menu'))
        if selm==0:
            return 0
        menufunc[selm]()
        return
    PInfo= namedtuple('ProdInfo','name, price')
    SInfo= namedtuple('SoldInfo','name, num')
    prodinfolist=[]
    soldinfolist=[]
    soldprintlist=[]
    def prodinfo():
        #품목명, 단가
        print('품목 정보 등록')
        pname=input('product name')
        price=int(input('price'))
        produ=PInfo(pname,price)
        prodinfolist.append(produ)
        print(prodinfolist)
        return
    def soldinfo():
        # 품목명, 판매 수량
        print('판매 정보 등록')
        pname=input('prod name')
        snum=int(input('number of sold this prod'))
       # for x in soldinfolist:
        #    if x.name==pname:
         #       snum+=x.num
                
          #  else
        produ=SInfo(pname,snum)
        soldinfolist.append(produ)
        print(soldinfolist)
        return
    def soldprint():
        #품목명, 단가, 판매수량, 판매 금액
        print('판매 현황 출력')
        for x in prodinfolist:
            for y in soldinfolist:
                if x.name==y.name:
                    tot=x.price*y.num
                    print('name: {0:<5} price: {1:3} num: {2:3} tot: {3:3}'.format(x.name, x.price, y.num, tot))
        return

    while True:
        b=menuprint()
        if b==0:
            break
    return

def pro7():
#Prob #7
    print('Prob. #7'.center(60,'='),'\n')
    sinfo=namedtuple('Studentinfo','sid, name, major')
    studinfolist=[]
    gpainfo=namedtuple('StudentGPAinfo','sid, p1,p2,p3')
    gpainfolist=[]
    SUBJECT=3
    def menuprint():
        menu='''
1. 학생 정보 등록
2. 성적 정보 등록
3. 학생 정보 조회
4. 성적 일람표
0. 종료
        '''
        menufunc={1:stuinfo_insert,2:gpainfo_insert,3:stuinfo_search,4:gpa_show}
        print(menu)
        selm=int(input('select menu'))
        if selm==0:
            return 0
        menufunc[selm]()
        return
    def stuinfo_insert():
        #학번 이름 학과 
        print('학생  정보 등록')
        sid=int(input('student id:'))
        name=input('student name:')
        major=input('student major:')
        
        studinfo=sinfo(sid,name,major)
        studinfolist.append(studinfo)
        print(studinfolist)
        
        return
    def gpainfo_insert():
        #학번 3과목 점수
        print('성적 정보 등록')
        sid=int(input('student id:'))
        subjectP=[]
       
        for x in range(SUBJECT):
            point=int(input('input point'+str(x+1)+':'))
            subjectP.append(point)

        gpa=gpainfo(sid,subjectP[0],subjectP[1],subjectP[2])
        gpainfolist.append(gpa)
        return
    def stuinfo_search():
        #학번, 이름, 학과, 3과목 성적
        print('학생 정보 출력')
        for x in studinfolist:
            for y in gpainfolist:
                if x.sid==y.sid:
                    print('Student ID: {0} Name: {1} Major: {2} Subject point1: {3} Subject point2:{4} Subject point3: {5}'.format(x.sid,x.name,x.major,y.p1,y.p2,y.p3))
        return
    def gpa_show():
        #3과목 점수, 총점, 평균, 판정
        print('성적 정보 출력')
        for x in studinfolist:
            for y in gpainfolist:   
                if x.sid==y.sid:
                    tot=y.p1+y.p2+y.p3
                    avg=tot/3
                    if avg>=90:
                        re='Excellent'
                    elif avg<90 and avg>=50:
                        re='Good'
                    else:
                        re='FFFFFFFFF'
                    print('Student ID: {0} Name: {1} Major: {2} Subject point1: {3} Subject point2:{4} Subject point3: {5} Total point: {6} Average: {7} Result: {8}'.format(x.sid,x.name,x.major,y.p1,y.p2,y.p3,tot, avg,re))

        return
    while True:
        b=menuprint()
        if b==0:
            break
        
        
    return
if __name__=='__main__':
    profunc={1:pro1, 2:pro2, 3:pro3, 4:pro4, 5:pro5, 6:pro6, 7:pro7}
    while True:
        print(menu)
        selpro=int(input('select program (0: exit)')) 
        if selpro==0:
            break
       # if selpro==3:
       #     pro3()
        profunc[selpro]()
