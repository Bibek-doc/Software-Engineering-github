# class Esewa:
#     def process_payment(self, amount):
#         return f"Processing ${amount} via Esewa"
    
# class Bankpayment:
#     def process_payment(self, amount):
#         return f"Processing ${amount } via Bank"
        
# def checkout(payment_method, amount):
#     if payment_method == "Esewa":
#         processor = Esewa()

#     elif payment_method == "Bank":
#         processor = Bankpayment()

#     else:
#         raise ValueError("Unknown payment methods used")
    
#     return processor.process_payment(amount)



class ShapeFactory:
    _registry = {}

    @classmethod
    def register(cls, name: str, shape_cls: type['Shape']) -> None:
        if not issubclass(shape_cls, Shape):
            raise TypeError("Registered class must inherit from Shape")
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create(cls, shape_type: str) -> 'Shape':
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()


def shape(name: str):
    def decorator(cls):
        ShapeFactory.register(name, cls)
        return cls
    return decorator

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass
@shape("circle")
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"

@shape("square")
class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"

@shape("triangle")
class Triangle(Shape):
    def draw(self) -> str:
        return "Drawing a Triangle"
    
@shape("rectangle")
class Rectangle(Shape):
    def draw(self) -> str:
        return "Drawing a Rectangle"
    
@shape("hexagone")
class Hexagone(Shape):
    def draw(self):
        return "Hexagon is best "

    
    
if __name__ == "__main__":
    factory = ShapeFactory

    for shape_name in ["circle", "square", "triangle", "rectangle", "hexagone"]:
        shape = factory.create(shape_name)
        print(shape.draw())

