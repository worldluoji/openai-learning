from abc import ABC, abstractmethod

'''
在这个例子中，每个形状持有对一个DrawingAPI实例的引用，这使得形状可以在不修改自身代码的情况下，与不同的绘图API协同工作。
这样，如果需要添加新的绘图方式或者新的图形，只需添加新的实现类即可，符合开闭原则。
'''

# 抽象类
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

    @abstractmethod
    def draw_rectangle(self, x, y, width, height):
        pass

# 具体实现类1 - 使用简单线条绘制
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1: Drawing Circle at ({x}, {y}) with radius {radius}")

    def draw_rectangle(self, x, y, width, height):
        print(f"API1: Drawing Rectangle at ({x}, {y}) with width {width} and height {height}")

# 具体实现类2 - 使用填充效果绘制
class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2: Filling Circle at ({x}, {y}) with radius {radius}")

    def draw_rectangle(self, x, y, width, height):
        print(f"API2: Filling Rectangle at ({x}, {y}) with width {width} and height {height}")

# 抽象部分
class Shape:
    def __init__(self, drawing_api: DrawingAPI):
        self._drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass

# 具体抽象类 - 圆形
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

# 具体抽象类 - 矩形
class Rectangle(Shape):
    def __init__(self, x, y, width, height, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def draw(self):
        self._drawing_api.draw_rectangle(self._x, self._y, self._width, self._height)

# 客户端代码
if __name__ == "__main__":
    # 使用第一个绘图API
    circle1 = Circle(1, 2, 3, DrawingAPI1())
    circle1.draw()

    rectangle1 = Rectangle(1, 2, 3, 4, DrawingAPI1())
    rectangle1.draw()

    # 使用第二个绘图API
    circle2 = Circle(3, 4, 5, DrawingAPI2())
    circle2.draw()

    rectangle2 = Rectangle(3, 4, 5, 6, DrawingAPI2())
    rectangle2.draw()