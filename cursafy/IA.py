import random
import pandas as pd
import csv


def getSolutionDifference(user, solution):
    similarity = 0
    temp = []
    userComp = user[5:]
    for i in range(0, len(userComp)):
        if type(userComp[i]) == bool:
            temp.append(userComp[i])
    for i in range(0, len(temp)):
        if solution[i]:
            if temp[i]:
                similarity += 1
        else:
            similarity += 1
    percentage = round(similarity / len(solution) * 100, 2)

    return [user[0], user[1], user[2], percentage]


def rewriteArray(array):
    temp = []
    for i in range(len(array)):
        if array[i] == "1":
            temp.append(True)
        elif array[i] == "0":
            temp.append(False)
        else:
            temp.append(array[i])
    return temp


def openFile(database, pais, estados):
    realDB = []
    with open(database, encoding='ISO-8859-1') as file:
        csvreader = csv.reader(file, delimiter=";")
        for row in csvreader:
            if pais == "Mexico":
                if row[4] in estados:
                    realDB.append(row)
            else:
                if row[3] == pais:
                    realDB.append(row)
    file.close()
    return realDB

def openSingleFile(database):
    realDB = []
    with open(database, encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=";")
        for row in csvreader:
            realDB.append(row)
    file.close()
    return realDB

def poblacion_inicial(database, pais, estados):
    realDB = openFile(database, pais, estados)
    result = []
    index = []
    for i in range(0, 15):
        randomNum = random.randint(0, len(realDB) - 1)
        index.append(randomNum)
        result.append(rewriteArray(realDB[randomNum]))

    return result, index

def buscarCursos(user):
    dbCursos = openSingleFile("cursafy/usuarios.csv")
    temp = ""
    for i in range(len(dbCursos)):
        if dbCursos[i][1] == user[0]:
            temp = dbCursos[i][5]
    if temp == "":
        temp = "Cursos no encontrados"
    return temp

def gpt5(solucion, pais, estados):
    database = "cursafy/competencias.csv"
    p_inicial, index = poblacion_inicial(database, pais, estados)
    dbUsers = openFile(database, pais, estados)
    rewriteSolution = rewriteArray(solucion)
    mejor = []
    for i in range(len(p_inicial)):
        iteracion = 0
        result = []
        while iteracion < 50:
            if index[i] - 15 > 0 and index[i] + 15 < len(dbUsers):
                result.append(getSolutionDifference(rewriteArray(dbUsers[random.randint(index[i] - 15, index[i] + 15)]),
                                                    rewriteSolution))
            elif index[i] - 15 < 0 and not (index[i] + 15 > len(dbUsers)):
                result.append(
                    getSolutionDifference(rewriteArray(dbUsers[random.randint(0, index[i] + 15)]), rewriteSolution))
            elif index[i] + 15 > len(dbUsers) and not (index[i] - 15 < 0):
                result.append(
                    getSolutionDifference(rewriteArray(dbUsers[random.randint(index[i] - 15, len(dbUsers) - 1)]),
                                          rewriteSolution))
            else:
                result.append(
                    getSolutionDifference(rewriteArray(dbUsers[random.randint(0, len(dbUsers) - 1)]), rewriteSolution))

            iteracion += 1

        result.sort(key=lambda x: -x[len(result) - 1])
        mejor.append(result[0])

    mejor.sort(key=lambda x: -x[len(mejor) - 1])
    mejor = [i for n, i in enumerate(mejor) if i not in mejor[:n]]

    respuestaFinal = []
    for user in mejor:
        temp = buscarCursos(user)
        if not temp == "Cursos no encontrados":
            user.append(temp)
            respuestaFinal.append(user)


    return respuestaFinal


#if __name__ == '__main__':
#    competenciasReales = [
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE",
#    "TRUE", "TRUE", "TRUE", "TRUE"
#    ]

#    respuestas = gpt5(competenciasReales, "Mexico", ["CHIH", "CDMX"])
#    for respuesta in respuestas:
#        print(respuesta)