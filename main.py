import random

# Make the player class
class Player:
    def __init__(self, score=0):
        self.score = score

    def throw(self):
        hand = random.randint(1, 6)
        return hand


print("""
.----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |   ______     | || |     _____    | || |    ______    | |
| |  |_   __ \   | || |    |_   _|   | || |  .' ___  |   | |
| |    | |__) |  | || |      | |     | || | / .'   \_|   | |
| |    |  ___/   | || |      | |     | || | | |    ____  | |
| |   _| |_      | || |     _| |_    | || | \ `.___]  _| | |
| |  |_____|     | || |    |_____|   | || |  `._____.'   | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' """)


# Asks how many players are there and puts them in a list called player_list
number_of_players = int(input("How many players? "))
player_list = []
for i in range(number_of_players):
    p = Player()
    player_list.append(p)


# Iter though the player list
p_num = 1
for player in player_list:
    print("It's Player", p_num, "'s turn.")
    # For every player, play the round
    m_score = 0
    while True:
        print("Player", p_num, "throws the die and scores:")
        hand = player.throw()

        print(hand)
        if hand == 1:
            print("and loses all his points!")
            break
        else:
            m_score += hand
            con = input("Continue?(Y/N) ")
            if con.lower() == "y":
                continue
            else:
                break
    player.score += m_score
    print("Score:", player.score)
    p_num+=1

