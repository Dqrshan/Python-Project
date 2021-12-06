from prettytable import PrettyTable
head = PrettyTable(["Computer Project : Class 11 Science-I"])
head.add_row(["         - by Devasurya & Darshan"])

content = PrettyTable(["Table of contents"])  # main table of contents

table = PrettyTable(["S. No.", "Chapter Name"])
table.add_row(["1", "Getting Started With Python"])
table.add_row([" ", " "])
table.add_row(["2", "Python Fundamentals"])
table.add_row([" ", " "])
table.add_row(["3", "Data Handling"])
table.add_row([" ", " "])
table.add_row(["4", "Flow Of Control"])
table.add_row([" ", " "])
table.add_row(["5", "String Manipulation"])
table.add_row([" ", " "])
# we could have done `.add_rows([])` xD
table.add_row(["6", "List Manipulation"])
table.add_row([" ", " "])
table.add_row(["7", "Exit the program"])
x = 0
while True:
    if x >= 1:
        contin = input("Continue? (Yes/No): ")
        print()
        if contin.lower() == "yes":
            x = 0
            continue
        elif contin.lower() != "yes":
            break
    print(head)
    print()
    print("          Table Of Contents")
    print(table)
    print()
    print()

    choice = int(input("Enter Your Choice:- "))
    print()

    # chapter 1
    if choice == 1:
        chap1 = PrettyTable(["S. No.", "Getting Started With Python"])
        chap1.add_rows(
            [
                ["1", "Pros and Cons Of Python"],
                ["", ""],
                ["2", "Print() Function"]
            ]
        )
        print(chap1)
        print()
        print()
        ch1 = int(input("Enter Your Choice:- "))
        print()
        # subtopic 1
        if ch1 == 1:
            print("""Advantages (Pros):-
        1. Easy-To-Use: It is an easy to use object oriented language with very simple syntaxes.
        2. Expressive Language: It uses fewer line of code and simpler syntax.
        3. Interpreted Language: It's easy to debug and suitable for beginners.
        4. Cross Platform.
        5. Free and Open Source.\n""")
            print("""Disadvantages (Cons):-
        1. Not the fastest language: Execution times are not that fast compared to compiled languages.
        2. Lesser libraries than other C++, Java, Perl.
        3. Not strong type binding.
        4. Not easily convertible.\n""")
            print()
            x += 1
        # subtopic 2
        elif ch1 == 2:
            print(">>> Print() - It is a function used to display the desired data type given by the user.\nFor example;\n \n")
            strToPrint = str(input("Enter the string you want to print: "))
            print(f"Printed Text: \"{strToPrint}\"")
            print()
            x += 1

    # chapter 2
    elif choice == 2:
        chap2 = PrettyTable(["S. No.", "Python Fundamentals"])
        chap2.add_rows([
            ["1", "Tokens"],
            ["", ""],
            ["2", "Barebones Of A Python Program"],
            ["", ""],
            ["3", "Variables And Assignments"],
            ["", ""],
            ["4", "Input And Output"]
        ])
        print(chap2)
        print()
        ch2 = int(input("Enter Your Choice:- "))
        print()
        if ch2 == 1:
            x += 1
            print("""Tokens are the smallest individual unit in a program and are also called "Lexical Units".
Python has the following tokens:
1. Keywords    - They are words that convey a special meaning to the language compiler/interpreter.
2. Identifier  - They are used as general terminology for the names given to different parts of the program.
3. Literals    - They are data items that have a fixed value. Python allows several kind of literals:-
    i. String Literal
    ii. Numeric Literal
    iii. Boolean Literal
    iv. Special Literal: None
    v. Literal Collections
4. Operators   - They are tokens that trigger some computation when applied to variables and other objects. Eg: +, -, *, etc.
5. Punctuators - They are symbols that are used in programming languages to organise sentence structures. 
            """)

        elif ch2 == 2:
            x += 1
            print("""The basic structure of python program contains:-
1. Expressions - Any legal combination of symbols that represent a value. Eg: a = 1 + 2, 3 + 5 / 4
2. Statements  - A statement is a programming instruction due to which some action takes place. Eg: print("Hello World") 
3. Comments    - Comments are additional readable information which is read by the programmers but ignored by the python interpreter. Eg: # This is a comment
4. Functions   - Function is a code that has a name and it can be reused by specifying its name in the program where needed. Eg: sum(1, 2)
5. Blocks & Indentations - A group of statements is called a block and it can be identified by its indentation. Eg:
        if b > 5:
            a += b
            print(a, b)
            """)
            print()
            print("""
# Python code in order to convert given temperature in K to C. 
# If the temperature is above 40 C, print "Temperature is very high" 
# and if the temperature is below -10 C, print "Temperature is very cold"
#  ^^ comments ^^  #

K = float(input("Enter Temperature in Kelvin: "))     # Statement 1
C = K - 273     # Expression 1
if C < -10:     # Expression 2
    print("Temperature is very cold", C, "celsius")     # Blocks
elif C > 40:
    print("Temperature is very high", C, "celsius)
            """)
            print()

        elif ch2 == 3:
            x += 1
            print(
                """A variable in python represents named location that refers to a value.""")
            print()
            print("Now try assigning a value to variable \"a\"-")
            assign = input("a = ")
            print(f"You assigned the value \"{assign}\" to the variable \"a\"")
            print()

        elif ch2 == 4:
            x += 1
            print("Input statements are used to get an input from the user. Input statements can be used by - \"x = input(\"Enter value for X: \")\"")
            print()
            print("Try using input() function to predict an output:-")
            inputThing = input("Enter Input Statement: ")
            print(f"Output: {eval(inputThing)}")
            print()

    # chapter 3
    elif choice == 3:
        chap3 = PrettyTable(["S. No.", "Data Handling"])
        chap3.add_rows([
            ["1", "Data Types"],
            ["", ""],
            ["2", "Mutable And Immutable Types"],
            ["", ""],
            ["3", "Operators"],
            ["", ""],
            ["4", "Expressions"],
            ["", ""],
            ["5", "Math Module"]
            # ["6", "Debugging"]
        ])
        print(chap3)
        print()
        ch = int(input("Enter Your Choice:- "))
        print()
        print()
    # chapter 4
    elif choice == 4:
        chap4 = PrettyTable(["S. No.", "Flow Of Control"])
        chap4.add_rows([
            ["1", "Types Of Statements"],
            ["", ""],
            ["2", "The \"if\", \"if - else\", \"if - elif\" Statements"],
            ["", ""],
            ["3", "Nested \"if\""],
            ["", ""],
            ["4", "Range() Function"],
            ["", ""],
            ["5", "The \"for\" Loop"],
            ["", ""],
            ["6", "The \"while\" Loop"],
            ["", ""],
            ["7", "Nested Loops"],
        ])
        print(chap4)
        print()
        ch = int(input("Enter Your Choice:- "))
        print()
        print()

    # chapter 5
    elif choice == 5:
        chap5 = PrettyTable(["S. No.", "String Manipulation"])
        chap5.add_rows([
            ["1", "String Operators"],
            ["", ""],
            ["2", "String Slicing"],
            ["", ""],
            ["3", "String Functions & Methods"],
        ])
        print(chap5)
        print()
        ch5 = int(input("Enter Your Choice:- "))
        print()

        if ch5 == 1:
            x += 1
            print("""
String Operators can be used to manipulate string in various ways.
The two basic operators of strings are, \"+\" and \"*\" .

String Operator + (Concatenation):
    The + creates a new string by joining the two operand strings. Eg: "a" + "b" will give "ab".
    [CAUTION! You cannot combine numbers and strings as operands]

String Operator * (Replication):
    The * operator when used with numbers it performs multiplication and returns the product. 
    When used with strings, the string will be replicated.
    [CAUTION! You cannot have strings as both the operands]

            """)
            print("Membership operator: There are two membership operators for strings - \"in\" and \"not in\". Eg:\n>>> if \"hello\" not in \"hello world\":")
            print()
            print("Comparison operator: The standard comparison operators i.e. all relational operators, are - \"<\", \">\", \"=<\", \">=\", \"==\", \"!=\"")
            print()

        elif ch5 == 2:
            x += 1
            print("""
String Slicing refers to a part of a string where strings are sliced using a range of indices.
Eg: In the statement x = \"elephant\", if the given slicing is \"x[3:]\", it will return \"phant\".

In a string, each character is numbered from left to right from 0 to n, and from right to left from -1 to (-n - 1).
            """)
            print()

        elif ch5 == 3:
            x += 1
            print("""
Python offers many built-in functions and methods for string manipulation.
1. len()
    It returns the length of its argument string.
    Eg: >>> len("hello world")
        >>> 11

2. capitalize()
    It returns a copy of the string with its first letter capitalized.
    Eg: >>> "hello world".capitalize()
        >>> "Hello world"

3. count()
    It returns the number of occurrences of the given value.
    Eg: >>> "Whitefield Global School".count("o")
        >>> 3

4. index()
    It returns the lowest index where the specified substring is found.
    Eg: >>> "hello world".index("l")
        >>> 2
    
5. isalpha()
    It returns True if all the characters in the string are alphabets.

6. islower()
    It returns True if all characters in the string are lower case.

7. lower()
    It returns a copy of a string converted into lower case.

8. join()
    It joins a string or character after each member of the string iterator.

9. replace()
    It replaces the desired string with the desired new string.
    Eg: >>> "Hello World".replace("l", "y")
        >>> "Heyyo Woryd"

10. title()
    It capitalizes the first letter of each substring.
    Eg: >>> "hello world".title()
        >>> "Hello World"
            """)

    # chapter 6
    elif choice == 6:
        chap6 = PrettyTable(["S. No.", "List Manipulation"])
        chap6.add_rows([
            ["1", "Creating A List"],
            ["", ""],
            ["2", "List Operations"],
            ["", ""],
            ["3", "Nested Lists"],
            ["", ""],
            ["4", "Working With Lists"],
        ])
        print(chap6)
        print()
        ch = int(input("Enter Your Choice:- "))
        print()
        print()
    elif choice == 7:
        break
    elif choice > 7:
        x += 1
        print("Not a valid choice")
        print()
        continue
