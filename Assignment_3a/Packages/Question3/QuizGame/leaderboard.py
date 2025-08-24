


def get_leader_board():
    leader_board = None
    with open('leaderboard.txt', 'r') as f:
        leader_board = f.readlines()

    return leader_board

def add_to_leader_board(name, score):
    leader_board = None
    with open('leaderboard.txt', 'r') as f:
        leader_board = f.readlines()

    for i in range(0, len(leader_board)):
        leader_board[i] = leader_board[i].strip('\n').split()

    for i in range(0, len(leader_board)):
        leader_board[i][1] = int(leader_board[i][1])

    leader_board.append([name, int(score)])
    print(leader_board)
    leader_board.sort(key=lambda x: x[1], reverse=True)

    with open('leaderboard.txt', 'w') as f:
        for score_card in leader_board:
            f.write(score_card[0] + " " + str(score_card[1]) + '\n')

    print("Updated Leader board")
