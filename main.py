import random

# Make the player class
class Player:
    def __init__(self, score=0):
        self.score = score

    def throw(self):
        hand = random.randint(1, 6)
        return hand


# Make player list
number_of_players = int(input("How many players? "))
player_list = []
for i in range(number_of_players):
    p = Player()
    player_list.append(p)



#player = Player()
for player in player_list:
    throwing = True
    score = 0
    while throwing:
        hand = player.throw()
        print(hand)

        if hand != 1:
            score += hand
            if score >= 10:
                print("you win")
                throwing = False
                break
            else:

                con = input("y/n")
                if con != "y":
                    throwing = False
                continue

        else:
            score = 0
            throwing = False
    player.score += score
    print(player.score)
