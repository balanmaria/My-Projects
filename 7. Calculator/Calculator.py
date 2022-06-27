#Calculator
import Beginner.Day10.art

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def substract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1,n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(Beginner.Day10.art.logo)
    num1 = float(input("What's the first number?: "))
    #afisam toti operatorii posibili
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2= float(input("What's the next number?: "))
        #cautat in dictionar, cheia care se potriveste cu operatia dorita de user
        function=operations[operation_symbol]
        #apelat functia reprezentativa dorintei user-ului
        result=function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1=result
        else:
            should_continue = False
            calculator()

calculator()