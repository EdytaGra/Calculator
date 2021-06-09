from math import sqrt
from typing import List


class Calculator:

    def get_user_input(self, list_of_messages: List[str]) -> List[float]:
        result = []
        for message in list_of_messages:
            result.append(float(input(message)))
        return result

    def addition(self) -> float:
        a, b = self.get_user_input(['Give a first summand: ', 'Give a second summand: '])
        return a + b

    def subtraction(self) -> float:
        a, b = self.get_user_input(['Give a minuend: ', 'Give a subtrahend: '])
        return a - b

    def multiplication(self) -> float:
        a, b = self.get_user_input(['Give a multiplicand: ', 'Give a multiplier: '])
        return a * b

    def division(self) -> float:
        a, b = self.get_user_input(['Give a dividend: ', 'Give a divisor: '])
        return a / b

    def exponentiation(self) -> float:
        a, b = self.get_user_input([' Give base of power: ', 'Give a exponent: '])
        return a ** b

    def square_root(self) -> float:
        a, = self.get_user_input(['Give a number: '])
        return sqrt(a)

    def square_area(self) -> float:
        a, = self.get_user_input(['Give a side lenght: a : '])
        return a * a

    def rectangle_area(self) -> float:
        a, b = self.get_user_input(['Give a side length: a : ', 'Give a side length: b : '])
        return a * b

    def triangle_area(self) -> float:
        a, b = self.get_user_input(['Give a base field: ', 'Give a height of the triangle: '])
        return a * b / 2

    def circle_area(self) -> float:
        a, = self.get_user_input(['Give a circle radius: '])
        return 3.14 * float(a) ** 2

    def display_basic_arithmetic_functions(self):

        print('Basic arithmetic functions menu:\n'
              '1 Addition\n'
              '2 Subtraction\n'
              '3 Multiplication\n'
              '4 Division\n'
              '5 Exponentiation\n'
              '6 Square root\n'
              '0 Exit')

    def display_basic_geometric_functions(self):

        print('Basic geometric functions menu:\n'
              '1 Square area\n'
              '2 Rectangle area\n'
              '3 Triangle area\n'
              '4 Circle area\n'
              '0 Exit')

    def run_basic_arithmetic_functions(self):
        while True:
            self.display_basic_arithmetic_functions()
            user_input = int(input('Choose number (0 - 6): '))
            if user_input == 1:
                print(f'The result is: {self.addition()}')
            elif user_input == 2:
                print(f'The result is: {self.subtraction()}')
            elif user_input == 3:
                print(f'The result is: {self.multiplication()}')
            elif user_input == 4:
                print(f'The result is: {self.division()}')
            elif user_input == 5:
                print(f'The result is: {self.exponentiation()}')
            elif user_input == 6:
                print(f'The result is: {self.square_root()}')
            elif user_input == 0:
                break
            else:
                print('Incorrect option selected')

            input('Press enter to continue...')

    def run_basic_geometric_functions(self):
        while True:
            self.display_basic_geometric_functions()
            user_input = int(input('Choose number (0 - 4): '))
            if user_input == 1:
                print(f'The result is: {self.square_area()}')
            elif user_input == 2:
                print(f'The result is: {self.rectangle_area()}')
            elif user_input == 3:
                print(f'The result is: {self.triangle_area()}')
            elif user_input == 4:
                print(f'The result is: {self.circle_area()}')
            elif user_input == 0:
                break
            else:
                print('Incorrect option selected')

            input('Press enter to continue...')

    def display_main_menu(self):
        while True:
            print('1 Basic arithmetic functions menu\n2 Basic geometric functions menu\n0 Exit')
            user_input = int(input('Choose number (1 - 2): '))
            if user_input == 1:
                self.run_basic_arithmetic_functions()
            elif user_input == 2:
                self.run_basic_geometric_functions()
            elif user_input == 0:
                break
            else:
                print('Incorrect option selected')

    def run(self):
        print('_____CALCULATOR_____    ')
        self.display_main_menu()
