from django.http import JsonResponse, HttpResponse
import json
import psycopg2 as pg

connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
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
