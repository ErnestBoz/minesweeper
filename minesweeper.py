import random
from collections import deque
import copy


def init_board(size=10):
    board = []
    for col in range(size):
        row = [None for i in range(size)]
        board.append(row)
    return board



def print_board(board):
    # Create a deep copy of the board so the original is not modified
    board_copy = copy.deepcopy(board)

    # Modify the copy
    board_copy.insert(0, [" ", " ", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    board_copy.insert(1, [" "])
    for i, letter in enumerate("ABCDEFGHIJ", start=2):
        board_copy[i].insert(0,f"{letter}  ")

    # Print the modified copy
    print(" ")
    for row in board_copy:
        print(" ".join(str(cell) if cell is not None else "-" for cell in row))



# print_board(init_board())


def mine_coords(count=10):  #change the number of mines here
    mines = []
    while len(mines) < count:
        (x, y) = (random.randint(0, 9), random.randint(0, 9))
        if (x,y) in mines:
            continue
        else:
            mines.append((x,y))
    return mines

# print(mines())

def cli_coordinates_input():
    

    alphabet = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,  #these are for rows
        'G': 7, 'H': 8, 'I': 9, 'J': 10
    } #allows for chess-like coordinates

    while True:
        try:
            print(" ")
            coords = input("Input coordinates, row and column (e.g. C4 <---> A-J, 0-9): ").upper() #input the coordinates
            if len(coords) != 2: #limits the length of the input to 2
                raise ValueError
            x, y = alphabet[coords[0]], int(coords[1])
            if x not in alphabet.values() or not (0 <= y <= 26): #limits to only 26
                raise ValueError
            return (x - 1, y)
        except (ValueError, KeyError, TypeError): #in case of an error, warning issued
            print("Incorrect format. Input coordinates, row and column (e.g. C4 <---> A-J, 0-9): ")




def count_mines(board, mines, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            if (r, c) in mines:
                count += 1
    return count


def reveal_cells(board, mines, start):     #understand this:
    queue = deque([start])
    visited = set()
    
    while queue:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        mine_count = count_mines(board, mines, row, col)
        board[row][col] = mine_count
        
        # If there are no mines around this cell, add its neighbors to the queue
        if mine_count == 0:
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if (r, c) not in visited:
                        queue.append((r, c))
    # print_board(board)


    
def victory(board, mines):
    number_of_mines = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == None:
                number_of_mines += 1
    if number_of_mines == len(mines):
        print_board(board)
        print("        YOU WIN!")
        

        return True
        
def check(board, mines, coordinates):
    if coordinates in mines:
        row, col = coordinates
        board[row][col] = "X"
        print_board(board)
        print("        YOU LOSE!")
        
        return True
    else:
        reveal_cells(board, mines, coordinates)
        return False


def game():
    # board = init_board()
    # mines = mine_coords()
    # used_coords =[]
    # print("welcome to the game!")
    while True:
        try: 
          
            coordinates = cli_coordinates_input()
            
            if coordinates in used_coords:
                raise ValueError
            else: 
                used_coords.append(coordinates)
                if check(board, mines, coordinates) == True:
                    
                    break

                if victory(board,mines) == True:

                    break
            print_board(board)
                
                
                    
        except (ValueError):
            print("You have already checked that cell")

    

        

board = init_board()
mines = mine_coords()
used_coords =[]
print("welcome to the game!")
game()
while True:
    again = input("Try again? Y/n: ").strip().lower()  
    if again == "y":
        board = init_board()
        mines = mine_coords()
        used_coords =[]
        game()
   
    else:
        print("BYE")
        break




# after a change, rerun this: pyinstaller --onefile --console minesweeper.py


