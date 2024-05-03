from abc import ABC, abstractmethod

from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior


class Duck(ABC):
    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None

    @abstractmethod
    def display(self):
        pass

    def set_fly_behavior(self, fb: FlyBehavior):
        self.flyBehavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quackBehavior = qb

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")
