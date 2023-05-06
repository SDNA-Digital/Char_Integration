import psycopg2 as pg
import json

try:
    connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
    curs = connection.cursor()
    curs.execute('SELECT processonivelrisco as "Nivel de Risco", mes as "Mes", ano as "Ano", COUNT(*) AS "QtdeProcessos" FROM dash_processo GROUP BY processonivelrisco, mes, ano')
    # corrigin erro: data nao é um tipo de dado que pode ser armazenado em um JSON

    nivel_risco = {
    'MBA': 'Muito Baixo', 'BAI': 'Baixo', 'MOD': 'Moderado', 'ALT': 'Alto', 'MAL': 'Muito Alto'
}
    dic_date_mounth = {
        '01' : 'Janeiro',
        '02' : 'Fevereiro',
        '03' : 'Marco',
        '04' : 'Abril',
        '05' : 'Maio',
        '06' : 'Junho',
        '07' : 'Julho',
        '08' : 'Agosto',
        '09' : 'Setembro',
        '10' : 'Outubro',
        '11' : 'Novembro',
        '12' : 'Dezembro'
    }

    columns = [col[0] for col in curs.description]
    results = []
    for row in curs.fetchall():
        result_dict = {}
        for i, value in enumerate(row):
            if i == 0:
                result_dict[columns[i]] = nivel_risco[value]
            elif i == 1:
                result_dict[columns[i]] = dic_date_mounth
        results.append(result_dict)

    curs.close()
    connection.close()
    json_result = json.dumps(results, indent=4)
    with open('resultado.json', 'w') as arquivo:
        arquivo.write(json_result)
except Exception as e:
    print("Ocorreu um erro:", e)