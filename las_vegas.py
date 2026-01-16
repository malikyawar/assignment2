import random
from typing import List, Tuple
from utils import is_safe
from visualization import visualize_board

def nQueens_las_vegas(n: int, max_attempts: int = 1000) -> List[Tuple[int, int]]:
    for attempt in range(max_attempts):
        board = []
        for row in range(n):
            col = random.randint(0, n - 1)
            if is_safe(board, row, col):
                board.append((row, col))
            else:
                break
        if len(board) == n:
            return board
    return []