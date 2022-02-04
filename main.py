from PIL import Image
from prettytable import PrettyTable

head = PrettyTable(["Computer Project : Class 11 Science-I"])
head.add_row(["         - by Devasurya & Darshan"])
content = PrettyTable(["Table of contents"])  # main table of contents
table = PrettyTable(["S. No.", "Chapter Name"])
table.add_rows([
    ["1", "Getting Started With Python"],
    [" ", " "],
    ["2", "Python Fundamentals"],
    [" ", " "],
    ["3", "Data Handling"],
    [" ", " "],
    ["4", "Flow Of Control"],
    [" ", " "],
    ["5", "String Manipulation"],
    [" ", " "],
    ["6", "List Manipulation"],
    [" ", " "],
    ["7", "Guess The Number GAME"],
    [" ", " "],
    ["0", "Exit"]
])

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
    print(f"{head}\n")
    print("\t \tTable Of Contents")
    print(f"{table}\n \n")
    choice = int(input("Enter Your Choice:- "))
    print()
    # exit
    if choice == 0:
        print("Thanks for choosing us!")
        break
    # chapter 1
    elif choice == 1:
        chap1 = PrettyTable(["S. No.", "Getting Started With Python"])
        chap1.add_rows(
            [
                ["1", "Pros and Cons Of Python"],
                ["", ""],
                ["2", "Print() Function"]
            ]
        )
        print(chap1, "\n")
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
        print(chap2, "\n")
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
        print(chap3, "\n")
        ch3 = int(input("Enter Your Choice:- "))
        print()
        if ch3 == 1:
            x += 1
            print("""There are 5 main data types in python-
1. Numbers: They can be further classified into integers, floating point numbers and complex numbers.
2. Strings
3. Lists
4. Tuples: Tuples are those lists that cannot be modified. They are a group of comma separated values of any data type within ().
5. Dictionaries: It is an unordered set of comma separated key-value pairs within {} with the requirement that no 2 keys can be the same.
            """)
        elif ch3 == 2:
            x += 1
            print("""Python can be broadly categorised into mutable and immutable types-
1. Immutable: Immutable types are those that can never change their value in place. The following types are immutable- integers, floats, bools, strings, tuples, etc.
2. Mutable  : Mutable types are those values that can be changed in place. Only 3 types are mutable in python which are lists, dictionaries and sets.
""")
        elif ch3 == 3:
            x += 1
            print("""The operators being carried out on data are represented by operators.
1. Arithmetic:
    a) Unary Operators : The operators that act on one operand are called unary operators. Eg: a = 5, where +a is 5.
    b) Binary Operators: Operators that have 2 operands are called binary operators. 
    Example:
      i. +
     ii. -
    iii. *
     iv. / 
      v. // (Rounds off the quotient)
     vi. % (Gives the remainder)
    vii. ** (Exponential)

2. Relational: They determine the relation among the different operands. The different relational operators are- <, >, >=, =<, !=, ==.

3. Identity  : There are 2 identity operators- "is" and "is not". 
    Eg: >>> a = 10
        >>> b = 10
        >>> c = 20
        >>> a is b
        True
        >>> a is c
        False

4. Logical   : Logical operators consists of- "or", "and", "not".

Now, lets recap everything you learnt in this chapter.
    """)
            answer1 = input(
                "Given, a = 100 and b = 350, give the output for the following statement\n>>> a is b\n$ ")
            if answer1.lower() == "true":
                print("Incorrect Answer!")
                break
            elif answer1.lower() == "false":
                print("Correct Answer!")
            else:
                image = Image.open("src/unknown.png")
                image.show()
                break

            print("Great Job! Now here's another one.")
            answer2 = input(
                "Given a = \"hello\" and b = \"\", give the output for the following statement\n>>> a or b\n$ ")
            if answer2 == "hello":
                print("Correct Answer!")
            else:
                image = Image.open("src/unknown.png")
                image.show()
                break

        elif ch3 == 4:
            x += 1
            print("""An Expression in Python is any valid combination of variables, literals and operators.
Different types of expressions are- Arithmetic, Logical, Relational and String.
Example: a, b = 10, 12""")
        elif ch3 == 5:
            x += 1
            print("""A Python module is a file which contains some variables and constants, some functions, objects, etc. defined in it which can be used in other python code.
            
            Working with Math Module of Python:
            In order to work with the math module, you have to first import the math module into the desired program. To do so, use "import math".
            By doing this, you can use the various functions from the math module. Such as- math.sqrt(), math.log().

            Now, lets recap math module.
            """)
            ans = input("How do you import the math module in python?\n>>> ")
            if ans == "import math":
                print("Correct!")
            else:
                print("Incorrect Answer!")
                image = Image.open("src/unknown.png")
                image.show()
                break

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
            ["5", "Nested Loops"],
        ])
        print(chap4, "\n")
        ch4 = int(input("Enter Your Choice:- "))
        print()
        if ch4 == 1:
            x += 1
            print("""Types of Statements in Python are: 
1. Empty Statement- A statement is just nothing
2. Simple (Single) Statement- Any single executable statement
3. Compound Statement- It represents a group of statements executed""")
        elif ch4 == 2:
            x += 1
            print("'if'  : It tests a condition and if the condition evaluates to True, it carries out some function")
            print("'else': It is used along with the 'if' statement, it carries out a specific function if the condition is False")
            print(
                "'elif': It tests a condition if 'if' evaluates to False and carries out a specific function")
            print(
                "\nFor example, given numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 and input 'num';\n")
            f1 = input(
                "What is the 'if' statement to display numbers greater than 5? ")
            if f1 == "num > 5" or f1 == "5 < num":
                print("Correct!")
                print()
            else:
                print("Bruh Moment")
                print()
            f2 = input(
                "What is the 'elif' statement to display numbers lesser than 5? ")
            if f2 == "num < 5" or f1 == "5 > num":
                print("Correct!")
                print()
            else:
                print("Bruh Moment")
                print()
            f3 = input("What is the 'else' statement to all the numbers? ")
            if f3 == "else" or f3 == None:
                print("Correct!")
                print()
            else:
                print("Bruh Moment")
                print()

        elif ch4 == 3:
            x += 1
            print("The nested 'if' statement is when we use an 'if' statement inside an 'if' statement. For example\n")
            print("""
    x = [1, 2, 3]
    y = [1, 2, 3, 4, 5]
    if x in y:
        if len(x) != len(y):
            print("x is a sublist of y, and they are not the same ;)")
    """)  # devasurya did this
        elif ch4 == 4:
            x += 1
            print("""The range(<start>, <stop>) function:
for i in range(1, 100, 2): # This statement will print all odd numbers from 1 to 100, here 1 is the starting point, 100 is the ending point, 2 is the step of increment
    print(i, end=" ") # This will print all odd numbers with a space
""")
        elif ch4 == 5:
            x += 1
            print("""The 'for' loop: 
The 'for' loop is designed to process the items of any sequence one by one. It is written as;
    for <variable> in <sequence>:
For example: 
    for i in range(1, 100):\n=---- o_o ----=\n
            """)
            print("""The 'while' loop:
The 'while' loop is a conditional loop that will repeat the instructions within itself as long as the condition remains True.
For example:
    x = 0
    while x < 50:
        print(x)
        x += 10 
    # This will print 0, 10, 20, 30, 40\n=---- o_o ----=
            """)
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
        print(chap5, "\n")
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
        ])
        print(chap6, "\n")
        ch6 = int(input("Enter Your Choice:- "))
        print()
        if ch6 == 1:
            x += 1
            print("""A List is a standard data type of Python that can store a sequence of values belonging to any type. They are depicted through square brackets [].
In order to create a list, put a number of expressions in square brackets []. Eg: [1, 2, 3, 4, "a", "b", "c", "d"].

Now try creating your own list.""")
            listvalues = eval(input("Enter your list now: "))
            print(f"Your list: {listvalues}")
            print("""Creating a list:
You can use "L = list(1, 2, 3)" in order to make the given data a list.
You can also use the "eval()" function in order to input a list. Eg: eval(input("Enter a list"))""")
            print()
            print("""Accessing a list:
You can use "len()" to find the number of items in a list.""")
            print()
            print("""Concatenation & Replication:
Adding 2 lists L1 + L2 will add the elements of L2 to L1.
Multiplying a list to a natural number will repeat the list.""")
            print()
            print("""In order to pick an element from a list we can do this:
L = ["A", "B", "C"]
L[1] # this will print "B"

NOTE: The index is numbered from 0 to len(L) - 1 from the left, and -1 to -(len(L)) from the right.""")

        elif ch6 == 2:
            x += 1
            print("""Joining Lists:
You can join 2 lists by using the concatenation operator (+).
Eg: L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    L = L1 + L2

NOTE: You cannot add a data of any other type to lists other than lists.

Repeating Lists:
    L1 = ["A", "B", "C"]
    L1 * 2
    will give ["A", "B", "C", "A", "B", "C"]

Slicing Lists:
    In order to obtain a certain part of the list, you can do this:-
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    L[1:3] # will return [2, 3, 4]

""")
            print("Now try the above functions one by one.")
            # pick an element
            List1 = eval(input("Enter a list (x): "))
            Index = int(input("Enter index from above: "))
            print()
            if Index > (len(List1) - 1):
                print("Bruh Moment")
                continue
            print(f"Your selected element is: {List1[Index]}")

            # add lists
            print()
            List2 = eval(input("Enter another list (y): "))
            Putin = input("Type the required step to add the lists: ")
            if Putin == "x + y" or Putin == "x+y" or "+" in Putin:
                print(f"Joined Lists: {List1 + List2}")
            else:
                print("Bruh Moment")

            # replicate lists
            print()
            Replin = input(
                "Type the required step to replicate the list (x): ")
            if "*" in Replin or Replin == "x * 2":
                print(f"Replicated list x: {List1 * 2}")
            else:
                print("Bruh Moment")
            print()

            # list functions and methods
            print("""LIST FUNCTIONS & METHODS:
1. index(<arg>)  : It returns the index of the first matched item from the list.
2. append(<arg>) : Adds an item to the end of the list.
3. extend(<arg>) : Adding multiple elements to the end of the list.
4. insert(<index>, <arg>) : It helps insert an element somewhere in between the list or any position of your choice.
5. pop(<index>)  : Used to remove an item using its index.
6. remove(<arg>) : Removes an element using its value.
7. clear(<arg>)  : Removes all/matched elements from the list.
8. count(<arg>)  : Returns the count of the item you passed as the argument.
9. sort(reverse=bool) : Sorts the items of the list (reverse can be used with this).
""")
        elif ch6 == 3:
            x += 1
            print("""NESTED LISTS:
Nested lists are lists that exist inside another list. Eg: [1, 2, [3, 4], 5].
In order to access the elements of the sublist, use the index of the sublist as a slicing method. Eg: L[2][0].
""")
            print()
            Acc = eval(input("Enter list A: "))
            Acb = eval(input("Enter list B: "))
            Ins = int(input("Enter index where you want to insert B in A: "))
            Acc.insert(Ins, Acb)
            print(f"Nested List: {Acc}")

    # Guess The Number GAME
    elif choice == 7:
        x += 1
        from gtn import guess_the_number
        guess_the_number()

    # Invalid Choice
    elif choice == 8:
        x += 1
        print("Why")
        Image.open("src/unknown.png").show()

    # More Invalid Choice
    elif choice > 8:
        print("Not a valid choice")
# congrats you have a lot of patience
