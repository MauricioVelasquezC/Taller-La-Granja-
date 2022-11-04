class Animal:
    def __init__(self):
        self.peso=0
        self.edad=0
        self.raza=""
        
    def Correr (self):
        run=int(input("Ingrese la Edad"))
        if run >=5:
            print ("Rapido")
        elif run <5:
            print("Lento")
        
    def Emitir_sonido (self):
        pass
        
    def Bovino_pastar (self):
        establo=int(input("Ingrese el Establo"))
        if establo >5:
            print ("Pastar")
        elif establo <=5:
            print("No Pastar")
        
        
    def Obtener_Edad (self):        
        pass
        
    
            