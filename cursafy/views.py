# -- coding: utf-8 --
import csv
import json
import sys

import numpy as np
from django.http import HttpResponse
from django.http import JsonResponse
import pandas as pd
from . import IA


def test(request):
    return HttpResponse("Hello, world.")


def queryParamTest(request):
    query = request.GET.get('query', '')
    return HttpResponse({query})


def paises(request):
    data = pd.read_csv("cursafy/usuarios.csv", delimiter=";", encoding="utf-8")
    data = data[["país_x"]]
    res = []
    for index, row in data.iterrows():
        if not (row["país_x"] in res):
            res.append(row["país_x"])

    response = []
    for i in res:
        response.append({"pais": i})

    return JsonResponse({"Paises": response})


def estados(request):
    data = pd.read_csv("cursafy/usuarios.csv", delimiter=";", encoding="utf-8")
    data = data[["estado"]]
    res = []
    for index, row in data.iterrows():
        if pd.isna(row["estado"]):
            if not ("Null" in res):
                res.append("Null")
        else:
            if not (row["estado"] in res):
                res.append(row["estado"])

    response = []
    for i in res:
        response.append({"estado": i})

    return JsonResponse({"Estados": response})


def competencias(request):
    realDB = []
    res = []
    with open("cursafy/cursos.csv", encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=";")
        for row in csvreader:
            realDB.append(row)
        for i in range(2, len(realDB[0])):
            res.append({"comp": realDB[0][i]})
    file.close()
    return JsonResponse({"Competencias": res})


def usuarios(request):
    pais = request.GET.get('pais', '')
    estados = request.GET.getlist('estados[]')
    competencias = request.GET.getlist('competencias[]')
    #estados = []
    #competencias = []
    #res_set = request.GET.copy()
    #print(res_set)
    #for item in res_set['estados[]']:
    #    estados.append(item)
    #for item in res_set['competencias[]']:
    #    competencias.append(item)
    realDB = []
    res = []
    with open("cursafy/cursos.csv", encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=";")
        for row in csvreader:
            realDB.append(row)
        for i in range(2, len(realDB[0])):
            res.append(realDB[0][i])
    file.close()

    compArray = []
    for i in res:
        temp = "0"
        for j in competencias:
            if j == i:
                temp = "1"
        compArray.append(temp)

    print(compArray)
    res = IA.gpt5(compArray, pais, estados)

    response = []
    for i in res:
        cursos = i[4].split(",")
        temp = []
        for j in cursos:
            temp.append({"curso": j})
        response.append({"nombre": i[0], "email": i[1], "telefono": i[2], "porcentaje": i[3], "cursos": temp})

    return JsonResponse({"usuarios": response})
