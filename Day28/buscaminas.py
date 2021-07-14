import random


def mapa():
    map = []
    for i in range(9):
        map.append(['U' for i in range(9)])
    return map


def put_mine(map):
    for i in range(9):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if map[row][column] != 'X':
            print(row, column)
            map[row][column] = 'X'

def index_mine(map):
    copy_map = map[:]
    index_mines = []
    for row in copy_map:
        index_column = []
        for ind in row:
            if ind == 'X':
                index_mines.append(row.index(ind))
                #print(copy_map[row], row.index(ind), row[row.index(ind)])
                copy_map[copy_map.index(row)].remove(ind)
        if index_column:
            for i in index_column:
                index_mines.append((copy_map.index(row), i))
    print(index_mines)


def num_next_to(map):
    index_mines = []
    for rows in map:
        index_mine = [rows.index(i) for i in rows]
        print("X", index_mine)



map = mapa()
put_mine(map)
index_mine(map)
for i in map:
    print(i)
