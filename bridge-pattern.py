from abc import ABC, abstractmethod
import turtle


class Shape(ABC):

    _shapes = {}

    def __new__(cls, **kwargs):
        try:
            sides = kwargs['sides']
            new = object.__new__(cls._shapes[sides])
        except KeyError:
            raise ValueError(f'unsupported value for sides')
        return new

    def __init_subclass__(cls, **kwargs):
        sides = kwargs.pop('sides')
        if cls not in cls._shapes:
            cls._shapes[sides] = cls

    def __init__(self, **kwargs):
        self._size = kwargs.pop('size', 40)
        self._turtle = turtle.Turtle()

    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Triangle(Shape, sides=3):

    def draw(self):
        for _ in range(0, 3):
            self._turtle.forward(self._size)
            self._turtle.right(120)


class Square(Shape, sides=4):

    def draw(self):
        for _ in range(0, 4):
            self._turtle.forward(self._size)
            self._turtle.right(90)


class Circle(Shape, sides=0):

    def draw(self):
        self._turtle.circle(radius=self._size)


if __name__ == '__main__':
    from time import sleep
    t = Shape(sides=3, size=150)
    t.draw()
    sleep(5)
