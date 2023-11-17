class Persona:
    
    def inicializar(self,nom):
        self.nombre=nom
        
    def imprimir (self):
        print ("Nombre", self.nombre)
    
    
#bloque principal

persona1=Persona()
persona1.inicializar("Sharon")
persona1. imprimir()

persona2=Persona()
persona2.inicializar("Dayanna")
persona2. imprimir()