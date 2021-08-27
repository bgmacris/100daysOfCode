import random

abc = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['ñ']

def comprv_ignore(coord, pos_ignore, list_moves, ignore):
    if coord[0] == pos_ignore[0] and coord[1] == pos_ignore[1]:
        for move in list_moves:
            if move not in ignore:
                ignore.append(move)
    if pos_ignore[0] == None:
        if coord[1] == pos_ignore[1]:
            for move in list_moves:
                if move not in ignore:
                    ignore.append(move)
        if coord[1] == pos_ignore[1]:
            for move in list_moves:
                if move not in ignore:
                    ignore.append(move)
    if pos_ignore[1] == None:
        if coord[0] == pos_ignore[0]:
            for move in list_moves:
                if move not in ignore:
                    ignore.append(move)
        if coord[0] == pos_ignore[0]:
            for move in list_moves:
                if move not in ignore:
                    ignore.append(move)
    return ignore

def create_soup(lista_palabras):
        sopa = []
        for i in range(10):
            sopa.append([random.choice(abc) for i in range(10)])
        
        for palabra in lista_palabras:
            coord_palabras_finales = {}
            coord = [random.randint(0, 9) for i in range(2)]
            coord = [6, 6]
            print("COORDS: ", coord)
            movimientos = ['UP', 'DOWN', 'RIGHT', 'LEFT']
            ignore = []
            pos_ignore = {
                (0, 0): ['UP', 'LEFT'],
                (0, 1): ['UP', 'RIGHT'],
                (9, 0): ['DOWN', 'LEFT'],
                (9, 9): ['DOWN', 'RIGHT'],
                (None, 0): ['LEFT'],
                (None, 9): ['RIGHT'],
                (0, None): ['UP'],
                (9, None): ['DOWN']
            }
            
            for pos in pos_ignore:
                ignore = comprv_ignore(coord, pos, pos_ignore[pos], ignore)
            if coord[0] - len(palabra) < 0:
                if 'UP' not in ignore: ignore.append('UP')
            if coord[0] + len(palabra) > 9:
                if 'DOWN' not in ignore: ignore.append('DOWN')
            if coord[1] + len(palabra) > 9:
                if 'RIGHT' not in ignore: ignore.append('RIGHT')
            if coord[1] - len(palabra) < 0:
                if 'LEFT' not in ignore: ignore.append('LEFT')
            
            print("IGNORE", ignore)
            movimientos = [move for move in movimientos if move not in ignore]
            print("AAA",movimientos)
            choice_move = random.choice(movimientos)
            print(choice_move)
            for letter in palabra:
                if choice_move == 'UP':
                    sopa[coord[0]][coord[1]] = letter
                    coord[0] = coord[0] - 1
                if choice_move == 'DOWN':
                    sopa[coord[0]][coord[1]] = letter
                    coord[0] = coord[0] + 1
                if choice_move == 'LEFT':
                    sopa[coord[0]][coord[1]] = letter
                    coord[1] = coord[1] - 1
                if choice_move == 'RIGHT':
                    sopa[coord[0]][coord[1]] = letter
                    coord[1] = coord[1] + 1
            
            for i in sopa:
                print(i)
            
            break
                

lista_palabras = ['python', 'artificial', 'phone']
create_soup(lista_palabras)
