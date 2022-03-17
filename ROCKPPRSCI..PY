import random

L = ['ROCK', 'PAPER', 'SCISSOR']
player1 = []
player2 = []

i = 1
while i==1:
    def rock_ppr_sci():
        rand = random.choice(L)
        player1 = rand
        rand = random.choice(L)
        player2 = rand
        print("Player 1 : ", player1)
        print("Player 2 : ", player2)
        win(player1,player2)


    def win(player1, player2):
         if player1 == player2:
            print("DRAW")
         elif player1 == 'ROCK' and player2 == 'PAPER':
            print("PLAYER 2 WON")
         elif player1 == 'ROCK' and player2 == 'SCISSOR':
             print("PLAYER 1 WON")
         elif player1 == 'PAPER' and player2 == 'ROCK':
             print("PLAYER 1 WON")
         elif player1 == 'PAPER' and player2 == 'SCISSOR':
             print("PLAYER 2 WON")
         elif player1 == 'SCISSOR' and player2 == 'ROCK':
             print("PLAYER 2 WON")
         elif player1 == 'SCISSOR' and player2 == 'PAPER':
             print("PLAYER 1 WON")
    rock_ppr_sci()

    hit = int(input("PRESS 1 TO RESTART GAME AND 2 TO EXIT: "))
    if hit == 1:
        continue
    elif hit == 2:
        print("GAME ENDED")
        break
