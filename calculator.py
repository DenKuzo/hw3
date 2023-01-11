class MathOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("Сложение")
        return self.x + other.y

    def __sub__(self, other):
        print('Вычитание')
        return self.x - other.y

    def __mul__(self, other):
        print("Умножение")
        return self.x * other.y

    def __truediv__(self, other):
        print("Деление")
        return self.x / other.y

    # Example usage


a = MathOperations(40, 20)
b = MathOperations(20, 10)

print(a + b)
print(a - b)
print(a * b)
print(a / b)