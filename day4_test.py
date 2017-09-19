#Prob #1
print('Prob. #1'.center(60,'='),'\n')
def avg(a, b):
    return (a+b)/2
num1=0
while num1!=(-1):
    num1=int(input('enter num1'))
    if num1==-1:
        print('The end')
        break
    num2=int(input('enter num2'))
    print(avg(num1,num2))

#Prob #2
print('Prob. #2'.center(60,'='),'\n')
def M(li):
    li.sort()
    minli=min(li)
    maxli=max(li)
    return minli, maxli

l=[]
n=int(input('num'))
while n!=-1:
    if type(n)!=int:
        continue
    l.append(n)
    n=int(input('num'))

print('origin:',l)
minl,maxl=M(l)
print('sort:',l)
print('min: {0:3} max:{1:3}'.format(minl,maxl))
#Prob #3
print('Prob. #3'.center(60,'='),'\n')
def selsum(a,b):
    s=0
    for x in range(a,b+1):
        s+=x
    return s

while True:
    nums=int(input('enter start num'))
    numl=int(input('enter last num'))
    if nums>numl:
        print('The end')
        break
    print('sum {0}~{1} : {2:<10}'.format(nums,numl,selsum(nums,numl)))

#Prob #4
print('Prob. #4'.center(60,'='),'\n')
def listt(l):
    for x in range(len(l)):
        #if(type(l[x])==int):
        #    continue
        #elif(type(l[x])==str):
            l[x]=l[x][0:3]
    return l
lis=[]
while True:
    ent=input('enter anything')
    if ent=='end':
         break
    lis.append(ent)
print(lis)
print(listt(lis))

#Prob #5
print('Prob. #5'.center(60,'='),'\n')
def myrange(*arg):
        t=()
        l=[]
        cnt=0
        if len(arg)==1:
            while arg[0]>cnt:
                l.append(cnt)
                cnt+=1
        elif len(arg)==2:
            cnt=arg[0]
            while arg[1]>cnt:
                l.append(cnt)
                cnt+=1
        elif len(arg)==3:
            cnt=arg[0]
            while arg[1]>cnt:
                l.append(cnt)
                cnt+=arg[2]
        else:
            print('error')
        t=tuple(l)
        return t
nr1=int(input('enter range1 :'))
if nr1>0:
    nr2=int(input('enter range2 :'))
    if nr2>0:
        ns=int(input('enter step:'))
        if ns>0:
            print(myrange(nr1,nr2+1,ns))
        else:
            print(myrange(nr1,nr2+1))
    else:
       print(myrange(nr1+1))

        
#Prob #6
print('Prob. #6'.center(60,'='),'\n')
def add(*a):
    print(a[0])
    s=sum(a[0])
    return s
#def add(a,b):
 #   return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    num=0
    num1=0
    num2=0
    print('1.add\n2.aubtract\n3.multiply\n4.divide\n0.end')
    sel=int(input('select'))
    if sel==1:
            l=[]
            while True:
                num=int(input('enter number'))
                if num==0:
                    break
                l.append(num)
            print(add(l))
    num1=int(input('enter number1'))
    if num1>0:
        num2=int(input('enter number2'))
        if num2<0:
            print('error')
            exit
        print('{0:3}+{1:3}={2:3}'.format(num1,num2,add(num1,num2)))

    elif sel==2:
        num1=int(input('enter number1'))
        if num1>0:
            num2=int(input('enter number2'))
        if num2<0:
            print('error')
            exit
        print('{0:3}-{1:3}={2:3}'.format(num1,num2,sub(num1,num2)))
    elif sel==3:
         num1=int(input('enter number1'))
         if num1>0:
            num2=int(input('enter number2'))
         if num2<0:
            print('error')
            exit
         print('{0:3}*{1:3}={2:3}'.format(num1,num2,multi(num1,num2)))
    elif sel==4:
        num1=int(input('enter number1'))
        if num1>0:
            num2=int(input('enter number2'))
        if num2<0:
            print('error')
            exit
        print('{0:3}/{1:3}={2:3}'.format(num1,num2,div(num1,num2)))
    elif sel==0:
        break
#Prob #6-2
print('Prob. #6-2'.center(60,'='),'\n')
def add(*a):
    print(a[0])
    s=sum(a[0])
    return s
#def add(a,b):
    return a+b
#def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def f(g,a,b):
    return g(a,b)
while True:
    num=0
    num1=0
    num2=0
    print('1.add\n2.aubtract\n3.multiply\n4.divide\n0.end')
    sel=int(input('select'))
    if sel==1:
       l=[]
       while True:
           num=int(input('enter number'))
           if num==0:
               break
           l.append(num)
       print(add(l))
            
    elif sel==2:
        num1=int(input('enter number1'))
        if num1>0:
            num2=int(input('enter number2'))
        if num2<0:
            print('error')
            exit
        print('{0:3}-{1:3}={2:3}'.format(num1,num2,f(sub,num1,num2)))
    elif sel==3:
         num1=int(input('enter number1'))
         if num1>0:
            num2=int(input('enter number2'))
         if num2<0:
            print('error')
            exit
         print('{0:3}*{1:3}={2:3}'.format(num1,num2,f(multi,num1,num2)))
    elif sel==4:
        num1=int(input('enter number1'))
        if num1>0:
            num2=int(input('enter number2'))
        if num2<0:
            print('error')
            exit
        print('{0:3}/{1:3}={2:3}'.format(num1,num2,f(div,num1,num2)))

    elif sel==0:
        break


#Prob #7
print('Prob. #7-1'.center(60,'='),'\n')
t={}
def enter():
    while True:
        na=input('enter name')
        if na=='end':
            break
        p1=int(input('enter point1'))
        p2=int(input('enter point2'))
        p3=int(input('enter point3'))
        def point(name,p1,p2,p3):
            
            s=p1+p2+p3
            avg=s/3
            if avg>90:
                re='Excellent'
            elif avg<=50:
                re='Fail'
            else:
                re='good'
            t[name]=(p1,p2,p3,s,avg,re)
            return t
        d=point(na,p1,p2,p3)
    for key in d:
       print(key, d[key])
enter()


#Prob #7
print('Prob. #7-2'.center(60,'='),'\n')
t={}
def enter():
    
    cnt=0
    na=input('name')
    while na!='end' and cnt<10:
        l=[]
        for x in range(3):
            p=int(input('enter point1'))
            l.append(p)
        l.append(sum(l))
        avg=sum(l)/3
        if avg>90:
            re='Excellent'
        elif avg<=50:
            re='Fail'
        else:
            re='good'
        l.append(avg)
        l.append(re)
        t[na]=l
        na=input('enter name')

    #print(type(t))
    #print(t)
        
    for key in t:
       #print(type(t))
        print(key, t[key])
    return 


enter()

#Prob #7
print('Prob. #7-3'.center(60,'='),'\n')
t={}
def point(name,p1,p2,p3):
            
    s=p1+p2+p3
    avg=s/3
    if avg>90:
        re='Excellent'
    elif avg<=50:
        re='Fail'
    else:
        re='good'
    t[name]=(p1,p2,p3,s,avg,re)
    return t
def enter():
    while True:
        na=input('enter name')
        if na=='end':
            break
        p1=int(input('enter point1'))
        p2=int(input('enter point2'))
        p3=int(input('enter point3'))

        d=point(na,p1,p2,p3)
    return d
    
d=enter()
for key in d:
    print(key, d[key])

        
