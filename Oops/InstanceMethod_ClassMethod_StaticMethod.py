
# InstanceMethod_ClassMethod_StaticMethod

class Employee:
    name = 'Sreenivas'
    age = 25
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        ''' InstanceMethod/ object related method: inside a method
        we are accessing instance variables are called InstanceMethod '''
        print(self.a)
        print(self.b)
        print(self.c)
    @classmethod
    def ClassMethod(self):
        ''' Class Method: if we are Accessing class level data
        in a method called class method '''
        print('classMethod of Name: ', self.name)
        print('classMethod of Age: ', self.age)
    @staticmethod
    def addition(num1, num2):
        ''' StaticMethod: if we are not accessing class level
        and instance level data in a method called static method'''
        print('StaticMethod, Addition of num1 & num2: ', num1+num2)

obj = Employee(1,2,3)
obj.display()
Employee.ClassMethod()  # obj.ClassMethod() and clear @classmethod decorator
Employee.addition(10,23)# obj.addition(10,23) and clear @staticmethod decorator