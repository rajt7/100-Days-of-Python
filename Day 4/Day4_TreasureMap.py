row1 = ["a", "b", "c"]
row2 = ["d", "e", "f"]
row3 = ["g", "h", "i"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1

map[row][column] = 'x'
print(f"{row1}\n{row2}\n{row3}")