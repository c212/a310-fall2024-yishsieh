def magic(size):
  matrix = []  #intialize a matrix
  for i in range(size):
    matrix.append([0] * size)

  # start point
    row = 0
    col = size // 2

  # fill up all the cells
  for k in range (1, size*size + 1):
    matrix[row][col] = k
    prev_row = row  # store the original position
    prev_col = col
    row -= 1 # move up
    col += 1 # move right

    if row < 0:  #if the row goes above the top row, go to the bottom row
      row = size -1

    if col == size: #if the col goes beyong the last col, go to the first col
      col = 0

    if matrix[row][col] != 0:
      row = prev_row
      col = prev_col
      row += 1
  return matrix

def show(m):
  for i in range(len(m)):
    for j in range(len(m)):
      print(("  " + str(m[i][j]))[-3:], end =' ')
    print()


# m = magic(3)
# show(m)

n = int(input("Enter size:"))
if n%2 == 1:
  show(magic(n))
else:
  print("The size should be an odd number.")