class N1:
    pass

class N2(N1):
    pass

class N3(N2):
    pass

a = N2()
print(issubclass(a,N2))
