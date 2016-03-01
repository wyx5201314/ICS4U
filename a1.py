#1
def helloWorld ():
    print("Hello World!")
helloWorld()
#2
def greet(a):
    print("Hello",a)
greet("Max!")

#3
def greet2():
    z=input("Please unter your name.")
    print("Hello",z,"!")

#4
def plus1(num):
    return num+1
#5
def max3(a,b,c):
    return max3(a,b,c)

#6
def printN(n):
   while n>x:
       x=x+1
       print(x)

#7
def sumN(n):
    return sum(range(1,n))
#8
def strFirst(str):
    return str[0]
#9
def strHalf(str):
    return str[:len(str)//2]
#10
import random
def guessingGame():
    guesses=0
    number = random.randint(1, 7)
    a=input("pls guess a number between 1 to 7. ")
    while True:
        guesses=guesses+1