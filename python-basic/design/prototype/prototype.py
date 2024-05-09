
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class ShapePrototype(Prototype):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def clone(self):
        # type(self) 这里就是Circle或者Square
        return type(self)(self.shape_type)

class Circle(ShapePrototype):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle with radius {self.radius}")

class Square(ShapePrototype):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def draw(self):
        print(f"Drawing Square with side {self.side}")


'''
ShapePrototype是一个抽象基类，定义了所有形状共有的克隆方法。Circle和Square类继承自ShapePrototype，并实现了具体的形状属性和绘制方法。
通过调用clone方法，我们可以创建这些形状的新实例，这些新实例是原始实例的副本，具有相同的属性，但位于不同的内存地址，因此是独立的对象。
这样，我们就实现了原型模式，利用原型实例来高效地创建具有相同或相似属性的新对象。
'''
if __name__ == "__main__":
    original_circle = Circle(5)
    cloned_circle = original_circle.clone()
    cloned_circle.draw()  # 输出: Drawing Circle with radius 5

    original_square = Square(10)
    cloned_square = original_square.clone()
    cloned_square.draw()  # 输出: Drawing Square with side 10