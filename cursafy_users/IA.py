import random


def getSolutionDifference(user, solution):  # simple usuario, solución que se requiere
    similarity = 0
    temp = []
    for i in range(0, len(user)):
        if type(user[i]) == bool:
            temp.append(user[i])
    for i in range(0, len(temp)):
        if solution[i] and temp[i]:
            similarity += 1
    difference = len(solution) - similarity

    return [user[0], difference]


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def getRandomUsers(DB):
    DB2 = []
    random.shuffle(DB)
    usuariosPorVecindad = 5
    iteraciones = round(len(DB) / usuariosPorVecindad)

    temp = list(split(DB, iteraciones))
    for i in range(len(temp)):
        DB2.append(random.sample(temp[i], 1)[0])

    return DB2


def gpt5(DB, solution):
    temp = []
    DB2 = getRandomUsers(DB)
    for i in range(0, len(DB2)):
        temp.append(getSolutionDifference(DB2[i], solution))

    temp.sort(key=lambda x: x[1])
    return temp

def test():
    DB = [
        ['Alex', True, False, True, False, True, True, False],
        ['Maria', False, True, True, True, False, False, False],
        ['Juan', True, False, False, False, True, True, True],
        ['Laura', False, True, False, True, True, False, False],
        ['Pedro', True, True, False, True, False, False, True],
        ['Ana', False, False, True, True, True, True, False],
        ['Carlos', True, False, True, False, False, True, True],
        ['Sofia', False, True, False, True, True, False, True],
        ['Luis', True, False, False, False, True, True, False],
        ['Elena', False, True, True, False, False, False, True],
        ['Miguel', True, True, False, True, True, False, True],
        ['Lucia', False, False, True, False, True, True, False],
        ['Andres', True, False, True, True, False, False, True],
        ['Raquel', False, True, True, True, False, False, True],
        ['Jorge', True, False, False, False, True, True, False],
        ['Clara', False, True, False, True, True, False, False],
        ['Fernando', True, True, False, True, False, True, True],
        ['Isabel', False, False, True, True, True, False, False],
        ['Roberto', True, True, True, False, False, True, False],
        ['Paula', False, False, False, True, True, True, True],
        ['Antonio', True, False, True, False, True, False, False],
        ['Beatriz', False, True, False, True, True, True, False],
        ['Diego', True, True, True, False, False, False, True],
        ['Eva', False, False, True, True, True, False, True],
        ['Francisco', True, True, False, False, True, True, False],
        ['Gloria', False, True, True, False, True, True, True],
        ['Hector', True, False, True, False, False, False, True],
        ['Irene', False, True, False, True, True, False, False],
        ['Javier', True, True, True, False, True, True, False],
        ['Karla', False, False, True, True, False, True, True],
        ['Leonardo', True, False, False, False, True, False, True],
        ['Marta', False, True, True, True, False, False, True],
        ['Nicolas', True, False, True, True, True, True, False],
        ['Olga', False, True, False, False, True, True, True],
        ['Pablo', True, False, True, True, False, False, False],
        ['Queralt', False, True, True, False, True, True, False],
        ['Ramon', True, False, True, True, True, False, True],
        ['Sara', False, True, False, True, False, True, False],
        ['Tomás', True, False, True, True, False, False, True],
        ['Uxue', False, True, True, True, True, True, False],
        ['Victor', True, False, False, False, True, False, True],
        ['Wendy', False, True, False, True, True, False, True],
        ['Ximena', True, False, True, False, True, True, False],
        ['Yolanda', False, True, False, False, True, False, False],
        ['Zoe', True, False, True, True, True, True, True],
        ['Adrian', False, True, False, True, False, True, True],
        ['Belén', True, False, True, False, True, False, False],
        ['Cesar', False, True, True, True, False, True, True],
        ['Daniela', True, False, False, False, True, True, False],
        ['Esteban', False, True, False, True, False, True, False],
    ]
    competenciasABuscar = [True, True, False, False, True, True, True]
    print(gpt5(DB, competenciasABuscar))