from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..R.
.R.."""
    print("Board 1:")
    print(board1)
    checkmate(board1)  # Expected: Fail
    #2,1 | 2,0 | 3,0 | 3,1 | 3,2 | 2,2 | 1,2 | 1,1 | 1,0
    board2 = """\
Q...
.K..
..Q.
.Q.B"""
    print("Board 2:")
    print(board2)
    checkmate(board2)  # Expected: Fail
    #2,1 | 2,0 | 3,0 | 3,1 | 3,2 | 2,2 | 1,2 | 1,1 | 1,0
    board2 = """\
Q...
.K..
..R.
.Q.B"""
    print("Board 3:")
    print(board2)
    checkmate(board2)  # Expected: Fail
    #2,1 | 2,0 | 3,0 | 3,1 | 3,2 | 2,2 | 1,2 | 1,1 | 1,0
    board3 = """\
..
.K"""
    print("Board 4:")
    print(board3)
    checkmate(board3)  # Expected: Fail


if __name__ == "__main__":
    main()