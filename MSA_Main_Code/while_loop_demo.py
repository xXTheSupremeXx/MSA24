def main():

    #create a while loop that prints integers between 0 and 10
    output_value = 0
    stop_value = 10

    #run the loop when the output while ouput_value is less than or equal to stop value
    while output_value <= stop_value:
        print(output_value)
        #increment output value
        output_value += 1
    print('\n\n')
    output_value = 0
    while True:
        print(output_value)
        output_value += 1

        #If output  value is greater than stop value. Break the loop
        if output_value > stop_value:
            break

main()