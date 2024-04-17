''' chess game 
- needs to draw the board
- needs to randomly decide colors? or user select? not user select dont need to add complexity
- needs to select pieces and make moves? html/js front end? this could get complex
- needs to have the backend logic to solve the board or play as computer opponent 
- needs to decide winner 
- needs to know each piece capabilities
- needs to know where each piece is on the board and the borders of the board 
'''

class Board():
    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    def __str__(self):
        for i in range(8):
            print(board[i])

if __name__ == "__main__":
    print("Welcome to chess!")
    board = Board()
    print(board)
