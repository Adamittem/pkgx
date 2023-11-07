import random
import time
import sys

def print_matrix(rows, columns):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[]{}|;:,.<>?/`~"
    matrix = [[random.choice(symbols) for _ in range(columns)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            if i == 0 and j == columns - 1:
                sys.stdout.write(matrix[i][j])
            else:
                sys.stdout.write(matrix[i][j] + " ")
        sys.stdout.write('\n')
    
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write("\033[H")

try:
    while True:
        rows, columns = 30, 80  # Ukuran layar konsol
        print_matrix(rows, columns)
except KeyboardInterrupt:
    pass
