from Animal import Animal 

class Bovino(Animal):
    
    def __init__(self):
        self.propietario=""
        self.fecha_vacunacion=""
        self.establo=0
        
    def Pastar(self):   
        pass
        
    def Emitir_sonido (self):
        print ("Muuuu")   