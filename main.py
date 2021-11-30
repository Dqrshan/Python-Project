from prettytable import PrettyTable
head = PrettyTable(["Computer Project : Class 11 Science-I"])
head.add_row(["         - by Devasurya & Darshan"])

content = PrettyTable(["Table of contents"]) # main table of contents

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
table.add_row(["6", "List Manipulation"]) # we could have done `.add_rows([])` xD

while True:
        print(head)
        print()
        print("          Table Of Contents")
        print(table)
        print()
        print()

        choice = int(input("Enter Your Choice:- "))
        print()
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
                        contin = input("Continue? (Yes/No): ")
                        print()
                        if contin.lower() == "yes":
                                continue
                        elif contin.lower() == "no":
                                break
                #
                #
                #
                # subtopic 2
                elif ch1 == 2:
                        strToPrint = str(input("Enter the string you want to print: "))
                        print(f"Printed Text: \"{strToPrint}\"")
                        print()
                        contin = input("Continue? (Yes/No): ")
                        print()
                        if contin.lower() == "yes":
                                continue
                        elif contin.lower() == "no":
                                break

        # chapter 2
        elif choice == 2:
                chap2 = PrettyTable([])
