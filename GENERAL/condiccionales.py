print("PROGRAMA DE NOTAS DE ALUMNOS")

nota_alumno=input("Introduce la nota del alumno: ")


def evaluacion(nota):
    valoracion="aprobado"
    if nota<4:
        valoracion="suspendido"

    return valoracion


print(evaluacion(int(nota_alumno)))