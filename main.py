from data import logo, board, is_winner, is_board_full, clean_board, current_board
import random


players = [{"name": "Player X", "symbol": "X"}, {"name": "Player O", "symbol": "O"}]


def game():
    clean_board(board)
    print(
        f"""{logo}
        Welcome to a new Tic Tac Toe Game!
        Here's your brand new board, ready for an exciting game:
        {current_board(board)}
        """
    )

    # First Move
    current_player = random.choice(players)
    current_move = input(
        f"""{current_player['name']} will be the first to move.
        Come on {current_player['name']}, choose a place for your {current_player['symbol']}
        (Input a row and a column, separated by a space):
        """
    )

    current_move_row = int(current_move.split(" ")[0])
    current_move_column = int(current_move.split(" ")[1])

    board[current_move_row][current_move_column] = current_player["symbol"]
    print(current_board(board))

    # Next Moves
    while True:
        # Switch players
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]

        # Input next move
        current_move = input(
            f"""
            Now it's {current_player['name']}'s turn.
            What's your move? (row column):
            """
        )
        current_move_row = int(current_move.split(" ")[0])
        current_move_column = int(current_move.split(" ")[1])
        # Check if input cell is taken
        while board[current_move_row][current_move_column] != " ":
            current_move = input(
                f"""
            Sorry {current_player['name']}, but that cell is taken.
            Try a different move? (row column):
            """
            )
            current_move_row = int(current_move.split(" ")[0])
            current_move_column = int(current_move.split(" ")[1])

        board[current_move_row][current_move_column] = current_player["symbol"]
        print(current_board(board))
        # Check if current player won
        if is_winner(current_player["symbol"]):
            print(f"Congratulations! {current_player['name']} won!")
            play_again = (input("Do you want to play again? Y | N\n")).lower()
            if play_again == "y":
                game()
            else:
                quit()
        else:
            # Check if board is full
            if is_board_full():
                play_again = input(
                    """
                It's a tie!
                Well done both of you, but we have no winner. 
                Do you want to play another game? (Y | N)
                """
                )
                if play_again == "Y":
                    game()
                else:
                    quit()


game()
