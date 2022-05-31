'''

1) Python 2 considers print to be a statement, not a function, and strings are stored as ASCII by default. Python 2 also
provides an integral value when dividing two values, exceptions are enclosed in notations, and global variable values
do change if used in a for-loop. Python 2 has the xrange() function defined for iterations, has a more complicated
syntax, has lots of libraries that are not forward compatible, and can port codes to Python 3 with a lot of effort.

Python 3 considers print to be a function, not a statement, and strings are stored as UNICODE by default. Python 3 also
provides a floating point value when dividing two integer values, exceptions are enclosed in parentheses, and value of
global variables never change. Python 3 uses a new range function to perform iterations, has an easier syntax than
Python 2, has lots of libraries that can only be used in Python 3, and is not backward compatible with Python 2.
'''

def problem_2():
    word = input("Enter word: ")
    new = ""

    # Add all elements except the last 2 characters.
    for i in range(len(word) - 2):
        new += word[i]
    
    # Reverse the result word
    reverse = new[::-1]
    print(reverse)

    num1 = int(input("Enter first integer number: "))
    num2 = int(input("Enter second integer number: "))
    # Perform and display addition, subtarction, and division on num1 and num2
    print("Add: ", num1 + num2)
    print("Subtract num 2 from num 1: ", num1 - num2)
    print("Subtract num 1 from num 2: ", num2 - num1)
    print("num1 / num2: ", num1 / num2)
    print("num2 / num1: ", num2 / num1)

    names = input("Enter a list of names (add a space after the last name): ")
    name = ""
    list1 = names.split()
    print("Length of list: ", len(list1))
   
    # Add a new name to list
    list1.append("Ash")

    # print all elements in the list
    for i in list1:
        print(i)


def problem_3():
    sent = input("Enter a sentence: ")

    # Split the sentence into a word list
    list2 = sent.split()
    new_sent = ""

    # change all python to pythons in the list
    for i in range(len(list2)):
        if list2[i].lower() == "python":
            list2[i] = "pythons"

    # form the new sentence from the list
    for i in list2:
        new_sent += i + " "

    print(new_sent)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_2()
    problem_3()