matrix = [
          [7, "i", 3],
          ["T", "s", "i"],
          ["h", "%", "x"],
          ["i", " ", "#"],
          ["s", "M", " "],
          ["$", "a", " "],
          ["#", "t", "%"],
          ["^", "r", "!"]
          ]

matrix_list = list(matrix)


small_alpha = [" ","a", "b", "c", "d", "e", "f", "g", "h",
              "i", "j", "k", "l", "m", "n", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z"]


capital_alpha = [" ","A", "B", "C", "D", "E", "F", "G", "H",
                "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
i = 0
for i in range(len(matrix)):
    for each in range(27):
        if (matrix[i] in small_alpha[each]) or (each[i] in capital_alpha[each]):
            print(each[i])
    i += 1


print(matrix)