try:
    print('statement1 Try block')
    try:
        print('statement2 Try block')
    except:
        print('statement2 Exception block')
    finally:
        print('statement1 Finally block')
except:
    print('statement1 Exception block')
finally:
    print('statement1 Finally block')