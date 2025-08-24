
from questions import questions
from game import conduct_quiz
from leaderboard import get_leader_board, add_to_leader_board

def main():
    name = input("Enter player name:")
    score = conduct_quiz()

    add_to_leader_board(name, score)

    print(get_leader_board())

if __name__ == "__main__":
    main()