# Inheritance: the process of creating new class based on
#              existing class is known as inheritence
#Types3:    1 single level, 2 multi level, 3 multiple
#1 single level:

class Parent:
    def __init__(self, name, age):
        self.parent_name = name
        self.parent_age = age
        #print('parent_name: ', name)
        #print('parent_age: ', age)

    def display(self):
        print('parent Name: ',self.parent_name)
        print('parent Age: ',self.parent_age)

class Child1(Parent):
    def __init__(self, name, age, gender):
        self.child1_name = name
        self.child1_age = age
        self.child1_gender = gender
        #print('child1_name: ', name)
        #print('child1_age: ', age)
        #print('child1_gender: ', gender)
        super().__init__('Parent',50)

    def display(self):
        print('child1 Name: ', self.child1_name)
        print('child1 Age: ', self.child1_age)
        print('child1 Gender: ', self.child1_gender)
        super().display()


class Child2(Parent):
    def __init__(self, name, age, gender):
        self.child2_name = name
        self.child2_age = age
        self.child2_gender = gender
        super().__init__('Parent', 50)

    def display(self):
        print('child2 Name: ', self.child2_name)
        print('child2 Age: ', self.child2_age)
        print('child2 Gender: ', self.child2_gender)
        super().display()

#obj1 = Child1('Child1', 20, 'F')
#obj1.display()
obj2 = Child2('c2', 25, 'M')
obj2.display()