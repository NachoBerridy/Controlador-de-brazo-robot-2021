from comandos import *
from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
from gcode import*

class XmlRpc_servidor:


    _metodos_rpc= ['comandos','reporte','G_code']
    def __init__(self, direccion):

        self.comando = Comandos() 
        self.Gcode=gcode()
        self._servidor = SimpleXMLRPCServer (direccion,allow_none=True)
        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self,metodo))

        self.thread = Thread(target = self.iniciar_servidor)
        self.thread.start()

        print("RPC iniciado en puerto",str(self._servidor.server_address))


    def iniciar_servidor(self):
        print("Servidor iniciado")
        self._servidor.serve_forever()
        return "Conectado"

    def apagar_servidor(self):
        self._servidor.shutdown()
        self.thread.join()
        print("Desconectado")
        return "Desconectado"

    def comandos(self,i,ang = 0 ,vel = 0 ,p = 0 ,x = 0 ,y = 0):

        if(int(i)==1):
            a=self.comando.conectar(i)
            return a

        elif(int(i)==2):
            a=self.comando.activar(i)    
            if (a==2):
                return 'Error'
            else:
                return a

        elif(int(i)==3):#art1
            a=self.comando.girar(i,ang,vel)
            if(a==False):
                return 'Error'
            elif(a=='Error1'):
                return 'Error1'
            elif(a=='Error2'):
                return 'Error2'
            else:
                self.Gcode.leergcode("Girar articulacion 1")
                self.comando.aprendizajes(i,ang,vel,x,y)
                return a

        elif(int(i)==4):#Art2
            a=self.comando.girar(i,ang,vel)
            if(a==False):
                return 'Error'
            elif(a=='Error1'):
                return 'Error1'
            elif(a=='Error2'):
                return 'Error2'
            else:
                self.Gcode.leergcode("Girar articulacion 2")
                self.comando.aprendizajes(i,ang,vel,x,y)
                return a
        elif(int(i)==5):#Art3
            a=self.comando.girar(i,ang,vel)
            if(a==False):
                return 'Error'
            elif(a=='Error1'):
                return 'Error1'
            elif(a=='Error2'):
                return 'Error2'
            else:
                self.Gcode.leergcode("Girar articulacion 1")
                self.comando.aprendizajes(i,ang,vel,x,y)
                return a
        elif(int(i)==6):
            a=self.comando.accionar_efector(i)
            if (a==2):
                return 'Error'
            else:
                self.Gcode.leergcode("Accionar efector")
                self.comando.aprendizajes(i,ang,vel,x,y)
                return a
            
        elif(int(i)==7):
            a=self.comando.mover(i,x,y,vel)
            print(a)
            if (a==False):
                return 'Error'
            else:
                self.Gcode.leergcode("Mover efector")
                self.comando.aprendizajes(i,ang,vel,x,y)
                return a
            
        elif(int(i)==8):
            a=self.comando.retorno_origen(i)
            if(a==False):
                return 'Error'
            else:
                self.comando.aprendizajes(i,ang,vel,x,y)
                return a
        elif(int(i)==9):
            a=self.comando.modo_automatico(i,p)
            if(a==2):
                return'Error' 
            elif(a==3):
                return'Error2'
            else:
                return a
        else:
            print("seleccione una opcion valida")
    
    def G_code(self):
        self.Gcode.escribirgcode()
        


    def reporte(self):
        f=open("Reporte.txt","a")
        if (self.comando.conexion==True):
            f.write("La conexion en este momento es: Conectado ")
            f.write("\n")
        else:
            f.write("La conexion en este momento es: Desconectado ")
            f.write("\n")
        if (self.comando.activacion==True):
            f.write("EL estado del robot en este momento es: Encendido ")
            f.write("\n")
        else:
            f.write("EL estado del robot en este momento es: Apagado ")
            f.write("\n")    
        f.write("\n")
        f.write("Tiempo acumulado es: ")
        s=time()
        s=s-self.comando.tinicial
        f.write(str(s))
        f.write("\n")
        f.write("Instante de incio: ")
        t=strftime(' %H:%M:%S %d/%m/%Y',localtime(self.comando.tinicial))
        f.write(str(t))
        f.write("\n\n")
        f.write("--------------------Detalles de las acciones realizadas hasta el momento-------------------- ")
        f.write("\n\n")
        for h in self.comando.detalle:
            if(h[0]==1):
                f.write(">>>Accion ralizada: ")
                f.write(str(h[1]))
                f.write("\n\n")
            elif(h[0]==2):
                f.write(">>>Accion realizada:")
                f.write(str(h[1]))
                f.write("\n\n")
            elif(h[0]==3 ): 
                f.write(">>>Accion realizada: Girar Articulacion 1")
                f.write("\n")
                f.write("       Angulo:")
                f.write(str(h[1]))
                f.write("   Velocidad:")
                f.write(str(h[2]))
                f.write("   Tiempo:") 
                f.write(str(h[3])) 
                f.write("   Tiempo de inicio:") 
                f.write(str(h[4]))  
                f.write("\n\n")

            elif(h[0]==4):
                f.write(">>>Accion realizada: Girar Articulacion 2")
                f.write("\n")
                f.write("       Angulo:")
                f.write(str(h[1]))
                f.write("   Velocidad:")
                f.write(str(h[2]))
                f.write("   Tiempo:") 
                f.write(str(h[3])) 
                f.write("   Tiempo de inicio:") 
                f.write(str(h[4])) 
                f.write("\n\n")
            elif(h[0]==5):
                f.write(">>>Accion realizada: Girar Articulacion 3")
                f.write("\n")
                f.write("       Angulo:")
                f.write(str(h[1]))
                f.write("   Velocidad:")
                f.write(str(h[2]))
                f.write("   Tiempo:")
                f.write(str(h[3]))
                f.write("   Tiempo de inicio:") 
                f.write(str(h[4])) 
                f.write("\n\n")
            elif(h[0]==6):
                f.write(">>>Accion realizada: ")
                f.write(str(h[1]))
                f.write("\n")
                f.write("      Tiempo: ")
                f.write(str(h[2]))
                f.write("   Tiempo de inicio: ")
                f.write(str(h[3]))
                f.write("\n\n")
            elif(h[0]==7):
                f.write(">>>Accion realizada:Mover")
                f.write("\n")
                f.write("       Coordenada x:")
                f.write(str(h[2]))
                f.write("   Coordenada y:")
                f.write(str(h[3]))
                f.write("   Velocidad lineal:") 
                f.write(str(h[4])) 
                f.write("   Tiempo :")
                f.write(str(h[5]))
                f.write("   Tiempo de inicio:")
                f.write(str(h[6]))
                f.write("\n\n")
                
            elif(h[0]==8):#volver origen
                f.write(">>>Accion realizada: ") 
                f.write(str(h[1])) 
                f.write("\n")
                f.write("       Tiempo ")
                f.write(str(h[2]))
                f.write("   Tiempo de inicio:")
                f.write(str(h[3]))
                f.write("\n\n")
            elif(h[0]==9):#modo automatico
                f.write(">>>Accion realizada: ") 
                f.write(str(h[1])) 
                f.write("\n\n")
        f.close() 