# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = " ".join(f"{val:4}" for val in row)
        print(f"  {formatted_row}")
    print()

def get_matrix_input(name="Matrix"):
    print(f"\n--- Entering {name} ---")
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows > 0 and cols > 0:
                break
            print("Please enter positive integers for dimensions.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                row_values = [int(x) for x in row_input.split()]
                
                if len(row_values) != cols:
                    print(f"Error: Expected {cols} values, got {len(row_values)}. Try again.")
                else:
                    matrix.append(row_values)
                    break
            except ValueError:
                print("Invalid input. Please enter space-separated integers.")
    return matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


def add_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
            
    return result


def multiply_matrices(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    cols_b = len(mat_b[0])
    
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
                
    return result


def main():
    print("       MATRIX OPERATIONS PROGRAM       ")

    print("TRANSPOSE A MATRIX")
    matrix_a = get_matrix_input("Matrix A")
    print_matrix(matrix_a, "Original Matrix")
    
    transposed = transpose_matrix(matrix_a)
    print_matrix(transposed, "Transposed Matrix")
    
    print("-" * 50)

    print("ADD TWO MATRICES")
    print("Note: Both matrices must be the same size.")
    mat_add_1 = get_matrix_input("First Matrix for Addition")
    
    rows = len(mat_add_1)
    cols = len(mat_add_1[0])
    print(f"\n--- Entering Second Matrix for Addition ({rows}x{cols}) ---")
    mat_add_2 = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                row_values = [int(x) for x in row_input.split()]
                if len(row_values) != cols:
                    print(f"Error: Expected {cols} values. Try again.")
                else:
                    mat_add_2.append(row_values)
                    break
            except ValueError:
                print("Invalid input.")
                
    summed_matrix = add_matrices(mat_add_1, mat_add_2)
    print_matrix(summed_matrix, "Result of Addition")

    print("-" * 50)

    print("MULTIPLY TWO MATRICES")
    print("Note: The number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
    mat_mult_1 = get_matrix_input("First Matrix for Multiplication")
    
    cols_1 = len(mat_mult_1[0])
    print(f"\n--- Entering Second Matrix for Multiplication ---")
    print(f"(Must have exactly {cols_1} rows)")
    
    while True:
        try:
            cols_2 = int(input("Enter number of columns for Second Matrix: "))
            if cols_2 > 0:
                break
        except ValueError:
            print("Invalid input.")
            
    mat_mult_2 = []
    for i in range(cols_1): 
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                row_values = [int(x) for x in row_input.split()]
                if len(row_values) != cols_2:
                    print(f"Error: Expected {cols_2} values. Try again.")
                else:
                    mat_mult_2.append(row_values)
                    break
            except ValueError:
                print("Invalid input.")
                
    multiplied_matrix = multiply_matrices(mat_mult_1, mat_mult_2)
    print_matrix(multiplied_matrix, "Result of Multiplication")
    print("=======================================")

if __name__ == "__main__":
    main()
