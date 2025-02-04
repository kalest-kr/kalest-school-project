files = ['a','b','c','d','e','f','g','h']  # 가로(col)
ranks = ['8','7','6','5','4','3','2','1']  # 세로(row)

board = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2' ,'d2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]

def square_to_rc(square: str) -> tuple:
    """ 예: 'a2' -> (6, 0) """
    file = square[0]  # 'a' ~ 'h'
    rank = square[1]  # '1' ~ '8'
    col = files.index(file)
    row = ranks.index(rank)
    return row, col

temp_rook_list = []

def rc_to_square(row: int, col: int) -> str:
    """ 예: (6, 0) -> 'a2' """
    return files[col] + ranks[row]

def rook_attack(x):
    row, col = square_to_rc(x.pos)
    for i in range(1, 9):
        attack_col = col + str(i)
        temp_rook_list.append(attack_col)
    for i in range(97, 105):
        alphabet = chr(i)
        attack_row = alphabet + str(col)
        temp_rook_list.append(attack_row)
    return temp_rook_list

class piece:
    def __init__(self, role, color, pos):
        self.role = role
        self.color = color
        self.pos = pos
        self.active = True

    def move(self, square):
        current_row, current_col = square_to_rc(self.pos)
        target_row, target_col = square_to_rc(square)
        if self.active == False:
            print("that piece have been captured")
            return
        elif self.color == "white":
            if self.role == "pawn":
                if target_col == current_col and target_row == current_row - 1:
                    if square_check(square):
                        self.pos = square
                    else:
                        print("that square is currently unavailable")
                    return
                elif abs(target_col - current_col) == 1 and target_row == current_row - 1:
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"pawn takes on {square}")
                    else:
                        print("that move is currently unavailable")
                    return
                elif current_row == 6 and target_row == 4 and current_col == target_col:
                    middle_square = rc_to_square(5, current_col)
                    if square_check(middle_square) and square_check(square):
                        self.pos = square
                    else:
                        print("that move is currently unavailable")
                    return
                else:
                    print("that move is currently unavailable")
                return
            elif self.role == "knight":
                if abs(target_col - current_col) == 1 and abs(target_row - current_row) == 2:
                    if color_check(square, self.color):
                        print(f"Nx{square}")
                        self.pos = square
                    else:
                        print("that move is currently unavailable")
                        return
                elif abs(target_col - current_col) == 2 and abs(target_row - current_row) == 1:
                    if color_check(square, self.color):
                        print(f"Nx{square}")
                        self.pos = square
                    else:
                        print("that move is currently unavailable")
                        return
                else:
                    print("that move is currently unavailable")
                    return
            elif self.role == "bishop":
                if abs(target_col - current_col) == abs(target_row - current_row):
                    col_size = target_col - current_col
                    row_size = target_row - current_row
                    for x in range(abs(col_size)):
                        middle_col_size = col_size - x
                        middle_row_size = row_size - x
                        temp_row = current_row - middle_row_size
                        temp_col = current_col - middle_col_size
                        bishop_mid_square = rc_to_square(temp_row, temp_col)
                        if square_check(bishop_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Bx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
            elif self.role == "rook":
                if current_row == target_row:
                    col_size = target_col - current_col
                    for x in range(abs(col_size)):
                        middle_col_size = col_size - x
                        temp_col = current_col - middle_col_size
                        rook_mid_square = rc_to_square(current_row, temp_col)
                        if square_check(rook_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        print(f"Rx{square}")
                        rook_attack_list1 = []
                        rook_attack_list2 = []  # 룩 공격 경로
                        self.pos = square
                        rook_attack_list1 = rook_attack(white_rook1)
                        rook_attack_list2 = rook_attack(white_rook2)
                    else:
                        print("that move is currently unavailable")
                        return
                elif current_col == target_col:
                    row_size = target_row - current_row
                    for x in range(abs(row_size)):
                        middle_row_size = row_size - x
                        temp_row = current_row - middle_row_size
                        rook_mid_square = rc_to_square(temp_row, current_col)
                        if square_check(rook_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        rook_attack_list = []
                        rook_attack(white_rook1)
                        rook_attack(white_rook2)
                        print(f"Rx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
            elif self.role == "queen":
                if current_row == target_row:
                    col_size = target_col - current_col
                    for x in range(abs(col_size)):
                        middle_col_size = col_size - x
                        temp_col = current_col - middle_col_size
                        rook_mid_square = rc_to_square(current_row, temp_col)
                        if square_check(rook_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Qx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
                elif current_col == target_col:
                    row_size = target_row - current_row
                    for x in range(abs(row_size)):
                        middle_row_size = row_size - x
                        temp_row = current_row - middle_row_size
                        rook_mid_square = rc_to_square(temp_row, current_col)
                        if square_check(rook_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Qx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
                elif abs(target_col - current_col) == abs(target_row - current_row):
                    col_size = target_col - current_col
                    row_size = target_row - current_row
                    for x in range(abs(col_size)):
                        middle_col_size = col_size - x
                        middle_row_size = row_size - x
                        temp_row = current_row - middle_row_size
                        temp_col = current_col - middle_col_size
                        bishop_mid_square = rc_to_square(temp_row, temp_col)
                        if square_check(bishop_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Qx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
            elif self.role == "king":
                if current_row == target_row and abs(target_col - current_col) == 1:
                    col_size = target_col - current_col
                    for x in range(abs(col_size)):
                        middle_col_size = col_size - x
                        temp_col = current_col - middle_col_size
                        rook_mid_square = rc_to_square(current_row, temp_col)
                        if square_check(rook_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Kx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
                elif current_col == target_col and abs(target_row - current_row) == 1:
                    row_size = target_row - current_row
                    for x in range(abs(row_size)):
                        middle_row_size = row_size - x
                        temp_row = current_row - middle_row_size
                        rook_mid_square = rc_to_square(temp_row, current_col)
                        if square_check(rook_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Kx{square}")
                    else:
                        print("that move is currently unavailable")
                        return
                elif abs(target_col - current_col) == abs(target_row - current_row)\
                        and abs(target_row - current_row) == 1 and abs(target_col - current_col) == 1:
                    col_size = target_col - current_col
                    row_size = target_row - current_row
                    for x in range(abs(col_size)):
                        middle_col_size = col_size - x
                        middle_row_size = row_size - x
                        temp_row = current_row - middle_row_size
                        temp_col = current_col - middle_col_size
                        bishop_mid_square = rc_to_square(temp_row, temp_col)
                        if square_check(bishop_mid_square):
                            print("that move is currently unavailable")
                            return
                    if color_check(square, self.color):
                        self.pos = square
                        print(f"Kx{square}")
                    else:
                        print("that move is currently unavailable")
                        return

def square_check(square: str) -> bool:
    for p in pieces_list:
        if p.pos == square:
            return False
    return True

def color_check(square: str, color: str) -> bool:
    for p in pieces_list:
        if p.pos == square and p.color != color:
            p.active = False
            return True
    return  False

white_pawn1 = piece("pawn", "white", "a2")
white_pawn2 = piece("pawn", "white", "b2")
white_pawn3 = piece("pawn", "white", "c2")
white_pawn4 = piece("pawn", "white", "d2")
white_pawn5 = piece("pawn", "white", "e2")
white_pawn6 = piece("pawn", "white", "f2")
white_pawn7 = piece("pawn", "white", "g2")
white_pawn8 = piece("pawn", "white", "h2")

white_night1 = piece("knight", "white", "b1")
white_night2 = piece("knight", "white", "g1")

white_bishop1 = piece("bishop", "white", "b1")
white_bishop2 = piece("bishop", "white", "f1")

white_rook1 = piece("rook", "white", "a1")
white_rook2 = piece("rook", "white", "h1")

white_king = piece("king", "white", "e1")
white_queen = piece("queen", "white", "d1")

black_pawn1 = piece("pawn", "black", "a7")
black_pawn2 = piece("pawn", "black", "b7")
black_pawn3 = piece("pawn", "black", "c7")
black_pawn4 = piece("pawn", "black", "d7")
black_pawn5 = piece("pawn", "black", "e7")
black_pawn6 = piece("pawn", "black", "f7")
black_pawn7 = piece("pawn", "black", "g7")
black_pawn8 = piece("pawn", "black", "h7")

black_night1 = piece("knight", "black", "b8")
black_night2 = piece("knight", "black", "g8")

black_bishop1 = piece("bishop", "black", "b8")
black_bishop2 = piece("bishop", "black", "f8")

black_rook1 = piece("rook", "black", "a8")
black_rook2 = piece("rook", "black", "h8")

black_king = piece("king", "black", "e8")
black_queen = piece("queen", "black", "d8")

pieces_list = [
    white_pawn1, white_pawn2, white_pawn3, white_pawn4,white_pawn5, white_pawn6, white_pawn7, white_pawn8, white_night1,
    white_night2, white_rook1, white_rook2, white_bishop1, white_bishop2, white_queen, white_king, black_rook1, black_rook2,
    black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8, black_night1,
    black_night2, black_bishop1, black_bishop2, black_queen, black_king
]