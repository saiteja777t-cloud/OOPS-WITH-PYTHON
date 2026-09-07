class Rectangle:
    def area(self, l, b):
        print(l * b)
    def perimeter(self, l, b):
        print(2 * (l + b))
l = int(input("Enter l = "))
b = int(input("Enter b = "))
r = Rectangle()
r.area(l, b)
r.perimeter(l, b)