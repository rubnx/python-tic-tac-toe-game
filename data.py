logo = """

                                                                                                                                                                         
8888888 8888888888 8 8888     ,o888888o.             8888888 8888888888   .8.           ,o888888o.             8888888 8888888888 ,o888888o.     8 8888888888            
      8 8888       8 8888    8888     `88.                 8 8888        .888.         8888     `88.                 8 8888    . 8888     `88.   8 8888                  
      8 8888       8 8888 ,8 8888       `8.                8 8888       :88888.     ,8 8888       `8.                8 8888   ,8 8888       `8b  8 8888                  
      8 8888       8 8888 88 8888                          8 8888      . `88888.    88 8888                          8 8888   88 8888        `8b 8 8888                  
      8 8888       8 8888 88 8888                          8 8888     .8. `88888.   88 8888                          8 8888   88 8888         88 8 888888888888          
      8 8888       8 8888 88 8888                          8 8888    .8`8. `88888.  88 8888                          8 8888   88 8888         88 8 8888                  
      8 8888       8 8888 88 8888                          8 8888   .8' `8. `88888. 88 8888                          8 8888   88 8888        ,8P 8 8888                  
      8 8888       8 8888 `8 8888       .8'                8 8888  .8'   `8. `88888.`8 8888       .8'                8 8888   `8 8888       ,8P  8 8888                  
      8 8888       8 8888    8888     ,88'                 8 8888 .888888888. `88888.  8888     ,88'                 8 8888    ` 8888     ,88'   8 8888                  
      8 8888       8 8888     `8888888P'                   8 8888.8'       `8. `88888.  `8888888P'                   8 8888       `8888888P'     8 888888888888          

                                             
"""

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# Function that prints the current state of the board
def current_board(board):
    return f"""
    +---+---+---+
    | {board[0][0]} | {board[0][1]} | {board[0][2]} |
    +---+---+---+
    | {board[1][0]} | {board[1][1]} | {board[1][2]} |
    +---+---+---+
    | {board[2][0]} | {board[2][1]} | {board[2][2]} |
    +---+---+---+
    """


# Clean board for new game
def clean_board(board):
    board[0] = [" ", " ", " "]
    board[1] = [" ", " ", " "]
    board[2] = [" ", " ", " "]


# Check if the current player just won
def is_winner(current_player):
    # First we check columns and rows
    for i in range(3):
        if (
            board[i][0] == current_player
            and board[i][1] == current_player
            and board[i][2] == current_player
        ):
            return True
        elif (
            board[0][i] == current_player
            and board[1][i] == current_player
            and board[2][i] == current_player
        ):
            return True
        else:
            pass
    # Then we check the two diagonals
    if (
        board[0][0] == current_player
        and board[1][1] == current_player
        and board[2][2] == current_player
    ):
        return True
    elif (
        board[0][2] == current_player
        and board[1][1] == current_player
        and board[2][0] == current_player
    ):
        return True
    else:
        return False


# Check if the board is already full
def is_board_full():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


# My first approach was a bit rough
# if (
#     board[0][0] != " "
#     and board[0][1] != " "
#     and board[0][2] != " "
#     and board[1][0] != " "
#     and board[1][1] != " "
#     and board[1][2] != " "
#     and board[2][0] != " "
#     and board[2][1] != " "
#     and board[2][2] != " "
# ):
#     return True
