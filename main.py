class Test:
    __slots__ = []
    def __init__(self):
        self.a = 1

    def doSome(self):
        print("Do Some")

a = Test()
b = Test()
c = Test()
d = Test()

print(b.__dict__)
del b.a
print(b.__dict__)
print(c.__dict__)



