from time import sleep
from xmlrpc.client import ServerProxy
import ctypes
from cmd import Cmd
from winsound import*
from manejo_grafico import*


class cliente(Cmd):

    s = ServerProxy('http://localhost:20064', allow_none=True)
    print("Conexion con el servidor establecida")
    ctypes.windll.user32.MessageBoxW(0,"Conexion con el servidor establecida","Conexion")
    """Interprete de comandos"""
    prompt = "Ingrese un comando:"

    def __init__(self):
        super(cliente,self).__init__()
        self.i = 0
        self.robot3D = grafico(19999)
        pass

    def do_opciones(self,args):
        """>>>Muestra las acciones que puede hacer el servidor"""
        print("----------------------------[COMANDOS]-----------------------------")
        print("\n")
        print("-----------(SELECCIONE LA OPERACIÓN QUE DESEA REALIZAR)------------")
        print("c 1 - Conectar Robot")
        print("c 2 - Activar Robot")
        print("c 3 - Girar articulacion 1")
        print("c 4 - Girar articulacion 2" )
        print("c 5 - Girar articulacion 3")
        print("c 6 - Accionar efector")
        print("c 7 - Mover robot")
        print("c 8 - Volver al origen")
        print("c 9 - Modo automatico")
        print("reporte")
        print("gcode")
        print("exit")
        print("-------------------------------------------------------------------")

    def do_c(self,i): #Comandos
        """>>>Argumento -> numero de operacion que de sea realizar
>>>sintaxis: comando+' '+opcion"""
        self.i = int(i)
        a = 0
        if (self.i == 1 or self.i == 2 or self.i == 6 or self.i == 8):
            a = self.s.comandos(self.i,0,0,0,0,0)
            if(self.i==1):
                Beep(800, 500)
                print (a)
            elif(self.i==2):
                if(a=='Error'):
                    Beep(900,250)
                    ctypes.windll.user32.MessageBoxW(0,"El robot esta desconectado","Error")
                else:
                    Beep(500, 500)
                    print(a)

            elif(self.i==6):
                if(a=='Error'):
                    Beep(900,250)
                    ctypes.windll.user32.MessageBoxW(0,"El robot esta apagado y/o desconectado","Error")
                else:
                    print(a)
            elif(self.i==8):
                if(a=='Error'):
                    Beep(900,250)
                    ctypes.windll.user32.MessageBoxW(0,"El robot esta apagado y/o desconectado","Error")
                else:
                    self.robot3D.mover(a[1][0],a[1][1])
                    for l in range(3):
                        self.robot3D.girar_articulacion(l+3,a[0][l])
                    print(a)


        elif(self.i == 3 or self.i == 4 or self.i == 5):
            angulo = float(input("Ingrese el angulo: "))
            velocidad = float(input("Ingrese la velocidad: "))
            a = self.s.comandos(self.i,angulo,velocidad,0,0,0)
            if(a=='Error'):
                Beep(900,250)
                ctypes.windll.user32.MessageBoxW(0,"El robot esta apagado y/o desconectado","Error")
            elif(a=='Error1'):
                Beep(900,250)
                ctypes.windll.user32.MessageBoxW(0,"No puede ser 0 la velocidad","Error")
            elif(a=='Error2'):
                Beep(900,250)
                ctypes.windll.user32.MessageBoxW(0,"Angulo fuera de rango","Error")
            else:
                self.robot3D.girar_articulacion(self.i,a[self.i-3]*3.1416/180)
                print(a)

        elif(self.i == 7):
            x = float(input("Ingrese la coordenada x: "))
            y = float(input("Ingrese la coordenada y: "))
            velocidad = float(input("Ingrese la velocidad: "))
            a = self.s.comandos(self.i,0,velocidad,0,x,y)
            
            if(a=='Error'):
                Beep(900,250)
                ctypes.windll.user32.MessageBoxW(0,"El robot esta apagado y/o desconectado","Error")
            else:
                self.robot3D.mover(float(a[0]/100),float(a[1]/100))
                print(a)

        elif(self.i == 9):
            p = int(input("Ingrese el numero de acciones que desea repetir: "))
            a =  self.s.comandos(self.i,0,0,p,0,0)
            if(a=='Error'):
                Beep(900,250)
                ctypes.windll.user32.MessageBoxW(0,"No hay tantos movimientos cargados","Error")
            elif(a=='Error2'):
                Beep(900,250)
                ctypes.windll.user32.MessageBoxW(0,"El robot esta apagado y/o desconectado","Error")
            else:
                print(a)
                for j in a:
                    if(j[0]==3 or j[0]==4 or j[0]==5):
                        n=j[0]-3
                        n=j[1][n]
                        #print(n)
                        self.robot3D.girar_articulacion(j[0],n*3.1416/180)
                        sleep(3)
                    elif(j[0]==8):
                        self.robot3D.mover(j[1][1][0],j[1][1][1])
                        for l in range(3):
                            n=j[1][0][l]
                            self.robot3D.girar_articulacion(l+3,n)
                            sleep(3)
                            #print(n)
                    elif(j[0]==7):
                        self.robot3D.mover(float(j[1][0]/100),float(j[1][1]/100))
                    else:
                        pass

        

    def do_reporte(self,args):
        self.s.reporte()
        ctypes.windll.user32.MessageBoxW(0,"Reporte generado","Reporte")
    
    def do_gcode(self,args):
        self.s.G_code()
        ctypes.windll.user32.MessageBoxW(0,"Archivo gcode generado","gcode")

    def do_exit(self,args):
        """">>>Exit: se cierra todo el programa"""
        raise SystemExit() 



    
    

