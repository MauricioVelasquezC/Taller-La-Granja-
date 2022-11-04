from Perro import Perro 
from Bovino import Bovino 
from Animal import Animal 

class Granja (Animal):
    
    def __init__(self):
        self.misPerros=[]
        self.misBovinos=[]
        
    def agregarPerro (self, peso, edad, raza, propietario, fecha_vacunacion):
        miPerro=Perro()
        
        miPerro.peso=peso
        miPerro.edad=edad
        miPerro.raza=raza
        miPerro.propietario=propietario
        miPerro.fecha_vacunacion=fecha_vacunacion
          
        self.misPerros.append(miPerro)  
    
    def agregarBovino (self, peso, edad, raza, propietario, fecha_vacunacion):
        miBovino=Bovino()
        
        miBovino.peso=peso
        miBovino.edad=edad
        miBovino.raza=raza
        miBovino.propietario=propietario
        miBovino.fecha_vacunacion=fecha_vacunacion
          
        self.misPerros.append(miBovino)   
    
    def obtenerPerro (self, indice):   
        return self.misPerros[indice]
    
    def obtenerBovino (self, indice):
        return self.misPerros[indice]    
         