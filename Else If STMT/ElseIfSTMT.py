"""
Write A Progam to Print a String message  if Number is divisable by 3 and 5 print  FizzBuzz if number only divisable by 3 print Fizz
if number only divisable by 5 print Buzz
"""

def checkNumDiv():
    n=int(input("Enter the Number : "))
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")

checkNumDiv()

"""
O/P:
Enter the Number : 5
Buzz
"""