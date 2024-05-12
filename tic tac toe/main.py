from TicTacToe import TicTacToe
from game_logic import choosePlayer, playerMove, aiMove

def playGame():
    memo = {}
    game = TicTacToe()
    game.show()

    player = choosePlayer()
    
    depth = 8
    ai_player = 'O' if player == 'X' else 'X'
    while not game.gameOver():
        if player == 'X':
            playerMove(game, player)
            if game.gameOver():
                break
            depth -= 1
            aiMove(game, depth, ai_player, memo)
            depth -= 1
        else:
            aiMove(game, depth,ai_player, memo)
            if game.gameOver():
                break
            depth -= 1
            playerMove(game, player)
            depth -= 1

    print("Game Over. " + game.whoWon() + " Wins")

if __name__ == '__main__':
    playGame()
