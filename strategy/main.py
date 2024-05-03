from fly_behavior import *
from mallard_duck import MallardDuck
from model_duck import ModelDuck

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.performFly()

    model = ModelDuck()
    model.performFly()
    model.set_fly_behavior(FlyRocketPowered())
    model.performFly()
