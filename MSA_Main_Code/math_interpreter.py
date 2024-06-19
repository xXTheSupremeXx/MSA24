def main():
    while True:
        expression = input("Expression: ").split(' ')   
        try:
            x = int(expression[0])
            y = expression[1]
            z = int(expression[2])

            if y == '+':
                print(x+z)
            if y == '-':
                print(x-z)
            if y == '*':
                print(x*z)
            if y == '/':
                print(x/z)
                if ZeroDivisionError:
                    print('cannot divide by 0')
            else:
                continue
        except:
            ValueError
main()