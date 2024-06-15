#Create a program that accepts a hwy number and outputs the direction
#User Enter 95
#Output: interstate 95 runs North to South

def main():
    while True:
        try:
            hwy_number = int(input('Please enter a highway number: '))
            #Get the remainder of highway number divided by 2,

            if hwy_number <= 0:
                print('ERROR: Enter a valid number')
                continue
        except:
            print('ERROR: Enter a correct input')
        
        print(f'Highway {hwy_number} run from East to West' if hwy_number % 2 == 0 else f'Highway {hwy_number} run from North to South')
        break
        
main()