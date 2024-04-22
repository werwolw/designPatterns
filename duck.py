from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")
