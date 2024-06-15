def coin():
    while True:
        starting_amount = 50
        try:
            insert_coin = int(input(f'Amount Due:'))
            if (insert_coin < 0):
                continue
            elif insert_coin not in [1, 5, 10, 25]:
                continue
            else:
                return insert_coin
        except:
            break
    



