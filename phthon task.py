1.Create a program to compare three numbers and find the bigger numbers. [topics covered: identified, variable, types, operator, if statement]

a = int(input("enter the value:"))
b = int(input("enter the value:"))
c = int(input("ener the value:"))
if a > b and a > c:
   highes = a

elif b > a and b > c:
     highest =b
else:
     highest = c

print("the bigger value is ", highest)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2.Write the above solution in a functionwhichtakes take numbers and return the bigger number


def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest

# Driven code
a = 20
b = 18
c = 10
print(maximum(a, b, c))

3.Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


name=input("enter the name:")
age=int(input("enter the age:"))
i=100-age
k=i+2021
print(name,"your age will become 100  at the year",k)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
6.Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock



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