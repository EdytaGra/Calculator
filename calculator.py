import math
from math import sqrt
from typing import List


class Calculator:

    def __init__(self):
        self.basic_arithmetic_functions = {
            1: self.addition,
            2: self.subtraction,
            3: self.multiplication,
            4: self.division,
            5: self.exponentiation,
            6: self.square_root
        }
        self.basic_geometric_functions = {
            1: self.square_area,
            2: self.rectangle_area,
            3: self.triangle_area,
            4: self.circle_area
        }
        self.main_menu = {
            1: self.run_basic_arithmetic_functions,
            2: self.run_basic_geometric_functions
        }

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
        while a < 0:
            print('Incorrect number!\nPlease select a number greater than 0')
            a, = self.get_user_input(['Give a side lenght: a : '])
        return a * a

    def rectangle_area(self) -> float:
        a, b = self.get_user_input(['Give a side length: a : ', 'Give a side length: b : '])
        if a >= 1 and b >= 1:
            return a * b
        else:
            print('Incorrect number!\nPlease select a number greater than 0')
            return self.rectangle_area()

    def triangle_area(self) -> float:
        a, b = self.get_user_input(['Give a base field: ', 'Give a height of the triangle: '])
        if a >= 0.01 and b >= 0.01:
            return a * b / 2
        else:
            print('Incorrect number!\nPlease select a number greater than 0')
            return None

    def circle_area(self) -> float:
        a, = self.get_user_input(['Give a circle radius: '])
        if a >= 0.01:
            return math.pi * a ** 2
        else:
            print('Incorrect number!\nPlease select a number greater than 0')
            return -1

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

    def display_main_menu(self):

        print('1 Basic arithmetic functions menu\n2 Basic geometric functions menu\n0 Exit')

    def run_basic_arithmetic_functions(self):
        while True:
            self.display_basic_arithmetic_functions()
            try:
                user_input = int(input(f'Choose number (0 - {len(self.basic_arithmetic_functions.keys())}): '))
                result = self.basic_arithmetic_functions[user_input]()
                print(f'The result is: {result}')
                input('Press enter to continue...')
            except KeyError:
                if user_input == 0:
                    break
                else:
                    print('Incorrect option selected!')
            except ValueError:
                print('Please enter numbers only!')

    def run_basic_geometric_functions(self):
        while True:
            self.display_basic_geometric_functions()
            try:
                user_input = int(input(f'Choose number (0 - {len(self.basic_geometric_functions.keys())}): '))
                result = self.basic_geometric_functions[user_input]()
                print(f'The result is: {result}')
                input('Press enter to continue...')
            except KeyError:
                if user_input == 0:
                    break
                else:
                    print('Incorrect option selected!')
            except ValueError:
                print('Please enter numbers only!')

    def run_main_menu(self):
        while True:
            self.display_main_menu()
            try:
                user_input = int(input(f'Choose number (0 - {len(self.main_menu.keys())}): '))
                self.main_menu[user_input]()
            except KeyError:
                if user_input == 0:
                    break
                else:
                    print('Incorrect option selected!')
            except ValueError:
                print('Please enter numbers only!')

    def run(self):
        print('_____CALCULATOR_____')
        self.run_main_menu()
