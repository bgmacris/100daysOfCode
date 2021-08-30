def backtracking(variables, rango_variables, optimo, profundidad):
    minn = rango_variables[profundidad][0]
    maxx = rango_variables[profundidad][1]
    for v in range(minn, maxx):
        print(es_completable(variables))
        variables[profundidad] = v
        
        if profundidad < len(variables)-1:
            if es_completable(variables):
                optimo = backtracking(variables[:], rango_variables, optimo, profundidad+1)
            else:
                sol = evalua_solucion(variables)
                if sol>evalua_solucion(optimo) and es_completable(variables):
                    optimo = (variables[0], variables[1])
        return optimo
    
def evalua_solucion(variables):
    x1 = variables[0]
    x2 = variables[1]
    val = (12 - 6)*x1 + (8 - 4)*x2
    return val

def es_completable(variables):
    x1 = variables[0]
    x2 = variables[1]
    val1 = 7*x1 + 4*x2
    val2 = 6*x1 + 5*x2
    if val1 <= 150 and val2 <= 160:
        return True
    else:
        return False
    
if __name__ == '__main__':
    variables = [0, 0]
    rango_variables = [(0, 51), (0, 76)]
    optimo = (0, 0)
    sol = backtracking(variables[:], rango_variables, optimo, 0)
    print(sol)
