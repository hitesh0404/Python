from employee import Employee

class HR(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
    def do_work(self,task):
        print("extra efforts being made from HR ", self.name)
        return super().do_work(task)
    

mohan = Employee(103,"Mohan Jodaro")
print(mohan.do_work("take interview calls"))

rashmi = HR(101,"Rashmi Thakur")
print(rashmi.do_work("take interview calls"))
class A:
    def __init__(self):
        print("Initializing A")

class B:
    def __init__(self):
        print("Initializing B")

class C(A, B):
    def __init__(self):
        super().__init__()  # Calls the __init__ of the next class in MRO (A)
        print("Initializing C")

class D(B, A):
    def __init__(self):
        super().__init__()  # Calls the __init__ of the next class in MRO (B)
        print("Initializing D")

    c_instance = C()
    print(C.__mro__)
    d_instance = D()
    print(D.__mro__)