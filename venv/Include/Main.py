#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import zeep
from zeep import helpers, xsd


class Estudiante(object):

    def __init__(self,matricula,nombre, carrera):
        self.carrera = carrera;
        self.matricula = matricula;
        self.nombre = nombre;


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)


wsdl = 'http://localhost:7000/ws/EstudianteWebServices?wsdl'
client = zeep.Client(wsdl=wsdl)

while True:
    print('Bievenido al Portal Estudiantil ')
    print('\n1) Listar todos los estudiantes\t\n2) Consultar Estudiantes\n3) Crear un nuevo Estudiante\n4)Borrar un estudiante.')
    opcion = int(input("◄◄◄◄◄◄◄ Ingrese el número de la opción deseada ►►►►►►►: "))

    if opcion == 1:
        print(client.service.getListaEstudiante())

    if opcion == 2:
        matricula = int(input('◄◄◄◄◄◄◄ Digite la matricula del estudiante ►►►►►►►: '))
        print(client.service.getEstudiante(matricula))

    if opcion == 3:
        matricula = int(input('◄◄◄◄◄◄◄ Digite la matricula ►►►►►►►: '))
        nombre = input('◄◄◄◄◄◄◄ Digite el nombre ►►►►►►►: ')
        carrera = input('◄◄◄◄◄◄◄ Digite la carreraa ►►►►►►►: ')

        va = Estudiante(matricula, nombre, carrera).toJSON()
        print("json: "+va+" desc: "+str(json.loads(va)))
        client.service.crearEstudiante(json.loads(va))
        #print(client.create_message(client.service,"crearEstudiante",json.loads(va)))
    if opcion == 4:
        matricula = int(input('◄◄◄◄◄◄◄ Digite la matricula ►►►►►►►: '))

        print("Estudiante eliminado: "+client.service.eliminandoEstudiante(matricula))
        #Esta funcion no esta implementada en el servidor