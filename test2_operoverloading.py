class MyStr:
      def __init__(self,s):
            self.s=s
      def __truediv__(self,b):
            return self.s.split(b)
      def __add__(self,b):
            return self.s+b
      def __radd__(self,b):
            return b+self.s
      def __iadd__(self,b):
            self.s+=b
            return self.s
class Square:
      def __init__(self,end):
            self.end=end
      def __len__(self):
            return self.end
      def __getitem__(self,k):
            if type(k) !=int:
                  raise TypeError('_')
            if k<0 or self.end <=k:
                  raise IndexError('index {} out of range'.format(k))
            k=k+1
            return k*k
      def __setitem__(self,k,value):
            return value
      
