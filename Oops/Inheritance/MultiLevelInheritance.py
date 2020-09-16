# MultiLevelInheritance: The process of creating a new class based on previous class

class Grandfather:
    def __init__(self, name):
        self.grand_father = name

    def display(self):
        print('Grand Father Name: ',self.grand_father)

class Father(Grandfather):
    def __init__(self, name):
        self.father = name
        super().__init__('GrandFather')

    def display(self):
        print('Father Name: ', self.father)
        super().display()

class Child(Father):
    def __init__(self, name):
        self.child = name
        super().__init__('Father')

    def display(self):
        print('Child Name: ', self.child)
        super().display()

C = Child('Child')
C.display()