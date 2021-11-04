from math import*
from Robot import *
from time import *
from errores import errores
from gcode import *
class Comandos:
    def __init__(self):
    
        self.conexion=False
        self.activacion=False
        self.robot1=Robot()
        self.aprendizaje=[]
        self.c=0
        self.tiempo=0
        self.tinicial=0
        self.detalle = []
        self.error= errores()
        self.codigo= gcode()
    
    #1
    def conectar(self,i): #hay que ponerle que le pasamos i
        if (self.conexion==True):
            self.conexion=False
            self.activacion=False
            self.tiempo =   time() - self.tinicial
            self.detalle.append([i,'Desconectar',ctime()])
        else:
            
            self.conexion=True
            self.tinicial = time()
            self.detalle.append([i,'Conectar',ctime()])
        return self.conexion

    #2    
    def activar(self,i):
        if(self.conexion==True):
            if(self.activacion==True):
                self.activacion =False
                self.detalle.append([i,'Apagar',ctime()])
            else:
                self.activacion =True
                self.detalle.append([i,'Encender',ctime()])
            return self.activacion
        else:
            return 2
   
         
    #3 #4 #5
    def girar(self,i,ang,vel):
        
        if(self.activacion==True):
            try:
                t=(ang*(pi/180))/vel 
                print (t)
            except ZeroDivisionError:
                self.error.ref=1
                self.error.imprimir(self.error.ref)  
                return 'Error1'
            tpo=ctime()
            sleep(abs(t))
            self.error.ref=4
            if(i==3):
                if (-180<(self.robot1.articulacion1.angulo+ang)<180):
 
                    #raise ValueError (self.error.imprimir(self.error.ref)) 
                    self.robot1.articulacion1.girarA(ang)
                    self.codigo.leergcode("Girar articulacion 1")
                    self.detalle.append([i,ang,vel, t, tpo])
                else:
                    return "Error2"

            elif(i==4):
                if (abs((self.robot1.articulacion2.angulo+ang))>90):# or self.robot1.verificar_z(2)<0):
                    return "Error2"
                else:
                    self.robot1.articulacion2.girarA(ang)
                    self.robot1.set_Z()
                    self.codigo.leergcode("Girar articulacion 2")
                    self.detalle.append([i,ang,vel, t, tpo])

            elif(i==5): 
                if (abs(self.robot1.articulacion3.angulo+ang)>80):# or self.robot1.verificar_z(3)<0):
                    return "Error2"
                else:
                    self.robot1.articulacion3.girarA(ang)
                    self.robot1.set_Z()
                    self.detalle.append([i,ang,vel, t, tpo])
                    self.codigo.leergcode("Girar articulacion 3")
            return (self.robot1.articulacion1.angulo,self.robot1.articulacion2.angulo,self.robot1.articulacion3.angulo)
        else:
            return self.activacion 
           

    #6
    def accionar_efector(self,i): 
        tpo= ctime()
        sleep(0.5)
        if(self.activacion==True):
            self.codigo.leergcode("Accionar efector")
            if (self.robot1.efector==False):
                self.robot1.efector=True
                self.detalle.append([i,"Abrir efector", 0.5, tpo])
            elif(self.robot1.efector==True):
                self.robot1.efector=False 
                self.detalle.append([i,"Cerrar efector", 0.5, tpo])
            return self.robot1.efector
        else:
            return 2
     #7  
    def mover(self,i,x,y,vel):#probar si funciona
        if (self.activacion==True):
            self.error.ref=1 ##Para indicar el tipo de referencia
            try:
                tpo=ctime()
                t=((x-self.robot1.x)+(y-self.robot1.y))/vel
                sleep(abs(t))
                self.robot1.x=x
                self.robot1.y=y
                self.detalle.append([i,"Mover",self.robot1.x,self.robot1.y,vel, t, tpo])
                self.codigo.leergcode("Mover efector")
                return (self.robot1.x,self.robot1.y)
            except ZeroDivisionError:
                self.error.imprimir(self.error.ref)  
                return "Operacion erronea"
        else:
            return self.activacion

    #8
    def retorno_origen(self,i):
        if(self.activacion==True):
            tpo= ctime()
            sleep(1)
            self.robot1.articulacion1.origen()
            self.robot1.articulacion2.origen()
            self.robot1.articulacion3.origen()
            self.robot1.x=0
            self.robot1.y=0
            self.detalle.append([i,"Retorno origen", 1, tpo])
            return[(self.robot1.articulacion1.angulo,self.robot1.articulacion1.angulo,self.robot1.articulacion1.angulo),(self.robot1.x,self.robot1.y)]
        else:
            return self.activacion

    def aprendizajes(self,i,ang,vel,x,y):
        if(i==3):#art1
            self.c=[i,ang,vel] #i->codigo comando
            self.aprendizaje.append(self.c)
        elif(i==4):#Art2
            self.c=[i,ang,vel]
            self.aprendizaje.append(self.c)
        elif(i==5):#Art3
            self.c=[i,ang,vel]
            self.aprendizaje.append(self.c)    
        elif(i==6):#abrir/cerrar efectro
            self.c=[i]
            self.aprendizaje.append(self.c)
        elif(i==7):#mover efector
            self.c=[i,x,y,vel]
            self.aprendizaje.append(self.c)
        elif(i==8):#volver al origen 
            self.c=[i]
            self.aprendizaje.append(self.c)   
        else:
            pass
    #9
    def modo_automatico(self,i,p):
        if(self.activacion==True):
            if(len(self.aprendizaje)>=p):
                self.detalle.append([i,"Inicio modo automatico"])
                j=[]
                for a in range(p):
                    h=self.aprendizaje[(len(self.aprendizaje)-(p-a))]
                    if(h[0]==3 or h[0]==4 or h[0]==5):
                        b = self.girar(h[0],h[1],h[2])
                        if(b=='Error2'):
                            pass
                        else:
                            j.append((h[0],b))
                    elif(h[0]==6):
                        #abrir/cerrar efector
                        b=self.accionar_efector(h[0])
                        j.append((h[0],b))
                    elif(h[0]==7):
                        b=self.mover(h[0],h[1],h[2],h[3])
                        j.append((h[0],b))
                    elif(h[0]==8):#volver origen
                        b=self.retorno_origen(h[0])
                        j.append((h[0],b))
                self.detalle.append([i,"Fin modo automatico"])
                return j
            else: #aca hay que devolver otro codigo de error 
                return 2
        else:
            return 3

            


