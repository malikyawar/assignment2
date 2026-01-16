from typing import List
def is_safe(position: List[int], current_row: int, col: int) -> bool:
    for r in range(current_row):
        if position[r] == col:
            return False
        if abs(position[r] - col) == abs(r - current_row):
            return False
    return True