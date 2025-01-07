print("Nicely done folks, lets check the points")

rank = 0

Winner = True 

def win():
    if Winner == True:
        rank = rank +100
        print("Congrats and bingo: ", rank)

def lost():
    Winner = False
    if Winner == False:
        rank = rank - 100
        print("You got wrecked: ", rank)

