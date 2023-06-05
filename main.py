python_quiz_dictionary = {'Lives': 3, 'Hints': 3, 'Last Section Completed': 0}

python_quiz_answers_list = ['A', 'B', 'C', 'D']


def python_quiz_rules():

    print()

    print('Welcome to the Python Quiz!')

    print()

    print('The quiz is broken up into three different sections, each with five questions each. There is an easy, medium and hard section each with questions with their respective difficulty.')

    print('Within the quiz you only have three lives, if a question is missed you lose a life. Once you\'re all out of lives, the quiz is over!!')

    print('You are also given three hints, however once you use all of them you can\'t use them again!')

    print('After each section there will be a bonus question, if you answer it correctly you will be given an extra life!')

    print()

    print('Good Luck!')

    print()


def python_quiz_easy_sec():

    print()

    print('Section 1 - Difficulty Easy:')

    print()
    print()

    print('1. What is not true of a variable in Python?')
    print('A) It stores a value that you assign to it.')
    print('B) It\'s name can start with a number.')
    print('C) It\'s value can be overwritten/updated by reassigning it later on in a program.')
    print('D) You can add variables together.')

    while True:

        python_quiz_question_1 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_1.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Try to remember the rules for naming variables.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_1.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_1.upper() != 'B':

            print('That\'s incorrect! The correct answer is "B"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('2. What is the symbol that goes after calling a function?')
    print('A) "_"')
    print('B) "#"')
    print('C) "()"')
    print('D) "*"')

    while True:

        python_quiz_question_2 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_2.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Look at python\'s many functions such as "print" and "input". What do they have in common?')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_2.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_2.upper() != 'C':

            print('That\'s incorrect! The correct answer is "C"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('3. What is the output of this code?')
    print()
    print('a = 5')
    print('b = 10')
    print('print(a + b)')
    print()
    print('A) "5"')
    print('B) "10"')
    print('C) "ab"')
    print('D) "15"')

    while True:

        python_quiz_question_3 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_3.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Remember that variables store the values that they are assigned.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_3.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_3.upper() != 'D':

            print('That\'s incorrect! The correct answer is "D"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('4. Which of the following creates an empty list?')
    print('A) "list = {}"')
    print('B) "list = []"')
    print('C) "list = ()"')
    print('D) "list = | |"')

    while True:

        python_quiz_question_4 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_4.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Within the answers "A", "B" and "C", there is a tuple, list and dictionary being made.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_4.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_4.upper() != 'B':

            print('That\'s incorrect! The correct answer is "B"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('5. True or False, you can change the data type of a variable?')
    print('A) True')
    print('B) False')

    while True:

        python_quiz_question_5 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_5.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Try to remember python\'s functions for the specific data types.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_5.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_5.upper() != 'A':

            print('That\'s incorrect! The correct answer is "A"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()

    print('Here\'s what you ended the first section with:')

    python_quiz_dictionary['Last Section Completed'] += 1

    print(python_quiz_dictionary)

    print()

    print('I\'ll also give you an extra hint for later!')

    python_quiz_dictionary['Hints'] += 1


def python_quiz_medium_sec():

    print()
    print()

    print('Section 2 - Difficulty Medium:')

    print()
    print()

    print('6. What is the index of "b" in this list?')
    print('list = [a, b, c, d]')
    print('A) 0')
    print('B) 1')
    print('C) 2')
    print('D) 3')

    while True:

        python_quiz_question_6 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_6.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Remember that when counting indexes you start at 0.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_6.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_6.upper() != 'B':

            print('That\'s incorrect! The correct answer is "B"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('7. What is the statement used to end a loop?')
    print('A) "continue"')
    print('B) "pass"')
    print('C) "break"')
    print('D) "exit"')

    while True:

        python_quiz_question_7 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_7.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('The term "exit" applies to a function used to exit the program so that\'s probably not it.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_7.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_7.upper() != 'C':

            print('That\'s incorrect! The correct answer is "C"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('8. What is the main purpose of a for loop?')
    print('A) To loop through a program until a specific condition is met.')
    print('B) To iterate through something such as a string or list.')
    print('C) To loop through a program infinitely.')
    print('D) To serve as a place to store values for variables.')

    while True:

        python_quiz_question_8 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_8.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Think of how a for loop works, try to read a program that uses one and see how it does so.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_8.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_8.upper() != 'B':

            print('That\'s incorrect! The correct answer is "B"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('9. What does the following code output?')
    print()
    print('a = 5')
    print('b = 5')
    print('while True:')
    print('print(a + b)')
    print()
    print('A) "10"')
    print('B) "5"')
    print('C) "ab"')
    print('D) "10" an infinite number of times.')

    while True:

        python_quiz_question_9 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_9.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Notice if the loop has any way of exiting.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_9.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_9.upper() != 'D':

            print('That\'s incorrect! The correct answer is "D"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('10. Is there a difference between "round(var, 2)" and ":.2f" when used in a program?')
    print('A) Yes, "round(var, 2)" rounds the variable to two decimals while the other does not.')
    print('B) No, they both do the same thing in terms of rounding the variable to two decimals.')
    print('C) Yes, ":.2f" rounds to two decimals while the other does not.')
    print('D) No, they both add two zeros at the end of the variable value.')

    while True:

        python_quiz_question_10 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_10.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('The "f" in ":.2f" is for "float", meaning a decimal number.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_10.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_10.upper() != 'B':

            print('That\'s incorrect! The correct answer is "B"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()

    print('Here\'s what you ended the second section with:')

    python_quiz_dictionary['Last Section Completed'] += 1

    print(python_quiz_dictionary)

    print()

    print('I\'ll also give you an extra hint for later!')

    python_quiz_dictionary['Hints'] += 1


def python_quiz_hard_sec():

    print('Section 3 - Difficulty Hard:')

    print()
    print()

    print('11. True or False, the replace function only replaces characters of a string.')
    print('A) True')
    print('B) False')

    while True:

        python_quiz_question_11 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_11.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('It is typically used to replace a specified phrase.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_11.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_11.upper() != 'A':

            print('That\'s incorrect! The correct answer is "A"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('12. How would you access a value of a variable that you return from a function with it being the second returned value of the function?')
    print()
    print('Assume it was returned like this: return var1, var2, var3. And that it was stored in a variable called "var".')
    print()
    print('A) You would type the variable name "var".')
    print('B) You would type "var2"')
    print('C) You would type "var[var2]"')
    print('D) You would type "var[1]"')

    while True:

        python_quiz_question_12 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_12.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Think about how indexing works when trying to access a specific value of an index.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_12.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_12.upper() != 'D':

            print('That\'s incorrect! The correct answer is "D"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('13. How is it possible to have a loop in a program without using any loop statements?')
    print('A) By using recursive functions to keep calling the same function until a condition is met.')
    print('B) It isn\'t possible to do loops without any loop statements.')
    print('C) You can by using only if statements to keep checking for a condition.')
    print('D) In order to do this you would have to import a specific library.')

    while True:

        python_quiz_question_13 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_13.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('Think of how a loop works in terms of doing the same thing over and over.')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_13.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_13.upper() != 'A':

            print('That\'s incorrect! The correct answer is "A"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('14. What is the difference between a tuple and a list?')
    print('A) You can modify a list, since it is mutable, while you cannot modify a tuple, since it is immutable.')
    print('B) You can modify a tuple, which is mutable, while you cannot modify a list, since it is immutable.')
    print('C) You can only use indexing with a list.')
    print('D) You can only use indexing with a tuple.')

    while True:

        python_quiz_question_14 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_14.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('What happens when you try to add something to a tuple compared to a list?')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_14.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_14.upper() != 'A':

            print('That\'s incorrect! The correct answer is "A"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()
    print()

    print('15. When importing a library such as random, what syntax needs to be used when attempting to use the specific function "randint" from the library?')
    print('A) No special syntax is needed since the library is already imported.')
    print('B) You would type the name of the library with the variable inside parenthesis. random(var)')
    print('C) You type it with the library name followed by a period then the function with the variable in parenthesis. (random.randint(var))')
    print('D) You would type it with the library name followed by a period then the function being used while storing the value in a variable. (var = random.randint(x, y))')

    while True:

        python_quiz_question_15 = input('Enter "A", "B", "C", "D" or "Hint": ')

        if python_quiz_question_15.upper() == 'HINT':

            if python_quiz_dictionary['Hints'] > 0:

                print('If you are generating a random number for a dice game for instance, where would you store it and how would you type it out?')

                python_quiz_dictionary['Hints'] -= 1

            else:

                print('You are out of hints!')

        elif python_quiz_question_15.upper() not in python_quiz_answers_list:

            print('Please input a valid answer!')

        elif python_quiz_question_15.upper() != 'D':

            print('That\'s incorrect! The correct answer is "D"!')

            python_quiz_dictionary['Lives'] -= 1

            break

        else:

            print('That\'s right!')

            break

    if python_quiz_dictionary['Lives'] == 0:

        print('You ran out of lives!')

        print()

        python_quiz_replay()

    print()

    print('Here\'s what you ended the third section with:')

    python_quiz_dictionary['Last Section Completed'] += 1

    print(python_quiz_dictionary)

    print()


def python_quiz_bonus_questions():

    print()

    if python_quiz_dictionary['Last Section Completed'] == 1:

        print('Welcome to the first bonus question!')

        print()

        print('What year was the Python language born in?')

        while True:

            python_bonus_1_answer = input('Enter the year: ')

            if (python_bonus_1_answer.isnumeric()) and (python_bonus_1_answer != '1991') and (len(python_bonus_1_answer) == 4):

                print('That\'s incorrect! Good try though!')

                break

            elif python_bonus_1_answer == '1991':

                print('Great Job! You earned an extra life!')

                python_quiz_dictionary['Lives'] += 1

                break

            else:

                print('Type a valid year!')

    elif python_quiz_dictionary['Last Section Completed'] == 2:

        print('Here is the second bonus question!')

        print()

        print('What type of language is python?')

        print('A) Object-Oriented')
        print('B) Logic')
        print('C) Procedural')
        print('D) Scripting')

        while True:

            python_bonus_2_answer = input('Enter either "A", "B", "C" or "D": ')

            if python_bonus_2_answer.upper() not in python_quiz_answers_list:

                print('Enter a valid answer please!')

            elif python_bonus_2_answer.upper() == 'A':

                print('Great job! Here\'s an extra life!')

                python_quiz_dictionary['Lives'] += 1

                break

            else:

                print('That\'s incorrect!')

                break


def python_quiz_replay():

    print()

    if python_quiz_dictionary['Lives'] == 5:

        print('Great Job! You didn\'t lose any lives as well as got both bonuses right!')

    elif python_quiz_dictionary['Lives'] == 4:

        print('You finished with an extra life! Awesome!')

    elif python_quiz_dictionary['Lives'] == 3:

        print('You started with three lives and ended with three lives, great work!')

    elif python_quiz_dictionary['Lives'] == 2:

        print('You ended with two lives left! I would go and review a little bit.')

    elif python_quiz_dictionary['Lives'] == 1:

        print('You barely made it through the quiz! I would go and study if I were you!')

    elif python_quiz_dictionary['Lives'] == 0:

        print('You lost all of your lives! You need to go do some studying!')

    print()

    while True:

        python_quiz_play_again = input('Would like to try the quiz again? ("Yes/"No") ')

        if python_quiz_play_again.upper() == 'YES':

            print('Cool, let\'s go again!')

            python_quiz_dictionary['Lives'] = 3

            python_quiz_dictionary['Hints'] = 3

            python_quiz_dictionary['Last Section Completed'] = 0

            python_quiz_gameplay_loop()

        elif python_quiz_play_again.upper() == 'NO':

            print('Okay, see you later!')

            exit()

        else:

            print('Please input either a "Yes" or a "No"!')


def python_quiz_gameplay_loop():

    while True:

        python_quiz_easy_sec()
        python_quiz_bonus_questions()
        python_quiz_medium_sec()
        python_quiz_bonus_questions()
        python_quiz_hard_sec()
        python_quiz_replay()


python_quiz_rules()

python_quiz_gameplay_loop()
