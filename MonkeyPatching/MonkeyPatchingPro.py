# MonkeyPatching: having capability of changing the behaviour at runtime

class Test:
    def class_method(self):
        print('class method')

def monkey_method():
    print('monkey method')

#Test().class_method()
Test.class_method = monkey_method()
Test.class_method