print ("WELCOME")

def modulo_calculator():
    x = int(input("Enter the dividend you want the remainder of: "))  
    y = int(input("Enter the divider you want the remainder of: "))  

    modulo = x % y

    print("The remainder of", x, "divided by", y, "is", modulo)

    

#modulo_calculator()



def integer_division():
    x = input ("give me a number to divident:")
    y = input("what do you want it divided by?")

    z = float(x) / int(y)

    print ("the result is" + str(z)) 
#integer_division()

def float_integer_calculator():
    a = float(input("Enter the first float number: "))
    b = float(input("Enter the second float number: "))
    int_a = int(a)
    int_b = int(b)
    result = int_a // int_b
    print(int_a, "//", int_b, "=", result)

#float_integer_calculator()


def for_loop_counter():
    counter = float(input("What should be the initial value of the counter?\n"))
    loop_count = int(input("How many times should the loop run?\n"))
    increment = float(input("How much should the counter increment by?\n"))
    is_positive = True if input("Should the counter decrement instead of incrementing? y / n\n") == 'n' else False

    if not is_positive:
        increment = increment * -1

    for iterator in range(loop_count):
        counter = counter + increment

    print("The final value of the counter is " + str(counter))

#for_loop_counter()


def print_ascii_values():
    char = input("Please enter a character: ")
    if len(char) == 1:
        ascii_value = ord(char)
        print("The ASCII value of", char, "is:", ascii_value)
    else:
        print("Please enter only one character.")

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











