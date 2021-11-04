from comandos import *
from cmd import Cmd
from XmlRpc_servidor import*

class Panel_control(Cmd):
    
    """Interprete de comandos"""
    prompt = "Ingrese un comando:"
    
    def __init__(self) :
        super(Panel_control,self).__init__()
        self.inst_servidor = None
    
    def do_servidor(self,args):
        self.inst_servidor = XmlRpc_servidor(('127.0.0.1', 20064))

    def do_opciones(self,args):
        """>>>Muestra las acciones que puede hacer el servidor"""
        print("----------------------------[COMANDOS]-----------------------------")
        print("\n")
        print("-----------(SELECCIONE LA OPERACIÓN QUE DESEA REALIZAR)------------")
        print("1 - Conectar Robot")
        print("2 - Activar Robot")
        print("3 - Girar articulacion 1")
        print("4 - Girar articulacion 2" )
        print("5 - Girar articulacion 3")
        print("6 - Accionar efector")
        print("7 - Mover robot")
        print("8 - Volver al origen")
        print("9 - Modo automatico")
        print("reporte")
        print("gcode")
        print("exit")
        print("-------------------------------------------------------------------")

    def do_c(self,i=0 ,ang = 0 ,vel = 0 ,p = 0 ,x = 0 ,y = 0):
        """>>>Argumento -> numero de operacion que de sea realizar
>>>sintaxis: comando+' '+opcion"""

        if(int(i)==1):
            try:
                a = self.inst_servidor.comando.conectar(i)
                print (a)
            except AttributeError:
                print("Servidor apagado")

        elif(int(i)==2):
            a=self.inst_servidor.comando.activar(i)
            if(a==2) :   
                print ("El Robot esta desconectado")
            else:
                print(a)

        elif(int(i)==3 or int(i)==4 or int(i)==5):#art1
            ang=float(input("Ingrese el angulo de giro: "))
            vel=float(input("Ingrese la velocidad de giro: "))
            self.inst_servidor.comando.aprendizajes(i,ang,vel,x,y)
            a=self.inst_servidor.comando.girar(i,ang,vel)
            if (a==False):
                print ("Error:El Robot esta apagado y/o desconectado")
            elif(a=='Error1'):
                print("Error:No puede ser 0 la velocidad")
            elif(a=='Error2'):
                print("Error:Angulo fuera de rango")
                self.inst_servidor.comando.aprendizajes(i,ang,vel,x,y)
                print(a)

        elif(int(i)==6):
            a=self.inst_servidor.comando.accionar_efector(i)
            if (a==2):
                print ("Error:El Robot esta apagado y/o desconectado")
            else:
                self.inst_servidor.comando.aprendizajes(i,ang,vel,x,y)
                print(a)
            
        elif(int(i)==7):
            x = float(input("Ingrese la coordenada x: "))
            y = float(input("Ingrese la coordenada y: "))
            vel = float(input("Ingrese la velocidad: "))
            a=self.inst_servidor.comando.mover(i,x,y,vel)
            if (a==False):
                print ("Error:El Robot esta apagado y/o desconectado")
            else:
                self.inst_servidor.comando.aprendizajes(i,ang,vel,x,y)
                print(a)
            
        elif(int(i)==8):
            a=self.inst_servidor.comando.retorno_origen(i)
            if (a==False):
                print ("Error:El Robot esta apagado y/o desconectado")
            else:
                self.inst_servidor.comando.aprendizajes(i,ang,vel,x,y)
                print(a)

        elif(int(i)==9):
            p=float(input("Ingrese la cantidad de movimiento para el modo automatico"))
            a=self.inst_servidor.comando.modo_automatico(i,p)
            if(a==2):
                print("No hay tantos movimientos cargados")
            elif(a==3):
                print("Error:El robot esta apagado y/o desconectado")
            else:
                print (a)
        else:
            print("seleccione una opcion valida")

    def do_reporte(self,args):
        """>>>Reporte:Muestra todas las acciones realizadas"""
        self.inst_servidor.reporte()
    
    def do_gcode(self,args):
        """>>>gcode: muestra archivo gcode"""
        self.inst_servidor.Gcode()

    def do_exit(self,args):
        """">>>Exit: se cierra todo el programa"""
        raise SystemExit()    