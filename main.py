from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Tes melawan semua bot
print("Vs Quincy:", play(player, quincy, 1000))
print("Vs Abbey:", play(player, abbey, 1000))
print("Vs Kris:", play(player, kris, 1000))
print("Vs Mrugesh:", play(player, mrugesh, 1000))

# Uncomment untuk unit test
# import test_module
