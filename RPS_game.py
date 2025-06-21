import random

def play(player1, player2, num_games, verbose=False):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0
    moves = ["R", "P", "S"]
    outcomes = {"RP": 1, "RS": 0, "PR": 0, "PS": 1, "SR": 1, "SP": 0}

    for i in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        if verbose:
            print(f"Game {i+1}: player1: {p1}, player2: {p2}")

        if p1 == p2:
            pass
        elif outcomes[p1 + p2] == 1:
            p1_score += 1
        else:
            p2_score += 1

        p1_prev = p1
        p2_prev = p2

    if verbose:
        print("Final score:")
        print("Player 1:", p1_score)
        print("Player 2:", p2_score)

    return p1_score / num_games

def quincy(prev_play):
    return "P"

def abbey(prev_play, counter=[0]):
    counter[0] += 1
    return ["R", "P", "S"][counter[0] % 3]

def kris(prev_play):
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]
    return {"R": "P", "P": "S", "S": "R"}[guess]
