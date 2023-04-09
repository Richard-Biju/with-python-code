print ("WELCOME")

def modulo_calculator(): #definition of function modulo_calculator.
    x = int(input("Enter the dividend you want the remainder of: "))  # input function takes user's input as a string. int function convert string to an integer and sore in x.
    y = int(input("Enter the divider you want the remainder of: "))   # stores in y

    modulo = x % y #calculation is done, reminder of divesion (modulo).

    print("The remainder of", x, "divided by", y, "is", modulo) #print the result.
 

#modulo_calculator()




def integer_division():  #definition of function integer_division.
    x = input ("give me a number to divident:")  #input function takes user's input(divident) as a string and stores it in the variable x.
    y = input("what do you want it divided by?") #input function takes user's input(divided) as a string and stores it in the variable y.

    z = float(x) / int(y) #division operation.
    #it takes value of x to a floating point number using the float function.
    #then it takes value of the string y to an integer using the int function and divide and store the value in z.

    print ("the result is" + str(z)) #print the result,the value in z  using the + operator.
#integer_division()

def float_integer_calculator(): #definition of function float_integer_calculator.
    a = float(input("Enter the first float number: ")) #takes the input from user, input function reads the user input as string, float convert the string to floating point number and stored in a.
    b = float(input("Enter the second float number: ")) #takes the second input from user .
    int_a = int(a) #this converts the floating point number a to an integer using the int function and store in int_a
    int_b = int(b) #this converts the floating point number a to an integer using the int function and store in int_b
    result = int_a // int_b #integer division calculation is performed, and the answer is stored in result
    print(int_a, "//", int_b, "=", result) #prints the result. division operator ('//').

#float_integer_calculator()


def for_loop_counter(): #definition of function for loop counter.
    counter = float(input("What should be the initial value of the counter?\n")) #user input the initial value of the counter as floating point number. the input function takes the user input as string. float convert the string to a floating point number and store in counter.
    loop_count = int(input("How many times should the loop run?\n"))
    increment = float(input("How much should the counter increment by?\n"))
    is_positive = True if input("Should the counter decrement instead of incrementing? y / n\n") == 'n' else False
    #then user enter the number of times should the loop run, input reads the input as string and int convert the string to an integer, and stored in loop_count.
    #user enter the increment value as floating point number. and stored in increment.
    #then it asks the user to choose y or n. if user input n then is_positive is set to true otherwise to false.

    if not is_positive:
        increment = increment * -1

    for iterator in range(loop_count):
        counter = counter + increment

    print("The final value of the counter is " + str(counter))
    # the if statement checks if is positive is false.
    #the line inside the if  ,increment value by multiplying it by -1.
    #for loop that iterates loop count times.
    #This line inside the for loop,  counter value by adding the increment or decrement value.
    #after this it print the final value of the counter.


#for_loop_counter()


def print_ascii_values():  #definition of function for print_ascii_values.
    char = input("Please enter a character: ")  #takes input from the user and store in char.
    if len(char) == 1:  #it checks if the char is equal to 1 , if it is, the code inside the if block will be executed.
        ascii_value = ord(char) #the ord function will calculate the ascii value of the character stored in char, and store it in ascii value.
        print("The ASCII value of", char, "is:", ascii_value) #this prints the results.
    else:
        print("Please enter only one character.") #if the user enter more than one character the else function is excuted .

#print_ascii_values()


def change_machine():
    coins = [25, 10, 5]
    coin_counts = [0, 0, 0]

    amount = float(input("Enter the amount in dollars (e.g., 2.95): "))
    cents = int(amount * 100)

    for i in range(len(coins)):
        coin = coins[i]
        coin_counts[i] = cents // coin
        cents %= coin

    print("Quarters:", coin_counts[0])
    print("Dimes:", coin_counts[1])
    print("Nickels:", coin_counts[2])
   #definition of function for change machine.
   #the coin and coin counts represents the coin order, the coin has value 25, 10, 5 which means quarters, dimes, and nickels in cents. 
   # next it takes input from user and convert it into float and store the result in amount.
   # calculation is done by multiplied by 100 to convert it into cents.
   # in the for loop in each step the coin value is stored. The calculation is done by integer division of cents by coin and the remainder is stored back in cents using the modulo operator %.
   # next line prints the results. 
#change_machine()


import random

def rock_paper_scissors_choices(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"

def rock_paper_scissors():
    number_choice = 0

    while number_choice < 1 or number_choice > 3:
        number_choice = int(input("Make a choice:\n 1.Rock\n 2.Paper\n 3.Scissors\n"))

    ai_number_choice = random.randint(1, 3)

    ai_choice = rock_paper_scissors_choices(ai_number_choice)
    choice = rock_paper_scissors_choices(number_choice)

    if choice == ai_choice:
        print("Draw. You both played " + choice + "!")
        return choice

    won = False
    if choice == "rock":
        if ai_choice == "scissors":
            won = True
    elif choice == "paper":
        if ai_choice == "rock":
            won = True
    elif choice == "scissors":
        if ai_choice == "paper":
            won = True

    if won:
        print("You won. You chose " + choice + ", and the AI chose " + ai_choice)
    else:
        print("You lost. You chose " + choice + ", and the AI chose " + ai_choice)

    return choice
#this code is a game of rock, paper and scissor.
#the import random function pick random integer.
#in if else, code takes user input to a string of this game choice. if choice is 1 rock it returns rock.
#if the choice is 2 it returns paper, if the choice is 3 it returns scissor.
#next it initializes a variable number_choice to 0.
#after that in while loop the user can choose rock paper and scissor. The user choice is stored as an integer in the variable number_choice. The while loop continues until number_choice is between 1 and 3.
#ai number choice function will choose a number between 1 and 3.
#next the user choise and ai choice is convert to string using rock_paper_scissors_choices function.
#in the if choice compares both user and ai choice. 
#if they are same the game print draw.
# the if else statement is to check the winner of the game . if user win the won is set to true.
#in the next line it prints the result.
#rock_paper_scissors()


def mario_wins_a_level():
    stairs = 0
    while not (1 <= stairs <= 20):
        stairs = int(input("Please enter the stairs Mario climbs to finish the level?\n"))
        if not (1 <= stairs <= 20):
            print("Please enter the stairs between 1 and 20.")

    for i in range(stairs):
        print(" " * (stairs - i), end="")
        print("#" * (i + 2), end="   ")

        if i == 0:
            print("|>")
        elif i == stairs - 1:
            print("#")
        else:
            print("|")
        
#definition of function for mario wins a level.
#the stair = 0.
#in the while loop , it asks the user to enter the number of stairs(#).
# the number is stored as an integer in the variable stairs.
#the while loop checks the number of stairs is between 1 and 20. if it is not in between in  this number it prints "Please enter the stairs between 1 and 20."
# next in the for loop iterates the stair value.
# next line print the stairs. stairs -1 for spaces. and i+2 for '#'. 
# next in the if else statement the flag is printed. If i is 0, the code outputs "|>". If i is stairs - 1, the code outputs "#". If i is neither 0 nor stairs - 1, the code outputs "|". and thats how the flag is printed.
#mario_wins_a_level()

def main():
    functions = {
        '0': modulo_calculator,
        '1': integer_division,
        '2': float_integer_calculator,
        '3': for_loop_counter,
        '4': print_ascii_values,
        '5': change_machine,
        '6': rock_paper_scissors,
        '7': mario_wins_a_level,
    }

    print("0: modulo_calculator")
    print("1: integer_division")
    print("2: float_integer_calculator")
    print("3: for_loop_counter")
    print("4: print_ascii_values")
    print("5: change_machine")
    print("6: rock_paper_scissors")
    print("7: mario_wins_a_level")

    user_input = input("please select a function? ")

    if user_input in functions:
        functions[user_input]()
    else:
        print("Invalid input. Please enter a valid option.")

main()
#this is the starting step  of the code.
#the dictionary function allows the user to choose from a set of functions. if the user enter 0 the modulo calculator code runs.
# the user input function allows the user to choce the function.
#the if else statement checks user's input is in the dictionary functions. if the user enter 8 the else statement will print invalid input.
#THE main() function starts the program.













