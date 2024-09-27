# translate a number into the closest letter grade
# A+  4
# A   4
# A-  3.7 (>3.85, A)
# B+  3.3 (>3.5, A-)
# B   3   (>3.15, B+)
# B-  2.7 (>2.85, B)
# C+  2.3 (>2.5, B-)
# C   2   (>2.15, C+)
# C-  1.7 (>1.85, C)
# D+  1.3 (>1.5, C-)
# D   1   (>1.15, D+)
# D-  0.7 (>0.85, D)
# F   0   (>0.35, D-)

def letter_converter(grade):
  if grade > 4:
    return "Grades should not exceed 4."
  elif grade == 4:
    return "A+"
  elif grade >= 3.85:
    return "A"
  #.... please finish the rest of them
  elif grade > 0.35:
    return "D-"
  elif grade == 0:
    return "F"
  else:
    return "Grades should be greater than 0."


g = letter_converter(4)
print(g)