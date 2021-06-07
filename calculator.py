from math import sqrt


class Calculator:

    def addition(self) -> float:
        a = float(input(f'Give a number: '))
        b = float(input(f'Give a second number: '))
        return a + b

    def subtraction(self) -> float:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) - int(b)

    def multiplication(self) -> float:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) * int(b)

    def division(self) -> float:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) / int(b)

    def exponentiation(self) -> float:
        a = input(f'Give a number: ')
        b = input(f'Give second number: ')
        return int(a) ** int(b)

    def rooting(self) -> float:
        a = input(f'Give a number: ')
        return sqrt(int(a))

    def square_area(self) -> float:
        a = input(f'Give a number: ')
        return int(a) * int(a)

    def rectangle_area(self) -> float:
        a = input('Give a number:')
        b = input('Give second number:')
        return int(a) * int(b)

    def triangle_area(self) -> float:
        a = input('Give a number:')
        h = input('Give second number:')
        return int(a) * int(h) / 2

    def circle_area(self) -> float:
        a = input('Give a number:')
        return 3.14 * float(a) ** 2

    def print_available_functions(self):
        print('Menu:\n'
              '1 Addition\n'
              '2 Subtraction\n'
              '3 Multiplication\n'
              '4 Division\n'
              '5 Exponentiation\n'
              '6 Rooting\n'
              '7 Square area\n'
              '8 Rectangle area\n'
              '9 Triangle area\n'
              '10 Circle area\n'
              '0 Exit')

    def run(self):
        while True:
            self.print_available_functions()
            user_input = int(input('Choose number (0 - 10): '))
            if user_input == 1:
                print(self.addition())
            elif user_input == 2:
                print(self.subtraction())
            elif user_input == 3:
                print(self.multiplication())
            elif user_input == 4:
                print(self.division())
            elif user_input == 5:
                print(self.exponentiation())
            elif user_input == 6:
                print(self.rooting())
            elif user_input == 7:
                print(self.square_area())
            elif user_input == 8:
                print(self.rectangle_area())
            elif user_input == 9:
                print(self.triangle_area())
            elif user_input == 10:
                print(self.circle_area())
            elif user_input == 0:
                break
            else:
                print('Incorrect option selected')
