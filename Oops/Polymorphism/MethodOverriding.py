# Polymorphism: the process of creating a new method with the same name
#               and different number of parameters in two different classes,
#               one is super class another one is sub class.


class Cricket:
    def __init__(self, name):
        self.cricketer_name = name

class Human(Cricket):
    def __init__(self, name, age, gender):
        self.human_name = name
        self.human_age = age
        self.human_gender = gender
        super().__init__(name)
obj = Human('Sreenivas', 25, 'Male')
print('Cricket: ',obj.cricketer_name)
print('Human : ',obj.human_name, obj.human_age, obj.human_gender)

