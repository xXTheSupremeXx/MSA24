def main():
    
    a = 7
    b = 7
    
    if a > b:
        print(f'{a} is greater than {b}')
    elif b > a:
        print(f'{b} is greater than {a}')
    elif a == b:
        print(f'{a} is equal to {b}')
    
    #print the appropriate letter grade based on the test score
    #A: 100-90, B: 89-80, C: 79-70, D:69-60, F:59-0
    print('\nGrade Decision: 1')
    test_score = 88.6657858457437

    if test_score <=100 and test_score >= 90:
        print(f'{test_score}-----> A')

    elif test_score <=90 and test_score >= 80:
        print(f'{test_score}-----> B')

    elif test_score <=80 and test_score >= 70:
        print(f'{test_score}-----> C')

    elif test_score <=70 and test_score >= 60:
        print(f'{test_score}-----> D')

    else:
        print(f'{test_score}-----> F')

    #Grade decision restructured
    print('\nGrade Decision: 2')
    if test_score <=100 and test_score >= 90:
        print(f'{test_score}-----> A')

    elif test_score >= 80:
        print(f'{test_score}-----> B')

    elif test_score >= 70:
        print(f'{test_score}-----> C')

    elif test_score >= 60:
        print(f'{test_score}-----> D')

    else:
        print(f'{test_score}-----> F')

    #Create a descision structure to determine the season winter, spring, summer and fall based on the month
    #winter:12, 1, 2 (Dec, Jan. Feb) spring: 3, 4, 5 (March, April and May) Summer: 6, 7, 8 (June, July and August) Fall: 9, 10, 11 (September, October, and November)
    #ask the user to input the number of the month
    #Output the season based on the month

    c = 4
    d = 10
    if a == 4 or b== 5 or c == 5 or d== 10:
        print('The or condition is true')

while True:
        
    months_number = int(input('Enter a number corresponding to a month of the year:'))

    if months_number == 12 or months_number == 1 or months_number == 2:
        print('Your month corresponds to the season of Winter\n')
        
    elif months_number == 3 or months_number == 4 or months_number == 5:
        print('Your month corresponds to the season of Spring\n')
        
    elif months_number == 6 or months_number == 7 or months_number == 8:
        print('Your month corresponds to the season of Summer\n')
        
    elif months_number == 9 or months_number == 10 or months_number == 11:
        print('Your month corresponds to the season of Fall\n')
    
    else:
        print('Please input a correct number\n')
        continue
main()