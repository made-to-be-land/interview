result = []
matrix = []
word: str = ""


def find_character(char_i, y, x):
    global result
    result.append('[' + str(y) + ',' + str(x) + ']')

    if char_i >= len(word) or len(result) == len(word):
        return
    if y != 0 and matrix[y - 1][x] == word[char_i]:
        find_character(char_i + 1, y - 1, x)
    if y != len(matrix) - 1 and matrix[y + 1][x] == word[char_i]:
        find_character(char_i + 1, y + 1, x)
    if x != 0 and matrix[y][x - 1] == word[char_i]:
        find_character(char_i + 1, y, x - 1)
    if x != len(matrix) - 1 and matrix[y][x + 1] == word[char_i]:
        find_character(char_i + 1, y, x + 1)
    if len(result) != len(word):
        result.pop()
    return


def crossword(a_matrix, a_word):
    global matrix, word

    if len(a_matrix) < len(word):
        print("word is too long or str for matrix is too short")
        return
    if type(a_matrix) != str or type(word) != str:
        return

    word = a_word.upper()
    str_matrix = a_matrix.upper()

    str_matrix = list(str_matrix)
    num_matrix = len(str_matrix)

    sqrt_num_matrix = num_matrix ** (0.5)
    if sqrt_num_matrix.is_integer() == 1:
        matrix = [(str_matrix[i:i + int(sqrt_num_matrix)]) for i in range(0, len(str_matrix), int(sqrt_num_matrix))]
        for level in matrix:
            print(level, "\n")
    else:
        print("the matrix couldn't create, try to send another string")

    lword = list(word)
    coord = ()
    for i in lword:
        for j in matrix:
            if i in j and lword[0] == i:
                coord = (1, matrix.index(j), j.index(i))

    char_i, y, x = coord
    find_character(char_i, y, x)


if __name__ == '__main__':
    crossword(input("string of chars for matrix \n"), input("word for search in a matrix \n"))
    print(result)
