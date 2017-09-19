class Square:
      def __init__(self,end):
            self.end=end
      def __len__(self):
            return self.end
      def __getitem__(self, k):
            if type(k)==slice:
                  start=k.start or 0
                  stop=k.stop or self.end
                  step=k.step or 1
                  return map(self.__getitem__, range(start,stop,step))
            elif type(k)==int:
                  if k<0 or self.end <=k:
                        raise IndexError('index {} out of range'.format(k))
                  return k*k
            else:
                  raise TypeError('...')
class MyDict:
      def __init__(self):
            self.d={}
      def __getitem__(self,k):
            return self.d[k]
      def __setitem__(self,k,v):
            self.d[k]=v
      def __len__(self):
            return len(self.d)
      
class StringRepr:
      def __repr__(self):
            return 'repr called'
      def __str__(self):
            return 'str called'

class MyStr:
      def __init__(self,s):
            self.s=s
      def __format__(self,fmt):
            print(fmt)
            if fmt[0]=='u':
                  s=self.s.upper()
                  fmt=fmt[1:]
            elif fmt[0]=='l':
                  s=self.s.lower()
                  fmt=fmt[1:]
            else:
                  s=str(self.s)
            return s.__format__(fmt)


class Obj:
      def __init__(self, a, b):
            self.a=a
            self.b=b
      def _key(self):
            return (self.a,self.b)
      def __eq__(self,o):
            return self._key()==o._key()
      def __hash__(self):
            return hash(self._key())

class Obj2:
      def __init__( self, a, b ):
            self.a=a
            self.b= b
      def _key(self):
            return ( self.a, self.b)
      def __eq__( self, o ):
            return self._key() == o._key()
      def __hash__(self):
            return hash( self._key() )
class GetAttr1(object):
      def __getattr__( self, x ):
            print( '__getattr__', x )
            if x == 'test':
                  return 10
            raise AttributeError
class GetAttr2( object ):
      def __getattribute__( self, x ):
            print( '__getattribute__ called..', x )
            return object.__getattribute__( self, x )
            
class Attr:
      def __setattr__(self,name,value):
            print('__setattr__(%s)=%s called'%(name,value))
            object.__setattr__(self,name,value)
      def __delattr__(self,name):
            print('__delattr__(%s)called'%name)
            object.__delattr__(self,name)


class Factorial:
      def __init__(self):
            self.cache={}
      def __call__(self,n):
            if n not in self.cache:
                  if n==0:
                        self.cache[n]=1
                  else:
                        self.cache[n]=n*self.__call__(n-1)
            return self.cache[n]


class NewTest:
      def __new__(cls,*args,**kw):
            print('__new__called',cls)
            instance=object.__new__(cls)
            return instance
      def __init__(self,*args,**kw):
            print('__init__called',self)


class Super:
      def __new__(cls,*args,**kw):
            obj=object.__new__(cls)
            obj.data=[]
            return obj

class Sub(Super):
      def __init__(self,name):
            self.name=name


class Singleton:
      __instance=None
      def __new__(cls,*args,**kw):
            if cls.__instance is None:
                  cls.__instance=object.__new__(cls)
            return cls.__instance
