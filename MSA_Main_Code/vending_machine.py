def coin():
    starting_amount = 50
    valid_coins = [1, 5, 10, 25]
    print(f'Amount Due: {starting_amount}')
    while starting_amount > 0:
        try:
            insert_coin = int(input())
            if insert_coin in valid_coins:
                starting_amount -= insert_coin
                print(f'Amount: {starting_amount}')
            if starting_amount <= 0:
                starting_amount *= -1
                break
            else:
                continue
        except:
            break
coin()
