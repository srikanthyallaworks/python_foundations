from typing import Final, ClassVar


class Temperature:
    def __set_name__(self, owner, name) -> None:
        self.name = f"__name{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value > 150 or value < 0:
            raise ValueError("Should be a reasonable number")
        if self.name in obj.__dict__ and obj.__dict__[self.name] is not None:
            raise TypeError("Already set")
        obj.__dict__[self.name] = value


Number = int | float


class Thermostat:

    minValue = Temperature()
    maxValue = Temperature()

    def __init__(self, minValue:Number = 0, maxValue:Number = 0):
        self.minValue = minValue
        self.maxValue = maxValue

    def __repr__(self) -> str:
        return f"Thermostat: {self.minValue} to {self.maxValue}"


def main():
    daySettings = Thermostat(68, 80)
    print(daySettings)
    # daySettings.maxValue = 50
    # print(daySettings)


if __name__ == "__main__":
    main()
