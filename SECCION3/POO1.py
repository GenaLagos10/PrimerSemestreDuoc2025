class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es de {self.edad} años")

    


persona1=Persona("Genaro", 39)
print(f"Nombre de la persona: {persona1.nombre}")
print(f"Edad de la persona: {persona1.edad}")
persona1.saludar()

