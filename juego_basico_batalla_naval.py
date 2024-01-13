import random

def create_board(size):
    board = []
    for i in range(size):
        row = ["-"] * size
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def get_row_col(string):
    valid_input = False
    while not valid_input:
        try:
            row, col = input(string).split(",")
            row = int(row.strip())
            col = int(col.strip())
            if row < 0 or col < 0 or row >= board_size or col >= board_size:
                print("Posición fuera de la cuadrícula.")
            else:
                valid_input = True
        except:
            print("Entrada inválida.")
    return row, col

def place_ships(board, player):
    print(f"{player}, ubica tus barcos.")
    for i in range(num_ships):
        print(f"Barco {i+1}")
        row, col = get_row_col("Ingresa la posición del barco (fila, columna): ")
        while board[row][col] != "-":
            print("Ya existe un barco en esa posición.")
            row, col = get_row_col("Ingresa la posición del barco (fila, columna): ")
        board[row][col] = "O"
        print_board(board)
    print("Barcos ubicados.")

def play_game(player1, player2):
    board1 = create_board(board_size)
    board2 = create_board(board_size)
    place_ships(board1, player1)
    place_ships(board2, player2)
    player1_turn = True
    num_turns = 0
    while num_turns < max_turns:
        if player1_turn:
            print(f"{player1}, es tu turno.")
            print("Tablero del oponente:")
            print_board(board2)
            row, col = get_row_col("Ingresa la posición del disparo (fila, columna): ")
            if board2[row][col] == "O":
                print("¡Acertaste!")
                board2[row][col] = "X"
                if all([all([pos != "O" for pos in row]) for row in board2]):
                    print(f"{player1} ha ganado.")
                    return
            else:
                print("Fallaste.")
            player1_turn = False
        else:
            print(f"{player2}, es tu turno.")
            print("Tablero del oponente:")
            print_board(board1)
            row, col = get_row_col("Ingresa la posición del disparo (fila, columna): ")
            if board1[row][col] == "O":
                print("¡Acertaste!")
                board1[row][col] = "X"
                if all([all([pos != "O" for pos in row]) for row in board1]):
                    print(f"{player2} ha ganado.")
                    return
            else:
                print("Fallaste.")
            player1_turn = True
        num_turns += 1
    print("Límite de turnos alcanzado. Nadie ganó.")

board_size = 5
num_ships = 3
max_turns = 12

print("Bienvenidos al juego de batalla naval.")
player1 = input("Jugador 1, ingresa tu nombre: ")
player2 = input("Jugador 2, ingresa tu nombre: ")


play_game(player1, player2)