# This program displays a triangle pattern. 4-19
BASE_SIZE = 8

for r in range(BASE_SIZE):
    for c in range(r+1):
        print('*', end='')
    print()