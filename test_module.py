import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class TestRPS(unittest.TestCase):
    def test_winrate(self):
        self.assertGreater(play(player, quincy, 1000), 0.6)
        self.assertGreater(play(player, abbey, 1000), 0.6)
        self.assertGreater(play(player, kris, 1000), 0.6)
        self.assertGreater(play(player, mrugesh, 1000), 0.6)

if __name__ == "__main__":
    unittest.main()
