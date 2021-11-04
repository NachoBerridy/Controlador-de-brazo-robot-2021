class errores:
    def __init__(self): 
        self.ref=int

    def imprimir(self, ref):
        if (ref==1): #Pertenece al error ZeroDivisionError
         print("No puede moverse/girar si la velocidad es 0")
        if (ref==2): #Pertenece al error NameError
            print("Nombre mal escrito")
        if (ref==3): #pertenece a TypeError
            print ("Error en tipo") ##ver bien que poner
        if (ref==4): #pertenece a valueError
            print("Angulo inválido")