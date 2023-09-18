# Written:  9/18/23
# Author: Jackson Young
# Class: CSC-1200

# Functions
squareSpaceString = "       " # Correct spacing between "|" in a line

def createTopLine(length):
    for v in range(length): # Per range of the length..
        if v == 0:
            print("+", end= " "); # Creates first plus
        for i in range(4):
            print("-", end= " ") # Create the dash fill line
            if i == 3 and (v != length - 1):
                print("+", end= " ")
            elif i == 3 and (v == length - 1):
                print("+")

def createFill(Length):
    Length = Length - 1 # Fix start point to 1 instead of 0
    
    def createFillLine():
        for sLength in range(Length):
            if sLength < (Length - 1): # I don't know why this determines if it works or not tbh
                print("|", squareSpaceString, end= " ") # Create the length - 1 of "|"'s 
            else:
                print("|", squareSpaceString, "|") # Final length, remove end=
    
    for _ in range(4): # Looping through AMOUNT of lines
        createFillLine()
        
def print_TwoByNumber(Number): # Draw the main grid with the amount of squares given
    for i in range(Number): # Loop provided amount to create a square. Repeats for function below as well
        createTopLine(2)
        createFill(2 + 1)
        if i == (Number - 1):
            createTopLine(2)
        
def print_FourByNumber(Number):
    for i in range(Number):
        createTopLine(4)
        createFill(4 + 1)
        if i == (Number - 1):
            createTopLine(4)
        
def print_LengthByWidth(X, Y): # Use Length and Width instead of a singular number
    for i in range(X):
        createTopLine(Y)
        createFill(Y + 1)
        if i == (X - 1):
            createTopLine(Y)
        
# Gather Inputs
NumberInput = ""
NumberInput = input("What is 'number' value for 2byNumber?: ") # get input for 2bN
print_TwoByNumber(int(NumberInput))
print("\n")
NumberInput = input("What is 'number' value for 4byNumber?: ") # get input for 4bN
print_FourByNumber(int(NumberInput))
print("\n")
Length, Width = "", ""
Length = input("What is 'Length' value for LengthByWidth?: ") # get length input for LbW
Width = input("What is 'Width' value for LengthByWidth?: ") # get width input for LbW
print_LengthByWidth(int(Length), int(Width))