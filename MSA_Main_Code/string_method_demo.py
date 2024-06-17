def main():
    #CapitaLize a string
    my_name = 'Abhinav'
    print(my_name.capitalize())

    #Make a string uppercase
    print(my_name.upper())

    #Make a string lowercase
    last_name = "PULA"
    print(f'{my_name.capitalize()} {last_name.lower()}')

    #Determine if a string starts with a set of characters
    print(my_name.startswith('a'))

    if(not my_name.startswith('a')) and not my_name.startswith('A'):
        print(f'You spelled {my_name} incorrectly')
    else:
        print(f'You spelled {my_name} incorrectly')

    #Determine if a string ends with a specified set of characters
    print(my_name.endswith('av'))

    #find a set of characters in a string
    print(my_name.find('a', 7))

    #loop through a string
    print('\n\n')
    for letter in my_name:
        print(letter)
    
    print(f'{my_name} has {len(my_name)} letters')

    for letter_index in range(len(my_name)):
        print(f'letter {letter_index}:{my_name [letter_index]}')
    
    print('\n\n')
    sentence = 'I have a dog. My dog is cute. Do you want a dog?'
    #Write code that counts the numebr of occurences of the word dog in sentence
    #expected output: 3
    #use a while loop to read the string
    #read the string until you find the first occurence of dog
    #Add 1 to the number of found dogs
    #continue reading from the next index: update the start index in the first method()

    start_index = 0
    number_of_dogs = 0
    while True:
        dog_index = sentence.find('dog', start_index)

        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
            start_index = dog_index + 1
            continue
    print(f'Number Of Dogs: {number_of_dogs}')

main()