mypi=3.14
def add(a,b):
    return a+b
def area(r):
    return mypi*r*r


if __name__=='__main__':
    print(add(5,3))
    print('mypi=',mypi)
    print(area(5))
    print(__name__)

