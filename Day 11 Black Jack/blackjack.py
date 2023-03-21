import random

def sum_and_check_winner(PlayerCards, ComputerCards):
    PlayerSum = sum(PlayerCards)
    ComputerSum = sum(ComputerCards)

    if PlayerSum > ComputerSum:
        print("You win!")
    else:
        print("Computer win!")


def random_numbers():
    return random.randint(2,11)

player = input("Hello, enter your name! ")

playerCards = [random_numbers() for i in range(2)]
botCards = [random_numbers()]

print(player, "Your cards:")
for i in playerCards:
    print("[",i,"]")

print("Computer first card:", botCards)

while True:
    decision = input("Type 'y' to get another card, type 'n' to pass: ")
    
    if decision == 'y':
        randomPlayerCard = random.choice(playerCards)
        additionalCard = random_numbers()
        
        index = playerCards.index(randomPlayerCard)
        playerCards[index] = additionalCard

        print("Your final hand:")
        for i in playerCards:
            print("[",i,"]")
        
        print("Computer final hand:")
        botCards.append(random_numbers())
        for i in botCards:
            print("[",i,"]")
        
        break
    elif decision == 'n':
        print("Your final hand:")
        for i in playerCards:
            print("[",i,"]")
        
        print("Computer final hand:")
        botCards.append(random_numbers())
        for i in botCards:
            print("[",i,"]")
        
        break
    else:
        print("Wrong type, try again!")

sum_and_check_winner(playerCards,botCards)

    
    





