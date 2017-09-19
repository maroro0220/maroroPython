#Prob #1
print('Prob. #1'.center(60,'='),'\n')

print('useing only for'.center(60,'-'))
for x in range(1,101):
    print(format(x,'4d'), end='')
    if x%10==0:
        print('')
#num=list(range(1,101))
print('useing list'.center(60,'-'))
#for x in num:
#    print(format(x,'5d'), end=' ')
#    if x%10==0:
 #       print('\n')
l=[k for k in range(1,101)]
start=0;
for x in range(10,101,10):
    print('{0[0]:4}{0[1]:4}{0[2]:4}{0[3]:4}{0[4]:4}{0[5]:4}{0[6]:4}{0[7]:4}{0[8]:4}{0[9]:4}'.format(l[start:x]))
    start+=10
#print(l[0:10],'\n')
#print(l[10:20],'\n')
#print(l[20:30],'\n')
#print(l[30:40],'\n')
#print(l[40:50],'\n')
#print(l[50:60],'\n')
#print(l[60:70],'\n')
#print(l[70:80],'\n')
#print(l[80:90],'\n')
#print(l[90:100],'\n')

#Prob #2
print('Prob. #2'.center(60,'='),'\n')
n=int(input('enter number'))
#num=list(range(1,n+1))

sum1=0;
for x in range(1,n+1):
    sum1+= x
print(sum1)

#Prob #3
print('Prob. #3'.center(60,'='),'\n')
n=int(input('enter number'))

sumodd=0;
sumeven=0;
for x in range(1,n+1):
    if x%2==1:
        sumodd+= x
    else :
        sumeven+=x
    print(x,end=' ');
print('\nodd sum: ',format(sumodd,'5d'),'\neven sum:',format(sumeven,'5d'))


#Prob #4
print('Prob. #4'.center(60,'='),'\n')
n=int(input('enter number'))

sum2=0;
for x in range(1,n+1):
    if x%3!=0 and x%5!=0:
        sum2+=x
    print(x,end=' ');
print('\n',format(sum2,'5d'))
#Excluding_Multiple_of_3_5.append( x )
#print( 'Excluding Multiple of 3 and 5 : ', Excluding_Multiple_of_3_5 )
#print( 'sum = {0:<6}'.format( sum( Excluding_Multiple_of_3_5 ) ) )

#Prob #5
print('Prob. #5'.center(60,'='),'\n')
print('useing only for')
for y in range(1,10):
    print(' --',y,' 단--',end='  ')
print('\n')
for x in range(1,10):
    for y in range(1,10):
        print(' ',y,'*',x,'=',format(y*x,'2d'),end=' ')
        if y==9:
            print('\n')
print('useing list')
l=[a*b for a in range(1,10) for b in range(1,10)]
start = 0
for x in range( 10, 91, 9 ):
    print( '{0[0]:3}{0[1]:3}{0[2]:3}{0[3]:3}{0[4]:3}{0[5]:3}{0[6]:3}{0[7]:3}{0[8]:3}'\
           .format( l[ start:x ] ) )
    start = start + 9
#print('1단:',l[0:9],'\n')
#print('2단:',l[9:18],'\n')
#print('3단:',l[18:27],'\n')
#print('4단:',l[27:36],'\n')
#print('5단:',l[36:45],'\n')
#print('6단:',l[45:54],'\n')
#print('7단:',l[54:63],'\n')
#print('8단:',l[63:72],'\n')
#print('9단:',l[72:81],'\n')
    
            
#Prob #6
print('Prob. #6'.center(60,'='),'\n')
n=0
cntp=0
cntn=0
odd=0
even=0
while n!=-999:
    n=int(input('enter number'))
    if n>0:
        cntp+=1
        if n%2==0:
            even+=1
        else:
            odd+=1
    elif n<0:
        cntn+=1
    else :
        print('0 is error. continue')
print('positive: ',cntp,'\nnegative:',cntn,'\neven:',even,'\nodd:',odd)


#Prob #7
print('Prob. #7'.center(60,'='),'\n')

def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a/b
sa={'+':add,'-':minus,'*':prod,'/':div}
num1=int(input('number1:'))
num2=int(input('number2:'))
s=input('what')
print(sa[s](num1,num2))

#Prob #8
print('Prob. #8'.center(60,'='),'\n')
cnt=0
table={}
name=input('name')
while name!='end' and cnt<10:
    score=[]
    for x in range(3):
        s=int(input('score'))
        score.append(s)
    score.append(sum(score))
    table[name]=score
    name=input('name')
for key in table:
    print(key, table[key])
    
