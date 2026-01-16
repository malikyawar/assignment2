from backtracking import nQueensBacktracking, nQeueensBacktrackingVersion2
from las_vegas import nQueensLasVegas

if __name__ == "__main__":
    print("Backtracking:")
    nQueensBacktracking(8)

    print("las Vegas:")
    nQueensLasVegas(8)

    print("Backtracking with starting position:")
    nQeueensBacktrackingVersion2(8, 0, 0)