import random

def difficult_option():
    while True:
        difficulty_level_input = int(input('Enter a difficulty level of 1, 2, or 3:'))
        if difficulty_level_input in [1, 2, 3]:
            return difficulty_level_input
        else:
            print('INVALID')
            continue
    
def questions():
    while True:
        questions_input = int(input('Enter number of questions from 3-10:'))
        if questions_input in [3, 4, 5, 6, 7, 8, 9, 10]:
            return questions_input
        else:
            print('INVALID')
            continue

def generate_question(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def main():
    level = difficult_option()
    number_of_questions = questions()
    correct_answers_gotten = 0

    for i in range(number_of_questions):
        x, y = generate_question(level)
        correction_answer = x + y
  
        for attempt in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correction_answer:
                    print("CORRECT!!!")
                    correct_answers_gotten += 1
                    break
                else:
                    print("WRONG!!!")
            except:
                print('"WRONG!!!"')
main()
