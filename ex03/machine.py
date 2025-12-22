from beverages import *
import random


class CoffeeMachine:

    def __init__(self):
        self.uses_left = 10

    class EmptyCup(HotBeverage):

        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):

        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.uses_left = 10

    def serve(self, beverage) -> HotBeverage:
        if self.uses_left <= 0:
            raise self.BrokenMachineException()

        self.uses_left -= 1
        roll = random.randint(1, 2)

        if roll == 1:
            return beverage()
        else:
            return self.EmptyCup()


if __name__ == "__main__":
    cm = CoffeeMachine()

    try:
        while True:
            beverage = random.choice([Coffee, Tea, Chocolate, Cappuccino])
            served = cm.serve(beverage)
            print(served)
            print()
    except CoffeeMachine.BrokenMachineException as e:
        print(e)

    cm.repair()
    print()

    try:
        while True:
            beverage = random.choice([Coffee, Tea, Chocolate, Cappuccino])
            served = cm.serve(beverage)
            print(served)
            print()
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
