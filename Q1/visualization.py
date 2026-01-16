from typing import List
def visualize_board(size: int, positions: List[int] = None) -> None:
    board = [['.' for _ in range(size)] for _ in range(size)]
    for row, col in enumerate(positions or []):
        if col != -1:
            board[row][col] = 'Q'
    for row in board:
        print(' '.join(row))
    print()