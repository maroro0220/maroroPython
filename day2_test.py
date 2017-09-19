#Prob #1
print('Prob. #1'.center(30,'='),'\n')
s = 'hong gil dong201412121623210'
name=s[0:13]
year=s[13:17]
month=s[17:19]
day=s[19:21]
num=s[21:]
birth=year+'/'+month+'/'+day
IDnumber=year+month+day+' - '+num
print("Name : {0}\nBirthday : {1}\nID Number : {2}\n\n".format(name,birth,IDnumber))
#print('Name :{0} \nBirthday : {1}'.format(name,birth))

#Prob #2
print('Prob. #2'.center(30,'='),'\n')
s = 'MultiCampus'
print('s:',s)
mu=s[0:5]
cam=s[5:]
s=cam+mu
print('changed s:',s,'\n')

#Prob #3
print('Prob. #3'.center(30,'='),'\n')
s = 'hello world'
#sp=s.split()
#sp.remove('hello')
#sp.insert(0,'hi')
s='hi'+s[5:]
print(s,'\n')

#Prob #4
print('Prob. #4'.center(30,'='),'\n')

x1=int(input('x1 :'))
x2=int(input('x2 :'))
cal=int(input('Plus(+) :1, Minus(-):2, Product(*):3, Divide(/):4 '))
c=['+','-','*','/']
calc=[x1+x2,x1-x2,x1*x2,x1/x2]
print(format(x1,'3d'),c[(cal-1)],format(x2,'2d'),' = ',format(calc[cal-1],'2d'))

#Prob #5
print('Prob. #5'.center(30,'='),'\n')
n=int(input("enter integer number n:"))
l=list(range(1,n+1))
print(l)
s=sum(l)
print(s)
#Prob #6
print('Prob. #6'.center(30,'='),'\n')
n=int(input("enter integer number n:"))
lodd=list(range(1,n+1,2))
leven=list(range(2,n+1,2))
print('odd:',lodd,'\n','even:',leven,'\n')
#print(l)
so=sum(lodd)
se=sum(leven)
print('odd sum:',so,'even sum',se)

#Prob #7
print('Prob. #7'.center(30,'='),'\n')
n=int(input("enter integer number n:"))
l=[k for k in range(1,n+1) if (k%3!=0)and(k%5!=0)]
print(l)
s=sum(l)
print(s)
