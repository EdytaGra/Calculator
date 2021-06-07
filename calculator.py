from typing import Union
from math import sqrt


class Calculator:

    def addition(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) + int(b)

    def subtraction(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) - int(b)

    def multiplication(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) * int(b)

    def division(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) / int(b)

    def exponentiation(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) ** int(b)

    def rooting(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        return sqrt(int(a))

    def square_area(self) -> Union[int, float]:
        a = input(f'Give a number: ')
        return int(a) * int(a)

    def rectangle_area(self) -> Union[int, float]:
        a = input('Give a number:')
        b = input('Give second number:')
        return int(a) * int(b)

    def triangle_area(self) -> Union[int, float]:
        a = input('Give a number:')
        h = input('Give second number:')
        return int(a * h) / int(2)

    def circle_area(self) -> Union[int, float]:
        a = input('Give a number:')
        return float(3.14 * float(a) ** int(2))

    def run(self):
        print('Menu :\n'
              '1 addition\n'
              '2 subtraction\n'
              '3 multiplication\n'
              '4 division\n'
              '5 exponentiation\n'
              '6 rooting\n'
              '7 square area\n'
              '8 rectangle area\n'
              '9 triangle area\n'
              '10 circle area')
        user_input = input('Choose number: ')
        if user_input == str(1):
            print(self.addition())
        elif user_input == str(2):
            print(self.subtraction())
        elif user_input == str(3):
            print(self.multiplication())
        elif user_input == str(4):
            print(self.division())
        elif user_input == str(5):
            print(self.exponentiation())
        elif user_input == str(6):
            print(self.rooting())
        elif user_input == str(7):
            print(self.square_area())
        elif user_input == str(8):
            print(self.rectangle_area())
        elif user_input == str(9):
            print(self.triangle_area())
        elif user_input == str(10):
            print(self.circle_area())

    # def triangle_area(self, x: Union[int, float], h: Union[int, float]) -> Union[int, float]:
    #    return (x * h) / 2
