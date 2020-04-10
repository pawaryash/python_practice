#This program will take a number as an input & will tell if the input is odd or even
unknownNumber = int(input("Enter a number : "))

resultNumber = unknownNumber % 2

if resultNumber == 0:
    print("Even")
else:
    print("Odd")