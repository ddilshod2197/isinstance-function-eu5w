class Test:
    pass

class Test2:
    pass

print(isinstance(Test(), Test))  # True
print(isinstance(Test(), Test2))  # False
print(isinstance(Test2(), Test))  # False
print(isinstance(Test2(), Test2))  # True
