class B:
    def __init__(self):
        pass

class A(B):
    def __init__(self):
        pass

a:[A] = [A(), A()] # [A]
b:[B] = [B(), B()] # [B]

b = a # [A] <= [B]
