# print('работать тут')
class Bank:
    def __init__(self, name, balanse):
        self.__name = name
        self.__balanse = balanse

    def moneyX(self):
        new_balanse = int(input('Введите число который ходите добавить - '))
        print(self.__balanse + new_balanse)

    def __kill(self):
        self.__balanse = 0
        print('zero')

    def _jackpot(self):
        print(f"""{self.__balanse * 10}""")

    def __cygan(self, other):
        print(f'{self.__balanse + other.__balanse}')


class MathOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("+")
        return self.x + other.y

    def __sub__(self, other):
        print("-")
        return self.x - other.y

    def __mul__(self, other):
        print("*")
        return self.x * other.y

    def __truediv__(self, other):
        print("/")
        return self.x / other.y


a = 0
b = 0
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
bank = Bank('mbank', 1000)
bank2 = Bank('optima', 2000)
bank.moneyX()
bank._Bank__cygan(bank2)
bank._jackpot()
