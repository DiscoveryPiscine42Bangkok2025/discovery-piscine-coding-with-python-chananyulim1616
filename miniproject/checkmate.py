def checkmate(board: str) -> None:
    rows = board.split('\n')
    attacked_path = []
    print(rows)
    size_board = (len(rows)-1, len(rows[0])-1 if rows else 0)
    print("Size of board:", size_board)
    chess_pos = []
    # left bottom is (0,0), right top is (size_board[0]-1, size_board[1]-1)
    def profile_path(role, x, y):
        # print(f"Profiling path for {role} at ({x},{y})")
        sub_attacked_path = []
        if role == 'P':
            if x+1 < size_board[0] and y-1 >= 0:
                sub_attacked_path.append((x+1, y-1))
            if x+1 < size_board[0] and y+1 < size_board[1]:
                sub_attacked_path.append((x+1, y+1))
        elif role == 'R':
            for side in [-1, 1]:
                for i in range(1,size_board[0]+1): # x = 2 0 1 2
                    i = side * i
                    if (i+x,y) not in chess_pos and 0 <= i+x <= size_board[0]:
                        attacked_path.append((i+x,y))
                    else:
                        attacked_path.append((x,i+y))
                        break
                for i in range(1,size_board[1]+1): # x = 2 0 1 2
                    i = side * i
                    if (x,i+y) not in chess_pos and 0 <= i+y <= size_board[1]:
                        attacked_path.append((x,i+y))
                    else:
                        attacked_path.append((x,i+y))
                        break

        elif role == 'B':
            for side_x in [-1, 1]:
                for side_y in [-1, 1]:
                    for i in range(1, min(size_board[0], size_board[1])+1):
                        i = side_x * i
                        j = side_y * i
                        if (i+x, j+y) not in chess_pos and 0 <= i+x <= size_board[0] and 0 <= j+y <= size_board[1]:
                            attacked_path.append((i+x, j+y))
                        else:
                            attacked_path.append((i+x, j+y))
                            break
        elif role == 'Q':
            sub_attacked_path += profile_path('R', x, y)
            sub_attacked_path += profile_path('B', x, y)

        print("Attacked path:", attacked_path)
        return sub_attacked_path

    for sub_col in rows:
        for point in sub_col:
            if point == 'K':
                king_pos = (size_board[0]-rows.index(sub_col), size_board[1]-1-sub_col.index(point))
            elif point != '.':
                chess_pos.append((size_board[0]-rows.index(sub_col), sub_col.index(point)))

    for sub_col in rows:
        for point in sub_col:
            if point == 'R':
                attacked_path += profile_path('R', size_board[0]-rows.index(sub_col), sub_col.index(point))
            elif point == 'B':
                attacked_path += profile_path('B', size_board[0]-rows.index(sub_col), sub_col.index(point))
            elif point == 'Q':
                attacked_path += profile_path('Q', size_board[0]-rows.index(sub_col), sub_col.index(point))
            elif point == 'P':
                attacked_path += profile_path('P', size_board[0]-rows.index(sub_col), sub_col.index(point))
            elif point == 'K':
                king_pos = (size_board[0]-rows.index(sub_col), size_board[1]-1-sub_col.index(point))
            # print(attacked_path)
            attacked_path = list(set(attacked_path))
    
    print("King position:", king_pos)
    if king_pos in attacked_path:
        print('got_checked')
        for i in [king_pos[0]-1, king_pos[0], king_pos[0]+1]:
            for j in [king_pos[1]-1, king_pos[1], king_pos[1]+1]:
                if 0 <= i < size_board[0] and 0 <= j < size_board[1]:
                    if (i, j) not in attacked_path and (i, j) != king_pos:
                        print(f"Fail at: {(i, j)}")
                        return
        print("Success")
    else:
        print("Fail")