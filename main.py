import random  # 1st step


class TicTacToe:  # 2nd step

    def __init__(self):  # 3rd step
        self.board = []

    # 4th step
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):  # 5th step
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):  # 6th step
        self.board[row][col] = player

    def is_player_win(self, player):  # 7th step
        win = None

        n = len(self.board)

        for i in range(n):  # checking rows 8th step
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):  # checking columns 9th step
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True  # checking diagonals 10th step
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):  # 11th step
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):  # 12th step
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):  # 13th step
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # 14th step input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # 15th step fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # 16th step checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # 17th step checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # 18th step swapping the turn
            player = self.swap_player_turn(player)

        # 19th step showing the final view of board
        print()
        self.show_board()


# 20th step starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
import random  # 1st step


class TicTacToe:  # 2nd step

    def __init__(self):  # 3rd step
        self.board = []

    # 4th step
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):  # 5th step
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):  # 6th step
        self.board[row][col] = player

    def is_player_win(self, player):  # 7th step
        win = None

        n = len(self.board)

        for i in range(n):  # checking rows 8th step
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):  # checking columns 9th step
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True  # checking diagonals 10th step
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):  # 11th step
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):  # 12th step
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):  # 13th step
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # 14th step input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # 15th step fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # 16th step checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # 17th step checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # 18th step swapping the turn
            player = self.swap_player_turn(player)

        # 19th step showing the final view of board
        print()
        self.show_board()


# 20th step starting the game:
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
