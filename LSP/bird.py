class Bird:
    def fly(self):
        pass

class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class Penguin(NonFlyingBird):
    def fly(self):
        print("I can't fly")