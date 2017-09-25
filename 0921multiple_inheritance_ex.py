class Person:
      def __init__(self,name,phone=None):
            self.name=name
            self.phone=phone
      def __repr__(self):
            return 'name={} tel={} '.format(self.name,self.phone)
class Job:
      def __init__(self,position,salary):
            self.position=position
            self.salary=salary
      def __repr__(self):
            return ' position={} salar{} '.format(self.position, self.salary)
class Employee(Person,Job):
      def __init__(self,name,phone,position,salary):
            Person.__init__(self,name,phone)
            Job.__init__(self,position,salary)
      def raisesalary(self,rate):
            self.salary=self.salary*rate
      def __repr__(self):
            return Person.__repr__(self)+''+Job.__repr__(self)
if __name__=='__main__':
      e=Employee('jong',5244,'prof',300)
      e.raisesalary(1.5)
      print(e)
      
