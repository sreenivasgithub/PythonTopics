# Exception: Unfortunately disturb a normal flow of a program
# Exception Handling: Defining alternative way to continue rest of program
# Try: Hard code
# Except: Error handling
# Finally: it will always execute either the Exception raised or not,
#          and we can terminate that finally block using os._exit(0)

try:
    print(5/0)
except Exception as e:
    print(type(e).__name__)
finally:
    print('Operation closed')