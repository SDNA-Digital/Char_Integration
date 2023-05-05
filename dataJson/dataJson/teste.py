from django.http import JsonResponse
import psycopg2 as pg
import json

try:
    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute('SELECT processonivelrisco as "Nivel de Risco", processodata as "data", COUNT(*) AS "QtdeProcessos" FROM dash_processo GROUP BY processonivelrisco, processodata')
    # corrigin erro: data nao é um tipo de dado que pode ser armazenado em um JSON
    nivel_risco = {
    'MBA': 'Muito Baixo',
    'BAI': 'Baixo',
    'MOD': 'Moderado',
    'ALT': 'Alto',
    'MAL': 'Muito Alto'
}
    columns = [col[0] for col in curs.description]
    results = []
    for row in curs.fetchall():
        result_dict = {}
        for i, value in enumerate(row):
            if i == 0:
                result_dict[columns[i]] = nivel_risco[value]
            elif i == 1:
                result_dict[columns[i]] = value
        results.append(result_dict)

    curs.close()
    connection.close()
    json_result = json.dumps(results, indent=4)
    with open('resultado.json', 'w') as arquivo:
        arquivo.write(json_result)
except Exception as e:
    print("Ocorreu um erro:", e)