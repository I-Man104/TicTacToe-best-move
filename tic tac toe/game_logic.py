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
        # print(f"depth = {returned_depth} AND value = {value}")
        if value > bestValue:
            bestValue = value
            bestMove = move
            bestDepth = returned_depth
            # print("_______________")
            # print(f"bestValue = {value}")
            # print("_______________")
            # print(f"bestMove = {bestMove}")
            # print("_______________")
        elif value == bestValue and returned_depth > bestDepth:
            bestMove = move
            bestDepth = returned_depth
            # print("_______________")
            # print(f"bestValue = {value}")
            # print("_______________")
            # print(f"bestMove = {bestMove}")
            # print("_______________")
            # print(f"bestDepth = {bestDepth}")
            # print("_______________")
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
        try:
            move = int(input(f"You are {player}: Choose number from 1-9: "))
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number from 1 to 9.")
            else:
                isValid = True
                game.makeMove(move - 1, player)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
    game.show()

def aiMove(game, depth, ai_player, memo):
    print("Computer choosing move...")
    move = make_best_move(game, depth, ai_player, memo)
    game.makeMove(move, ai_player)
    game.show()
