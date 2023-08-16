
def foo():
    a = "ADAM"
    def foo2():
        print(a)

    return foo2()

foo()