from abc import ABC, abstractmethod
import turtle

class Shape(ABC):

    flavors = {}

    def __new__(cls, **kwargs):
        try:
            flavor = kwargs['flavor']
            new = object.__new__(cls.flavors[flavor])
        except KeyError:
            new = object.__new__(cls)
        return new

    def __init_subclass__(cls, **kwargs):
        flavor = kwargs.pop('flavor')
        if cls not in cls.flavors:
            cls.flavors[flavor] = cls

    def __init__(self, **kwargs):
        self._size = kwargs.pop('size', 40)
        self._turtle = turtle.Turtle()

    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Triangle(Shape, flavor='triangle'):

    def draw(self):
        for _ in range(0, 3):
            self._turtle.forward(self._size)
            self._turtle.right(120)


class Square(Shape, flavor='square'):

    def draw(self):
        for _ in range(0, 4):
            self._turtle.forward(self._size)
            self._turtle.right(90)

class Circle(Shape, flavor='circle'):

    def draw(self):
        self._turtle.circle(radius=self._size)

if __name__ == '__main__':
    from time import sleep
    t = Shape(flavor='circle', size=150)
    t.draw()
    sleep(5)
