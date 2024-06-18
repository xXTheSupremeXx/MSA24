menu = {

    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    amount = 0
    while True:
        print('\nItem:')
        user_input = input().title()
        if user_input.lower() == 'end':
            break
        elif user_input in menu.keys():
                amount += menu[user_input]
                print(f"Total: ${amount:.2f}")
        else:
            continue
main()
