
def foo(a = 0):
    def foo2(a):
        return a+1
    return foo2

t = foo(1)

print(t)
