# InstanceVariable_ClassVariable_StaticVariable

class Employee:
    name = 'Sreenivas'
    age = 25
    def __init__(self, a, b, c):
        ''' Instance Variable/object level variable:
        Inside Constructor by using self, we have to declare '''
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        print('Instance Variable of A:',self.a)
        print('Instance Variable of B:',self.b)
        print('Instance Variable of C:',self.c)
    @classmethod
    def ClassVar(self):
        ''' Static variables / Class variable: Accessing class level data '''
        print('class Variable of Name: ', self.name)
        print('class Variable of Age: ', self.age)
    @staticmethod
    def addition(num1, num2):
        ''' local Variables / Method Variables: without using self,
        we are declared any variable called '''
        localVar = 'it is local variable'
        print('Local variable: ',localVar)
        #print('Addition of num1 & num2: ', num1+num2)

obj = Employee(1,2,3)
obj.display()
Employee.ClassVar()  # obj.ClassVar() and clear @classmethod decorator
Employee.addition(10,23)# obj.addition(10,23) and clear @staticmethod decorator