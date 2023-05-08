from django.http import JsonResponse, HttpResponse
import json
import psycopg2 as pg


def Dash_IncidenteArea(request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
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
    
    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
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

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
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
    
    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
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

def Dash_Processo (request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute('SELECT processonivelrisco as "Nivel de Risco", mes as "Mes" , COUNT(*) AS "QtdeProcessos" FROM dash_processo GROUP BY processonivelrisco, "Mes" ORDER BY "Mes", "Nivel de Risco"')

    dic_nivel_risco = {
        'MBA': 'Muito Baixo', 
        'BAI': 'Baixo', 
        'MOD': 'Moderado', 
        'ALT': 'Alto', 
        'MAL': 'Muito Alto'
    }
    
    dic_date_mounth = {
        '01': 'Janeiro',
        '02': 'Fevereiro',
        '03': 'Marco',
        '04': 'Abril',
        '05': 'Maio',
        '06': 'Junho',
        '07': 'Julho',
        '08': 'Agosto',
        '09': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }

    results = []
    for row in curs.fetchall():
        result_dict = {}
        result_dict['Mes'] = dic_date_mounth[row[1]]
        result_dict['Nível de Risco'] = dic_nivel_risco[row[0]]
        result_dict['QtdeProcessos'] = row[2]
        results.append(result_dict)

    curs.close()
    connection.close()
    
    results_grouped = {}
    for result in results:
        mes = result['Mes']
        if mes not in results_grouped:
            results_grouped[mes] = {}
        dic_nivel_risco = result['Nível de Risco']
        if dic_nivel_risco not in results_grouped[mes]:
            results_grouped[mes][dic_nivel_risco] = 0
        results_grouped[mes][dic_nivel_risco] += result['QtdeProcessos']
    
    final_results = []
    for mes, data in results_grouped.items():
        data['Mes'] = mes
        final_results.append(data)

        return JsonResponse(final_results, safe=False)