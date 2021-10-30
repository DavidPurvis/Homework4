import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try: 
    	infile = open(filename, "r")

    	print("File opened.")
    except TypeError:
    	print("Input must be a string.")
    except IOError:
    	print("File does not exist.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
    	return num1 / num2
    except ZeroDivisionError:
    	print("Cannot divide by 0.")
    except TypeError:
    	print("Input must be integers.")

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = None
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
    except:
        print("Error: Parameters passed were not valid data types")

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    if isinstance(temp, list):
        temp2 = ""
        for i in temp:
            temp2+=str(i)
        temp = temp2
    try:
        temp = str(temp)
    except:
        print("Error: Unable to convert object to string")
    else:
        test = temp[::-1]
        if(test == temp):
            return True
        else:
            return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    try:
    	div = num1 / num2
    	print("Your numbers divided is:", div)
    except:
        print("Please try again")


## returns the squareroot of a particular number
def sq(num):
	try:
		return math.sqrt(num)
	except ValueError:
		print("Input must be positive numbers.")
	except TypeError:
		print("input must be integers.")

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
	try:
		if(first.isalpha() and middle.isalpha() and last.isalpha()):
    			print("Hello!")
    			print("Welcome to the program", first, middle, last)
    			print("Glad to have you!")
		else:
    			print("Input must be string values.")
	except:
		print("Input must be string values.")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])
