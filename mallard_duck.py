from fly_behavior import FlyWithWings
from duck import Duck
from quack_behavior import Quack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard Duck!")
