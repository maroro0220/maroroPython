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
