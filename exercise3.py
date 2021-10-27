while True:
    ram = input("Enter a choice (rock, paper, scissors): ")
    raj = input("enter a choice(rock, paper, scissors):")
    if ram == raj:
        print(ram,raj,"Both players choose the same. so It's a tie!")
    elif ram == "rock":
        if raj == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif ram == "paper":
        if raj == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif ram == "scissors":
        if raj == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    continue

