class SingletonClassic:

    _instance = None

    def __init__(self):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def get_instance(cls):
        print("Get instance called -> ")

        if not cls._instance:
            cls._instance= cls.__new__(cls)

        return cls._instance

s_one = SingletonClassic.get_instance()
print(s_one)

s_two = SingletonClassic.get_instance()
print(s_two)