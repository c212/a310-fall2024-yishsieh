# scalable  Z

size = 9
for row in range(size):
  for col in range(size):
    if row == 0 or row == size-1 or row + col == size -1:
      print("*", end =' ')
    else:
      print(" ", end=' ')
  print()


# scalable  Q
for row in range(size):
  for col in range(size):
    if (row == 0 or row == size-2) and (col>0 and col< size-1) :
      print("*", end=' ')
    elif (col ==0 or col == size-1) and (row >0 and row <size-2):
      print("*", end=' ')
    elif row == col and row>size//2 -1 :
      print("*", end=' ')
    else:
      print(" ", end=' ')
  print()