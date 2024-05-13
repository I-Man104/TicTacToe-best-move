class TicTacToe:
    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        """Make a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        elif self.board[position] != " " and player == " " :
            self.board[position] = player
            return True
        else:
            print("Invalid Move")
            return False

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def evaluate(self, player):
        if player == "O":
            if self.checkWin() == "O":
                return 1
            elif self.checkWin() == "X":
                return -1
            elif self.gameOver():
                return 0
        elif player == "X":
            if self.checkWin() == "X":
                return 1
            elif self.checkWin() == "O":
                return -1
            elif self.gameOver():
                return 0

    def maximize(self, board_key, depth, player, memo):
        bestValue = -float('inf')
        bestDepth = 0
        for move in self.availableMoves():
            self.makeMove(move, "O")
            returned_value, returned_depth = self.minimax(depth - 1, False, player, memo)
            self.makeMove(move, " ")
            bestValue = max(bestValue, returned_value)
            bestDepth = max(bestDepth, returned_depth)
        memo[(board_key)] = bestValue
        return bestValue, bestDepth

    def minimize(self, board_key, depth, player, memo):
        bestValue = float('inf')
        bestDepth = 9
        for move in self.availableMoves():
            self.makeMove(move, "X")
            returned_value, returned_depth = self.minimax(depth - 1, True, player, memo)
            self.makeMove(move, " ")
            bestValue = min(bestValue, returned_value)
            bestDepth = min(bestDepth, returned_depth) 
        memo[(board_key)] = bestValue
        return bestValue, bestDepth

    def minimax(self, depth, is_maximizing, player, memo={}):
        board_key = tuple(self.board)
        if (board_key) in memo:
            return memo[(board_key)], depth

        if depth == 0 or self.gameOver():
            return self.evaluate(player), depth

        if is_maximizing:
            return self.maximize(board_key, depth, player, memo)
        else:
            return self.minimize(board_key, depth, player, memo)
