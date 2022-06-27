import Beginner.Day14.art
import Beginner.Day14.game_data
import random

def createVariant(player1, player2):
    """
    #Format the account data into printable format.
    :param player1:
    :param player2:
    :return:
    """
    variantA="Compare A: "+player1["name"]+", a "+player1["description"]+", from "+player1["country"]+"."
    variantB="Compare B: "+player2["name"]+", a "+player2["description"]+", from "+player2["country"]+"."
    return variantA, variantB

def compare(a,b):
    """
    Compare what number is bigger
    :param a:
    :param b:
    :return:
    """
    if a>b:
        return 1
    return 0

def verify(playerA):
    """
    Check for playerA == playerB
    :param playerA:
    :return:
    """
    playerB = random.choice(Beginner.Day14.game_data.data)
    while playerA["name"] == playerB["name"]:
        playerB = random.choice(Beginner.Day14.game_data.data)
    return playerB

def afis(a,b):
    """
    Format the start
    :param a:
    :param b:
    :return:
    """
    print(Beginner.Day14.art.logo)
    var1, var2 = createVariant(a, b)
    print(var1)
    print(Beginner.Day14.art.vs)
    print(var2)

def play():
    curent_score=0
    # Generate a random account from the game data.
    playerA = random.choice(Beginner.Day14.game_data.data)
    playerB = random.choice(Beginner.Day14.game_data.data)
    while playerA["name"] == playerB["name"]:
        playerB=random.choice(Beginner.Day14.game_data.data)
    play=True
    while play:
        afis(playerA, playerB)
        #Ask for a guess
        answer=input("Who has more followers? Type 'A' or 'B': ")
        if answer == "A":
            #Check if user is correct
            if compare(playerA["follower_count"], playerB["follower_count"]) == 1:
                curent_score +=1
                print(f"You're right! Current score: {curent_score}")
                playerA=playerA
                playerB=verify(playerA)
            else:
                play=False
                print(f"Sorry, that's wrong. Final score: {curent_score}")
        elif answer == "B":
            # Check if user is correct
            if compare(playerA["follower_count"], playerB["follower_count"]) == 0:
                curent_score +=1
                print(f"You're right! Current score: {curent_score}")
                playerA=playerB
                playerB=verify(playerA)
            else:
                play=False
                print(f"Sorry, that's wrong. Final score: {curent_score}")
        else:
            play=False
            print(f"Sorry, you type an option which not exist, so you lose! Final score: {curent_score}")

play()