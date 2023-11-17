##Confeccionar una clase que represente un empleado.
##Definir como atributos su nombre y su sueldo. En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y
##por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
  
class empleado:
    def __init__ (self):
        self.nombre=input ("Ingrese su nombre: ")
        self.sueldo=float(input("Ingrese su sueldo: "))

    def imprimir (self):
        print ("Nombre", self.nombre)
        print ("Sueldo", self.sueldo)
        
    def impuestos (self):
        if self.sueldo >3000:
            print ("Debe pagar impuestos")
        else:
            print ("No paga impuestos")
                
##Bloque principal

empleado1=empleado()
empleado1.imprimir()
empleado1.impuestos()

empleado2=empleado()
empleado2.imprimir()
empleado2.impuestos()