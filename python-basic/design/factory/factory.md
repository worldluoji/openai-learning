# factory
Python中的工厂模式是一种创建型设计模式，其核心思想是将对象的创建过程封装起来，隐藏具体的创建逻辑，提供一个统一的接口或方法来获取所需的对象实例，而无需直接指定具体的实现类。工厂模式有助于降低代码间的耦合度，提高程序的可扩展性和灵活性。根据不同的应用场景和复杂程度，工厂模式通常有以下几种变体：

### 1. **简单工厂模式 (Simple Factory)**

简单工厂模式通常定义一个单独的类（即工厂类），这个类负责创建一系列相关或者相互依赖的对象，而不必关心具体创建的是哪个类的实例。客户端只需调用工厂类提供的静态方法或实例方法，传入必要的参数，即可得到所需类型的对象。

**示例代码：**

```python
class CarFactory:
    @staticmethod
    def create_car(brand):
        if brand == "BMW":
            return BMW()
        elif brand == "Mercedes":
            return Mercedes()
        elif brand == "Rolls Royce":
            return RollsRoyce()
        else:
            raise ValueError(f"Unsupported car brand: {brand}")

class Car:
    def __init__(self, name):
        self.name = name

    def operation(self):
        pass  # 实际操作由子类实现

class BMW(Car):
    def operation(self):
        print("Operating BMW")

class Mercedes(Car):
    def operation(self):
        print("Operating Mercedes")

class RollsRoyce(Car):
    def operation(self):
        print("Operating Rolls Royce")

# 客户端使用
car = CarFactory.create_car("BMW")
car.operation()  # 输出：Operating BMW
```

在这个例子中，`CarFactory` 类就是一个简单工厂，它接收一个参数 `brand`，并根据该参数返回相应的 `Car` 子类实例。客户端无需了解如何创建不同品牌的汽车，只需调用 `CarFactory.create_car()` 方法并传递品牌名称即可。

### 2. **工厂方法模式 (Factory Method)**

工厂方法模式将简单工厂的创建逻辑进一步抽象化，通过在抽象基类中定义一个工厂方法（通常是一个虚方法或抽象方法），将对象的创建延迟到子类中进行。这样，每个子类都可以重写工厂方法以创建特定类型的对象。

**示例代码：**

```python
from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class BMWFactory(CarFactory):
    def create_car(self):
        return BMW()

class MercedesFactory(CarFactory):
    def create_car(self):
        return Mercedes()

class RollsRoyceFactory(CarFactory):
    def create_car(self):
        return RollsRoyce()

# ... 同上定义 Car、BMW、Mercedes、RollsRoyce 类

# 客户端使用
factory = BMWFactory()
car = factory.create_car()
car.operation()  # 输出：Operating BMW
```

这里，`CarFactory` 是一个抽象基类，定义了 `create_car()` 抽象方法。每个具体的汽车品牌工厂类（如 `BMWFactory`）继承自 `CarFactory` 并实现 `create_car()` 方法以返回对应的汽车对象。客户端通过实例化特定的工厂子类来创建所需类型的汽车。

### 3. **抽象工厂模式 (Abstract Factory)**

抽象工厂模式更进一步，它不仅负责创建单个对象，而是负责创建一组相关或相互依赖的对象（即产品族）。抽象工厂提供了创建一系列相关对象的接口，而具体的产品创建则由具体子工厂实现。

**示例代码：**

```python
from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_suv(self):
        pass

class BMWFactory(CarFactory):
    def create_sedan(self):
        return BMW_Sedan()

    def create_suv(self):
        return BMW_SUV()

class MercedesFactory(CarFactory):
    def create_sedan(self):
        return Mercedes_Sedan()

    def create_suv(self):
        return Mercedes_SUV()

# ... 定义相关的汽车子类，如 BMW_Sedan、BMW_SUV、Mercedes_Sedan、Mercedes_SUV

# 客户端使用
bmw_factory = BMWFactory()
sedan = bmw_factory.create_sedan()
suv = bmw_factory.create_suv()
```

在这个例子中，`CarFactory` 是抽象工厂，它定义了创建两种类型汽车（轿车和SUV）的抽象方法。具体工厂类如 `BMWFactory` 和 `MercedesFactory` 实现这些方法，创建对应品牌的轿车和SUV。客户端通过使用某个具体工厂来创建整套相关类型的汽车。

总结来说，Python 3 中的工厂模式是一种实现对象创建解耦的重要手段，包括简单工厂模式、工厂方法模式和抽象工厂模式，它们根据复杂性和需求的不同，提供不同程度的抽象和灵活性。通过运用工厂模式，可以有效地管理对象的创建过程，使得代码更加易于维护和扩展。