def guess_the_number():
    import random
    from PIL import Image
    print("You can play 2 types of guess the number game\n1. User : You guess the number\n2. Computer : Computer guesses your number\n \n(You can type '0' if you want to quit)")
    inp = int(input("\nEnter your choice (1/2): "))
    if inp == 1:
        x = int(input("\nEnter higher limit of the range: "))
        num = random.randint(1, x)
        guess = 0
        z = 0
        while True:
            guess = int(input(f"Enter your guess between 1 and {x}: "))
            z += 1
            if guess == 0:
                print(
                    f"You have surrendered, the correct number was {num}\n \n")
                break
            elif guess > num:
                print(f"{guess} is too high.")
            elif guess < num:
                print(f"{guess} is too low.")
            elif guess == num:
                if z == 1:
                    print(
                        f"Congratulations! You guessed {num} on your first try!\n \n")
                    break
                else:
                    print(
                        f"Congratulations! You guessed the number {num} right!\n \n")
                    break

    elif inp == 2:
        print("\n(IMPORTANT) Too High: [H] | Too Low: [L] | Correct: [C]\n")
        x = int(input("\nEnter higher limit of the range: "))
        lower = 1
        higher = x
        guessed = ""
        z = 0
        while True:
            if lower != higher:
                BeGuessed = random.randint(lower, higher)
            else:
                BeGuessed = lower  # Can also be higher since; lower = higher
            guessed = input(
                f"Is {BeGuessed} H, L or C: ").lower()
            z += 1

            if guessed == "h":
                if z > 15:
                    print("I'm sorry I can't do this anymore :(")
                    break
                else:
                    higher = BeGuessed - 1
            elif guessed == "l":
                if z > 15:
                    print("I'm sorry I can't do this anymore :(")
                    break
                else:
                    lower = BeGuessed - 1
            elif guessed == "c":
                if z == 1:
                    print(
                        f"LES GOOOOOO!!! I guessed {BeGuessed} on my first try!")
                else:
                    print(f"Yay! I guessed {BeGuessed}!")
                break
            elif guessed == "0":
                print(f"NOOOOOOOO!!!\nI couldn't guess your word :(")

    elif inp > 2 or type(inp) == str:
        print("Why?")
        Image.open("src/unknown.png").show()
