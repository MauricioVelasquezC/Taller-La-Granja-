from Animal import Animal 

class Perro(Animal):
    
    def __init__(self):
        self.propietario=""
        self.fecha_vacunacion=""
    
    def Emitir_sonido (self):
        soun=int(input("Ingrese la Edad"))
        if soun <3:
            print ("Auf Auf")
        elif soun >=3:
            print("Guau Guau")
    