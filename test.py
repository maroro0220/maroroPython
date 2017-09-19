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
