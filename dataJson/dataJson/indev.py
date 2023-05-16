from django.http import JsonResponse, HttpResponse
import json
import psycopg2 as pg

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
    result_dict['Status'] = dic_status_tarefa[str(row[3])]
    result_dict['ID'] = row[0]
    result_dict['Plano'] = row[1]
    result_dict['Area'] = dic_area_tarefa[str(row[3])]
    result_dict['Prazo'] = row[4]
    results.append(result_dict)

curs.close()
connection.close()