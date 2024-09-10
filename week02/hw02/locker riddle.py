# locker riddle

# S1 - open 1~ 100
# S2 - close 2 4 6 8 ...
# S3 - open/close 3 6 9 12 ...
# ....
# S100 - open/close 100

# L1- 1 -open
# L2- 1 2 - closed
# L3- 1 3 - closed
# L6- 1 2 3 6 - closed
# L9- 1 3 9 - open
# L16 - 1 2 8 4 16 - open

lockers = [' '] * 100
#print(lockers)

for student in range(1,101): #start, stop
    for locker in range(student, 101, student):
        if lockers[locker-1] == ' ':
            lockers[locker-1] = 'o'
        else:
            lockers[locker-1] = ' '
    print(''.join(lockers))