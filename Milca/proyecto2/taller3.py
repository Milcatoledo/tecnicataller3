import json


def publicaciones():
    profesores = []
    publicaciones = open('publicacion.json', 'r')
    datos = json.load(publicaciones)
    print('---------------------------------------- INFORMACION DOCENTES ------------------------------------------')
    for i in datos:
        cedula = i['cedula']
        apellidos = i['apellidos']
        if not (profesores.__contains__(i['cedula'])):
            profesores.append({'cedula': cedula, 'apellidos': apellidos})
    newprofesor = []
    for i in profesores:
        cedula = i['cedula']

        publicaciones = 0
        for m in datos:
            if cedula == m['cedula']:
                publicaciones = +1
        newprofesor.append({'cedula': cedula, 'apellidos': i['apellidos'], 'publicaciones': publicaciones})
    for i in newprofesor:
        print(f" - El/La docente {i['apellidos']} con su C.I: {i['cedula']} tiene: {i['publicaciones']} articulos")
    print('------------------------------------------------------------------------------------------------------')

if __name__ == "__main__":
    publicaciones()