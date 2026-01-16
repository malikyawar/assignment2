from typing import List, Tuple
from utils import is_safe
from visualization import visualize_board

def nQueenstracking(size: int) -> Tuple[bool, List[List[int]]]:
    positions = [-1] * size

    def backtrack(row: int) -> bool:
        if row == size:
            return True
        for col in range(size):
            if is_safe(positions, row, col):
                positions[row] = col
                if backtrack(row + 1):
                    return True
                positions[row] = -1
        return False
    
    success = backtrack(0)
    board = [[0] * size for _ in range(size)]
    if success:
        for r in range(size):
            board[r][positions[r]] = 1
    return success, board