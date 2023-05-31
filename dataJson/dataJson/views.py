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
    
    curs.close
    connection.close
    
    return JsonResponse(ArrayDic, safe=False)

def Dash_Norma (request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()

    ArrayDic = []
    
    curs.execute('select * from Radar_regulatorio')

    result = curs.fetchall()

    columns = [col[0] for col in curs.description]

    for tuple in result:
        result_dict ={}
        for i, tupleItem in enumerate(tuple):
            if i == 1:
                tupleItem = tupleItem.strip()
                   
            result_dict[columns[i]] = tupleItem
        ArrayDic.append(result_dict)

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
        '1': 'Janeiro',
        '2': 'Fevereiro',
        '3': 'Marco',
        '4': 'Abril',
        '5': 'Maio',
        '6': 'Junho',
        '7': 'Julho',
        '8': 'Agosto',
        '9': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }

    results = []
    for row in curs.fetchall():
        result_dict = {}
        result_dict['Mes'] = dic_date_mounth[str(row[1])]
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
        
def Card_Processos(request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute('SELECT qtde_processos as "Processos_mapeados" FROM card_processos GROUP BY qtde_processos')

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

def Dash_ProcessoxArea(request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute('SELECT processonivelrisco as "Nivel de Risco", areaid as "Area" , COUNT(*) AS "QtdeProcessos" FROM dash_processo GROUP BY processonivelrisco, "Area" ORDER BY "Area", "Nivel de Risco"')

    dic_nivel_risco = {
        'MBA': 'Muito Baixo', 
        'BAI': 'Baixo', 
        'MOD': 'Moderado', 
        'ALT': 'Alto', 
        'MAL': 'Muito Alto'
    }

    results = []
    for row in curs.fetchall():
        result_dict = {}
        areaid = result_dict['Area'] = row[1]
        result_dict['Nivel de Risco'] = dic_nivel_risco[row[0]]
        result_dict['QtdeProcessos'] = row[2]
        results.append(result_dict)
    
    curs.close()
    connection.close()

    results_grouped = {}
    for result in results:
        areaid = result['Area']
        if areaid not in results_grouped:
            results_grouped[areaid] = {}
        dic_nivel_risco = result['Nivel de Risco']
        if dic_nivel_risco not in results_grouped[areaid]:
            results_grouped[areaid][dic_nivel_risco] = 0
        results_grouped[areaid][dic_nivel_risco] += result['QtdeProcessos']

    final_results = []
    for areaid, data in results_grouped.items():
            data['Area'] = areaid
            final_results.append(data)
    
    return JsonResponse(final_results, safe=False)

def Dash_PlanosMitigantes(request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute('SELECT tarefastatustarefa as "status", mes as "mes_criacao", tarefaprevtermino as "prevtermino" , COUNT(*) AS "QtdeTarefas" FROM dash_tarefa GROUP BY tarefastatustarefa, "mes_criacao", tarefaprevtermino ORDER BY "mes_criacao", "status", "prevtermino"')

    dic_status_tarefa = {
        '1': 'Nao iniciado', 
        '2': 'Em andamento', 
        '3': 'Em aprovacao', 
        '4': 'Concluido', 
        '5': 'Cancelado'
    }

    dic_date_mounth = {
        '1': 'Janeiro',
        '2': 'Fevereiro',
        '3': 'Marco',
        '4': 'Abril',
        '5': 'Maio',
        '6': 'Junho',
        '7': 'Julho',
        '8': 'Agosto',
        '9': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }

    results = []
    for row in curs.fetchall():
        result_dict = {}
        result_dict['mes_criacao'] = dic_date_mounth[str(row[1])]
        result_dict['status'] = dic_status_tarefa[str(row[0])]
        result_dict['QtdeProcessos'] = row[3]
        results.append(result_dict)

    curs.close()
    connection.close()

    results_grouped = {}
    for result in results:
        mes = result['mes_criacao']
        if mes not in results_grouped:
            results_grouped[mes] = {}
        dic_status_tarefa = result['status']
        if dic_status_tarefa not in results_grouped[mes]:
            results_grouped[mes][dic_status_tarefa] = 0
        results_grouped[mes][dic_status_tarefa] += result['QtdeProcessos']

    final_results = []
    for mes, data in results_grouped.items():
        data['mes_criacao'] = mes
        final_results.append(data)
    return JsonResponse(final_results, safe=False)

def Tabela_Tarefas(request):

    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute ('SELECT tarefaid AS "ID", tarefatitulo AS "Plano", usuario_areaid AS "Area", tarefastatustarefa AS "Status", tarefaprevtermino AS "Prazo" FROM table_tarefa GROUP BY "ID", "Plano", "Area", "Status", "Prazo" ORDER BY "ID", "Plano", "Area", "Status", "Prazo"')

    dic_status_tarefa = {
        '1': 'Nao iniciado', 
        '2': 'Em andamento', 
        '3': 'Em aprovacao', 
        '4': 'Concluido', 
        '5': 'Cancelado'
    }
    dic_area_tarefa = {
        '1': 'Juridico', 
        '2': 'Operacional', 
        '3': 'Financeiro', 
        '4': 'RH', 
        '5': 'Comercial',
        '6': 'Administrativo'
    }

    results = []
    for row in curs.fetchall():
        result_dict = {}
        result_dict['ID'] = row[0]
        result_dict['Plano'] = row[1]
        result_dict['Area'] = dic_area_tarefa[str(row[2])]
        result_dict['Status'] = dic_status_tarefa[str(row[3])]
        result_dict['Prazo'] = row[4]
        results.append(result_dict)

    curs.close()
    connection.close()

    return JsonResponse(results, safe=False)

#def Matriz_Probabilidade_Impacto(request):
    
    connection = pg.connect(user="postgres", password="0832", host="localhost", port="5432", database="Eagle")
    curs = connection.cursor()
    curs.execute ('SELECT processoid AS "ID", probabilidade AS "Probabilidade", impacto AS "Impacto" FROM matriz_probabilidade_impacto GROUP BY "ID", "Probabilidade", "Impacto" ORDER BY "ID", "Probabilidade", "Impacto"')

    dic_probabilidade = {
        'quase certo': 'Quase certo',
        'provavel': 'Provavel',
        'pouco provavel': 'Pouco provavel',
        'possivel': 'Possivel',
        'rara': 'Rara'
    }

    dic_impacto = {
        'desprezivel': 'Desprezivel',
        'marginal': 'Marginal',
        'media': 'Media',
        'critica': 'Critica',
        'extrema': 'Extrema'
    }

    results = []
    for row in curs.fetchall():
        result_dict = {}
        result_dict['ID'] = row[0]
        result_dict['Probabilidade'] = dic_probabilidade[row[1]]
        result_dict['Impacto'] = dic_impacto[row[2]]
        results.append(result_dict)

    curs.close()
    connection.close()

    return JsonResponse(results, safe=False)


# teste local do arquivo JSON>>>>>>>    json_result = json.dumps(final_results, indent=4)
#                                       with open('resultado.json', 'w') as arquivo:
#                                       arquivo.write(json_result)