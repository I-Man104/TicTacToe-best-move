def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"

def make_best_move(board, depth, player, memo):
    bestMove = None
    bestValue = -float('inf')
    bestDepth = 0
    print("____________________________"+player+"__________________________________")
    for move in board.availableMoves():
        board.makeMove(move, player)
        value, returned_depth = board.minimax(depth, False, player, memo)
        board.makeMove(move, " ")
        print(returned_depth)
        if value > bestValue:
            bestValue = value
            bestMove = move
            bestDepth = returned_depth
        elif value == bestValue and returned_depth > bestDepth:
            bestDepth = returned_depth
    return bestMove

# Actual game
def choosePlayer():
    player = input("Do you want to play with X or O? (X always starts): ").upper()
    if player != 'X' and player != 'O':
        print("Invalid input. Defaulting to X.")
        player = 'X'
    return player

def playerMove(game, player):
    isValid = False
    while not isValid:
        move = int(input(f"You are {player}: Choose number from 1-9: "))
        isValid = game.makeMove(move - 1, player)
    game.show()

def aiMove(game, depth, ai_player, memo):
    print("Computer choosing move...")
    move = make_best_move(game, depth, ai_player, memo)
    game.makeMove(move, ai_player)
    game.show()
