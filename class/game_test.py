from SoupPlayer_class import *
from SoupRound_class import *
from Appendix_A import *
from CDIPlayerType_class import *

PAYOFFMAT=[[(3,3),(0,5)],[(5,0),(1,1)]]
#eight pure strategies
p_cdi_list=[(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1)]
ptype1=CDIPlayerType(random.choice(p_cdi_list))
ptype2=CDIPlayerType(random.choice(p_cdi_list))
print("the type of player1's strategy is:",ptype1.p_cdi)
print("the type of player2's strategy is:",ptype2.p_cdi)

# for i in range(10):
#     player1=SoupPlayer(ptype1)
#     player2=SoupPlayer(ptype2)
#     # players=player1,player2
#     # game=SoupRound(players,PAYOFFMAT)
#     game = SoupRound((player1,player2),PAYOFFMAT)
#     game.run()
#     player1.choose_next_type()
#     player2.choose_next_type()
#     ptype1=player1.evolve()
#     ptype2=player2.evolve()

player1=SoupPlayer(ptype1)
player2=SoupPlayer(ptype2)
game = SoupRound([player1,player2],PAYOFFMAT)
game.run()


print("the sequence of history is:")
#for i in player1.games_played.
for game in player1.games_played:
    print(game.payoff()[player1])
print("the payoff of player1:",player1.get_payoff())

for game in player1.games_played:
    print(game.payoff()[player1])
print("the payoff of player2:",player2.get_payoff())
