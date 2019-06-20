import re


def calculate(number1: int, number2: int, operation: str) -> int:
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2


string = input()

rm = re.match(r'(-?\d+)([*/+-])(-?\d+)=(-?\d+)', string)
if rm:
    result = calculate(int(rm.group(1)), int(rm.group(3)), rm.group(2))
    if int(rm.group(4)) == result:
        print("Yes")
    else:
        print("No")
else:
    print("ERROR")
