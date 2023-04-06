print ("Hello world")




def multiplication():

    x= input ("give me a number to multiply:")
    y= input("what do you want it multiplied by?")

    z= int(x) * int(y)

    print("the result is" + str(z))    

multiplication()

def division():
    x = input ("give me a number to divident:")
    y = input("what do you want it divided by?")

    z = float(x) / int(y)

    print ("the result is" + str(z)) 
division()

def wide_boy_strings():
    user_str = input("give me a string to W I D E N\n")

    for char in user_str:
        print(char, end= " ")

wide_boy_strings()
def wide_boy_strings2():
    user_str = input("give me a string to W I D E N\n")

    i = 0

    wide_str = ""

    for char in user_str:

        

        if i < len(user_str) - 1:
           wide_str = wide_str + char + " "
        else:
            wide_str = wide_str + char 
        i += 1
    print(wide_str)

        

wide_boy_strings2()

def for_loop_example():
    x = int(input("HOW MANY TIME SHOULD I RUN?"))

    for i in range(x):
        print("this loop is running for the "+ str(i+1) +" time.")

for_loop_example()

def odd_or_even():
    x = int(input("which number do you want to check?"))

    if x % 2 == 0:
        print("the number  " + str(x)+ " is even.")
    else:
        print("the number " + str(x)+" is an odd.")

odd_or_even()

def ascii_sum():
    user_str = input("give me a string for which you want the sum of the ASCII value of its char:\n")

    str_size = len(user_str)

    i=0

    sum = 0

    while(i < str_size):
        
        sum = sum + ord(user_str[i])
        i = i + 1

    print("the sum of all this ASCII value is ", sum)

ascii_sum()

def string_flipper():
    user_str = input(" give me a string you want flipped or reversed \n")

    for char in reversed(user_str):
        print(char, end="")

string_flipper()

user_input = input("which function would you like to run?")

if user_input == 0:
   multiplication()
elif user_input == 1:
    division()
elif user_input == 2:
    wide_boy_strings()
elif user_input == 3:
    wide_boy_strings2()
elif user_input == 4:
    for_loop_example()
elif user_input == 5:
    odd_or_even()
elif user_input == 6:
    ascii_sum()












