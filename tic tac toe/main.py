from TicTacToe import TicTacToe
from game_logic import choosePlayer, playerMove, aiMove, changePlayer

def playGame():
    memo = {}
    game = TicTacToe()
    game.show()

    player = choosePlayer()
    
    depth = 9
    ai_player = changePlayer(player)
    while not game.gameOver():
        if player == 'X':
            playerMove(game, player)
            depth -= 1
            if depth == 0 or game.gameOver():
                break
            aiMove(game, depth, ai_player, memo)
            depth -= 1
        else:
            aiMove(game, depth,ai_player, memo)
            depth -= 1
            if depth == 0 or game.gameOver():
                break
            playerMove(game, player)
            depth -= 1

    print("Game Over. " + game.whoWon() + " Wins")

if __name__ == '__main__':
    playGame()
