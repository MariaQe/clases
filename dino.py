class Dino: #almacena funciones de un objeto caracteristico
    #cola, dientes, color, size
    def __init__(self,nombre):
        print ("Hola soy un dinosaurio, me llamo," nombre)

pepito = Dino("Pepe")

#Agregarle una propiedad color a la clase Dino, y que salude diciendo
# diciendo su nombre y de que color es el dinosaurio

class Dino:
    def __init__ (self,nombre, color): #es una funcion especial de dos _ guiones 
        print ("Hola soy un dinosaurio, me llamo", nombre, "soy de color",
         color)

pepito= Dino ("Pepe", "amarillo" ) 






