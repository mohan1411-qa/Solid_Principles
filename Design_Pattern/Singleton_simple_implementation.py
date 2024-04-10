class Singleton:
    """Whenever a class is instantiated __new__ and __init__ methods are called.
    __new__ method will be called when an object is created and __init__ method will be called to initialize
    the object. In the base class object, the __new__ method is defined as a static method which requires to
    pass a parameter cls. cls represents the class that is needed to be instantiated, and the compiler
    automatically provides this parameter at the time of instantiation."""
    _instance = None


    def __new__(cls):
        print("New instance creating")
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

s_one = Singleton()
print(s_one)
s_two = Singleton()
print(s_two)
