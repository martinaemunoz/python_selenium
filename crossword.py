def initializing_matrix(matrix, rows, columns): # para inicializar funcion en python debe estar lo más arriba posible, usando def y dos puntos
    for i in range(rows): # en js seria for (let i = 0; condicion de salida; i++)
        matrix.append([])
        for _ in range(columns):
            matrix[i].append("*")
    print("")

def add_word(entered_word, matrix, row):
    for i in range(len(entered_word)): # len returns the number of items in a container
        matrix[row][i] = entered_word[i]

def search_r(matrix, row, columns):
    r_found_at = columns
    for i in range(columns):
        if matrix[row][i].upper() == "R": # si la matriz de i es igual a r (upper es método Mayusculas)
            r_found_at = i
            break 
    return r_found_at

def adjusting_word(matrix, row, columns):
    row_content = ""
    i_word = 0

    r_found_at = search_r(matrix, row, columns)

    if r_found_at == columns:
        print("The word you entered does not contain the letter R ")
    else:
        for i in range(columns):
            row_content += matrix[row][i]

        for i in range(columns):
            if i >= 5 - r_found_at:
                matrix[row][i] = row_content[i_word]
                i_word += 1
            else:
                matrix[row][i] = "*"
            
def print_matrix(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end="")
        print("")

rows = int(input("Enter the number of words you want to display ")) # int es para pasar a num entero e input actua como leer en pseint
columns = int(input("Enter the maximum number of letters for each word "))
columns += 5 # margen de error para alineamiento de palabras

matrix = []
initializing_matrix(matrix, rows, columns)

for i in range(rows):
    entered_word = input(f"Enter word number {i + 1} ")
    add_word(entered_word, matrix, i)

for i in range(rows):
    adjusting_word(matrix, i, columns) 

print_matrix(matrix, rows, columns)