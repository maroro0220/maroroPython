class Calculator:#Entitiy
    def __init__( self ):
        self.result = 0
        self.op = { 1:'+', 2:'-', 3:'*', 4:'/' }

    def calculate( self, number1, number2, op_select ):
        self.result = eval( number1 + self.op[op_select] + number2 )
        return self.result

class ControlCalculator:
      def __init__(self):
            self.calculator=Calculator()
            
      def calculate(self,number1,number2,op_select):
            self.result=self.calculator.calculate(number1,number2,op_select)
            return self.result
