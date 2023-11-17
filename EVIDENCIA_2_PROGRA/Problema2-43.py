#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos,
#imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4) Definir dos objetos de la clase Alumno.
class alumno:
    def nombre_nota(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir (self):
        print ("nombre:",self.nombre)
        print ("nota:",self.nota)
        
    def mostrar_notas (self):
        if self.nota >=4: 
            print ("Es regular")
        else:
            print ("No es regular")
            
##bloque principal

alumno1=alumno()
alumno1.nombre_nota("Alondra",3)
alumno1.imprimir()
alumno1.mostrar_notas()

alumno2=alumno()
alumno2.nombre_nota("Paola",9)
alumno2.imprimir()
alumno2.mostrar_notas()