
# a = float(input('Give a number'))
# b = float(input('Give the second number'))
#
# operation = input('Choose an action +, -, *, /')
# if operation == '+':
#     print(a + b)
# if operation == '-':
#     print(a - b)
# if operation == '*':
#     print(a * b)
# if operation == '/':
#     print(a / b)

from calculator import Calculator

if __name__ == '__main__':
    calc = Calculator()          # stworzyłam obiekt calc typu calculator#
    calc.run()                   # na obiekcie calc wywołujemy metodę run

