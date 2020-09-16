# # Multiple Inheritance: The process of creating new class based on multiple existing classes
#
# class Father:
#     def __init__(self, name):
#         self.Father_name = name
#     def display(self):
#         print('Father name: ', self.Father_name)
#
# class Mother:
#     def __init__(self, name):
#         self.Mother_name = name
#     def display(self):
#         print('Mother name: ', self.Mother_name)
#
# class Child(Father, Mother):
#     def __init__(self, name):
#         self.Child_name = name
#         Father.__init__(self, 'Father')
#         Mother.__init__(self, 'Mother')
#     def display(self):
#         print('Child name: ', self.Child_name)
#         Father.display(self)
#         Mother.display(self)
#
# c = Child('Child')
# c.display()

class Cricket:
    def __init__(self, name):
        self.cricketer_name = name

class Footbal:
    def __init__(self, name, age):
        self.footballer_name = name
        self.footballer_age = age

class Human(Cricket, Footbal):
    def __init__(self, name, age, gender):
        self.human_name = name
        self.human_age = age
        self.human_gender = gender
        Cricket.__init__(self, name)
        Footbal.__init__(self, name, age)
obj = Human('Sreenivas', 25, 'Male')
print('Cricket: ',obj.cricketer_name)
print('Football: ',obj.footballer_name, obj.footballer_age)
print('Human : ',obj.human_name, obj.human_age, obj.human_gender)

