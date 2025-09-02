# Make sure you are not modifying the method signatures
# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    # TODO: Implement this function
    
    print("Hello world!")

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function

    name= input("Enter your name:")
    print(f"Hello, {name}")

    age= int(input("Enter your age:"))
    print(f"You are {age} years old")

    height= float(input("Enter your height:"))
    print(f"You are {height} meters long")

hello_world()
input_output()