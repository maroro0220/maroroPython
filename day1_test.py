print("1.");
speed=int(input("   speed: "))
dist=int(input("distance: "))
#speed=input("speed:")
#dist=input("distance:")
#time=dist/speed
time=eval('dist/speed')
print("    time: %2d"%(time),end='\n');
print(end='\n')
print("2.");
len=int(input("length :"))
wid=int(input("width:"))
vol=len*wid; sur=len*2+wid*2
print("volume:",vol,end='\n');
print("surround:",sur,end='\n');
print(end='\n')
print("3.");
temp=float(input("F:"))
Ctemp=(temp-32)/1.8
print("c:",Ctemp,end='\n')
print(end='\n')
print("4.");
num1=float(input("enter number1:"))
num2=float(input("enter number2:"))
summ=num1+num2; minus=num1-num2; prod=num1*num2; mok=num1//num2; nam=num1%num2;print(end='\n')

print('sum : {0:<10}\nminus : {1:<10}\nprod : {2:<10}\nmok : {3:<10}\nnam : {4:<10}'.format(summ,minus,prod,mok,nam))
#result=[summ,minus,prod,mok,nam]

#import pprint
#pprint.pprint(result,width=20, indent=4)
#print("sum : %.2f \nminus : %.2f \nprod: %.2f \nmok: %.2f \nnam: %.2f"%(summ,minus,prod,mok,nam))

#print("sum/",sum,end='\n');
#print("minus:",minus,end='\n');
#print("prod:",prod,end='\n');
#print("mok",mok,end='\n');
#print("nam",nam,end='\n');
