def main():

    #list demo
    #create a list of string names
    names = ['John', 'Alice', 'Mary', 'Bob']
    list_of_integers = [10,16, 24, 42, 14, 9]
    random_type_list = ['Cyd,', 15, 22.3, "Frank"]

    print(names)
    print(list_of_integers)

    #add values to a list
    names.append('jonny')
    list_of_integers.append(5)
    list_of_integers.append(63)

    print(type(names))
    print(type(list_of_integers))

    print(names)
    print(list_of_integers)
    
    #get the number of items in a list
    number_of_items = len(list_of_integers)
    print('\n\n')
    print(f'number of items in integer list: {number_of_items}')

    #Get values from our list
    #get the first value from the list of integers
    print(f'\nFirst item in iteger list: {list_of_integers[0]}')

     #Get values from our list
    #get the fourth value from the list of integers
    print(f'\nfourth item in iteger list: {list_of_integers[3]}')

    #print all items in the list of integers
    print('\nInteger list items')
    for item in list_of_integers:
        print(item)
    
    print('\n')
    #get the number of items in the integer list
    number_of_items = len(list_of_integers)
    for index in range(number_of_items):
        print(f'Index {index+1}: {list_of_integers[index]}')

main()