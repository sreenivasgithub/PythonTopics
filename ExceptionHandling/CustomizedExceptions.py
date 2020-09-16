# rise key word best soutable for Customized Exceptions

class Vehicle(Exception):
    def __init__(self, msg):
        self.mgs = msg
class noVehicle(Exception):
    def __init__(self, msg):
        self.msg = msg

money = int(input('Enter how much money u have: '))
if money>200000:
    raise Vehicle('u have more money, choose car')
elif money<5000:
    raise noVehicle("don't think for vehicle")
else:
    print("choose bike")