import re


def identity(mystring):
    if '=' in mystring and ((re.search("[a-zA-Z]+", mystring)) is None):
        part1, part3 = mystring.split('=')
    else:
        print('error')
    if '+' in mystring:
        operator = '+'
    elif '-' in mystring:
        operator = '-'
    elif '*' in mystring:
        operator = '*'
    elif '/' in mystring:
        operator = '/'
    else:
        print('error')

    part1, part2 = part1.split(operator)

    if part1.isdigit() and part2.isdigit() and part3.isdigit():
        a = int(part1)
        b = int(part2)
        c = int(part3)

        foperp(operator, a, b, c)
    else:
        print('error')
        return False
    return


def foperp(operator, a, b, c):
    if (operator == '+') and (a + b == c):
        print('YES')
        return True
    elif operator == '-' and (a - b == c):
        print('YES')
        return True
    elif operator == '*' and (a * b == c):
        print('YES')
        return True
    elif operator == '/' and (a / b == c):
        print('YES')
        return True
    else:
        print('NO')
        return False


if __name__ == '__main__':
    mystring = input("input a string :")
    identity(mystring)
