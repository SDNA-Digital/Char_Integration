from django.http import JsonResponse, HttpResponse
import json
import psycopg2 as pg


def Dash_IncidenteArea(request):

    connection = pg.connect(user="postgres", password="0832", host="localhost", port="5432", database="Eagle")
    curs = connection.cursor()
    curs.execute('SELECT areaid as "AreaID", areanome as "Area", COUNT(*) as "QtdeIncidentes" FROM dash_incidentes GROUP BY areaid, areanome')

    columns = [col[0] for col in curs.description]
    results = []
    for row in curs.fetchall():
        result_dict = {}
        for i, value in enumerate(row):
            if i == 1:
                value = value.strip()

            result_dict[columns[i]] = value
        results.append(result_dict)

    curs.close
    connection.close

    return JsonResponse(results, safe=False)


def Dash_Politicas_Manuais(request):
    
    connection = pg.connect(user="postgres", password="0832", host="localhost", port="5432", database="Eagle")
    curs = connection.cursor()
    curs.execute('select * from dash_politicas_manuais')
    
    result = curs.fetchall()

    ArrayDic = []
    
    columns = [col[0] for col in curs.description]

    for tuple in result:
        result_dict ={}
        for i, tupleItem in enumerate(tuple):
            if i == 1:
                tupleItem = tupleItem.strip()
                
            result_dict[columns[i]] = tupleItem
        ArrayDic.append(result_dict)
    
    print(result)

    curs.close
    connection.close
    
    return JsonResponse(ArrayDic, safe=False)

def Dash_Norma (request):

    connection = pg.connect(user="postgres", password="0832", host="localhost", port="5432", database="Eagle")
    curs = connection.cursor()

    curs.execute('select count(*) as qtdnorma from norma ')

    result = curs.fetchall()
    qtdnormas ={'Qtdnormas':result[0][0]}
    ArrayDic = []
    ArrayDic.append(qtdnormas)

    curs.execute('select * from Radar_regulatorio ')

    result = curs.fetchall()

    columns = [col[0] for col in curs.description]

    for tuple in result:
        result_dict ={}
        for i, tupleItem in enumerate(tuple):
            if i == 1:
                tupleItem = tupleItem.strip()
                   
            result_dict[columns[i]] = tupleItem
        ArrayDic.append(result_dict)
    print(ArrayDic)

    curs.close
    connection.close
    
    return JsonResponse(ArrayDic, safe=False)

def Dash_RadarConformidade (request):
    connection = pg.connect(user="postgres", password="0832", host="localhost", port="5432", database="Eagle")
    curs = connection.cursor()

    ArrayDic = []

    curs.execute('select * from Radar_conformidade')

    result = curs.fetchall()

    columns = [col[0] for col in curs.description]

    for tuple in result:
        result_dict ={}
        for i, tupleItem in enumerate(tuple):
            if i == 1:
                tupleItem = tupleItem.strip()
                   
            result_dict[columns[i]] = tupleItem
        ArrayDic.append(result_dict)
    print(ArrayDic)

    curs.close
    connection.close
    
    return JsonResponse(ArrayDic, safe=False)