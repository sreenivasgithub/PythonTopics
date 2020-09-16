class A:
    bonus = 1000

    def display_bonus(self):
        print(self.bonus)

    @classmethod
    def increment_bonus(cls):
        cls.bonus += 1000

    def increment_with_incentives(self, amount):
        print(self.bonus + amount)


obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()
obj1.display_bonus()
obj2.display_bonus()
obj3.display_bonus()
obj4.display_bonus()
obj1.increment_bonus()
print("after incrementing ...........")
obj1.display_bonus()
obj2.display_bonus()
obj3.display_bonus()
obj4.display_bonus()
obj1.increment_with_incentives(30000)
print("after incrementing  incentives...........")
obj1.display_bonus()
obj2.display_bonus()
obj3.display_bonus()
obj4.display_bonus()