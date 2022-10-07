class Base(object):
    def __init__(self):
        print("Base initiated")

class ChildA(Base):
    def __init__(self):
        print("Child A Initiated")
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        print("Child B Initiated")
        super().__init__()

class UserDependency(Base):
    def __init__(self):
        print("UserDependency Initiated")
        super().__init__()
    
class UserA(ChildA, UserDependency):
    def __init__(self):
        print("User A initiated")
        super().__init__()

class UserB(ChildB, UserDependency):
    def __init__(self):
        print("User B initiated")
        super().__init__()

UserA()
UserB()