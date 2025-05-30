class ShapeCalculator:
    def area(self, a, b=None):
        if b is None:
            return 3.14 * a * a  #Circle
        else:
            return a * b  # Rectangle

# Usage
s = ShapeCalculator()
print("Circle area:", s.area(5))
print("Rectangle area:", s.area(5, 10))
