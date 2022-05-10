#initializing empty board
from this import d


board = {
    "7": " ", "8": " ", "9": " ",
    "4" : " ", "5": " ","6": " ",
    "1": " ", "2": " ", "3": " "
}

#prints out the board
def print_board(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"]) 
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])  

#checks if the game is still on 
#if there is no winner then return False --> continue
def game_is_on(board, player1, player2):
    if player1_winner(board):
        print(f"{player1} wins!")
        return False
    elif player2_winner(board):
        print(f"{player2} wins!")
        return False
    else: return True

#checks if player 1 has won
def player1_winner(board):
    if ((board["7"] == "X" and board["8"] == "X" and board["9"] == "X") or 
        (board["4"] == "X" and board["5"] == "X" and board["6"] == "X") or
        (board["1"] == "X" and board["2"] == "X" and board["3"] == "X") or
        (board["1"] == "X" and board["2"] == "X" and board["7"] == "X") or
        (board["2"] == "X" and board["5"] == "X" and board["8"] == "X") or
        (board["3"] == "X" and board["6"] == "X" and board["9"] == "X") or
        (board["7"] == "X" and board["5"] == "X" and board["3"] == "X") or
        (board["1"] == "X" and board["5"] == "X" and board["9"] == "X")):
        return True
    else:
        return False

#checks if player2 has won
def player2_winner(board):
    if ((board["7"] == "O" and board["8"] == "O" and board["9"] == "O") or 
        (board["4"] == "O" and board["5"] == "O" and board["6"] == "O") or
        (board["1"] == "O" and board["2"] == "O" and board["3"] == "O") or
        (board["1"] == "O" and board["2"] == "O" and board["7"] == "O") or
        (board["2"] == "O" and board["5"] == "O" and board["8"] == "O") or
        (board["3"] == "O" and board["6"] == "O" and board["9"] == "O") or
        (board["7"] == "O" and board["5"] == "O" and board["3"] == "O") or
        (board["1"] == "O" and board["5"] == "O" and board["9"] == "O")):
        return True
    else:
        return False



#gets the user input if the game is still valid

def main():
    turn = 1
    #gets both player names
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")


    print_board(board)
    print(f"{player1} and {player2}, you will play Tic Tac Toe on this game field above!")
    print(f"{player1} will play with 'X', {player2} will play with 'O'")
    print(f"{player1} starts!")


    while game_is_on(board, player1, player2) and turn < 10:

        while True:
            if turn % 2 == 0:
                inp = input(f"{player2} your turn, which index would you prefer: ")
            else:
                inp = input(f"{player1} your turn, which index would you prefer: ")
            

            if int(inp) < 1 or int(inp) > 9:
                print("Not in the board, index must be between 1 and 9")
            elif board[f"{inp}"] == " " and turn % 2 == 0:
                board[f"{inp}"] = "O"
                break
            elif board[f"{inp}"] == " " and turn % 2 != 0:
                board[f"{inp}"] = "X"
                break
            else:
                print("Field already been used!")
                
        
        turn += 1
        print_board(board)
        
    if turn == 10:
        print("There is no winner!")


main()


