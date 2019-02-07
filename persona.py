#Crear una carpeta que se llame clases y adentro poner los archivos
# dino.py persona.py

#Crear una clase Persona() en el archivo persona.py que tenga como 
#atributos nombre edad y profesion
#Al instanciar la clase tiene que saludar igual que el dino diciendo sus 
#atributos

class Persona:
    def __init__ (self, un_nombre="",una_edad= 0,una_profesion=""): #aqui se carga una edad vacia en 
#numero para ir asignando
        self.nombre= un_nombre
        self.edad= una_edad
        self.profesion= una_profesion
        print("Hola me llamo",self.nombre,"tengo", self.edad, "y soy", self.profesion)
    
    def cumpleanhos (self):
        self.edad= self.edad +1 #este metodo suma 1 a la edad cada vez que se le llama
        return self.edad 

humano= Persona ("Maria", 33, "profesor")
print (humano.cumpleanhos())
print(humano.cumpleanhos())

print(humano.nombre)
print(humano.edad)
print(humano.profesion)

#Agregar un metodo a la clase persona que se llame cumpleanhos y que aumente la edad de la persona
# en un anho y retorne la edad nuevA

