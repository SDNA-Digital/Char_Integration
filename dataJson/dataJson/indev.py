from django.http import JsonResponse, HttpResponse
import json
import psycopg2 as pg

connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
curs = connection.cursor()
curs.execute('select count(*) as qtdnorma from norma ')
