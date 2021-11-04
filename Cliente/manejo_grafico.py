import sim 
import ctypes


class grafico():
    
    def __init__(self,puerto):
        sim.simxFinish(-1)
        self.clientID = sim.simxStart('127.0.0.1',puerto,True,True,2000,5)
        if self.clientID == 0: 
            ctypes.windll.user32.MessageBoxW(0,"Conectado con Coppeliasim","Coppeliasim")
        else:
            ctypes.windll.user32.MessageBoxW(0,"No se puedo conectar con Coppeliasim","Coppeliasim")
    
        returnCode,self.art1 = sim.simxGetObjectHandle(self.clientID,'Articulacion1',sim.simx_opmode_blocking)

        returnCode,self.posArt1 = sim.simxGetJointPosition(self.clientID, self.art1,sim.simx_opmode_blocking)

        returnCode,self.art2 = sim.simxGetObjectHandle(self.clientID,'Articulacion2',sim.simx_opmode_blocking)

        returnCode,self.posArt2 = sim.simxGetJointPosition(self.clientID, self.art2 ,sim.simx_opmode_blocking)

        returnCode,self.art3 = sim.simxGetObjectHandle(self.clientID,'Articulacion3',sim.simx_opmode_blocking)

        returnCode,self.posArt3 = sim.simxGetJointPosition(self.clientID, self.art3 ,sim.simx_opmode_blocking)

        returnCode,self.efect = sim.simxGetObjectHandle(self.clientID, 'Efector' ,sim.simx_opmode_blocking)

        returnCode,self.posEfect = sim.simxGetObjectPosition(self.clientID, self.efect,- 1 ,sim.simx_opmode_blocking)

        returnCode,self.base = sim.simxGetObjectHandle(self.clientID,'Robot',sim.simx_opmode_blocking)

        #returnCode,self.conexion = sim.simxGetObjectHandle(self.clientID,'NiryoOne_connection',sim.simx_opmode_blocking)

        #returnCode,self.pinza = sim.simxGetObjectHandle(self.clientID,'Pinza',sim.simx_opmode_blocking) 
        
        returnCode,self.cerrar = sim.simxGetIntegerSignal(self.clientID,'Pinza',sim.simx_opmode_blocking) 


    def girar_articulacion(self,i, angulo):

        if (i == 3):
            sim.simxSetJointTargetPosition(self.clientID, self.art1, angulo, sim.simx_opmode_oneshot)
        if (i == 4):
            sim.simxSetJointTargetPosition(self.clientID, self.art2, angulo, sim.simx_opmode_oneshot)
        if (i == 5):
            sim.simxSetJointTargetPosition(self.clientID, self.art3, angulo, sim.simx_opmode_oneshot)
    
    def mover(self,x,y):
       sim.simxSetObjectPosition(self.clientID,self.base,-1,(x,y,0.0510),sim.simx_opmode_streaming)

    def abrir(self):
        if self.cerrar==1:
            sim.simxSetIntegerSignal(self.cerrar,'_close',0)
        else:
            sim.simxSetIntegerSignal(self.cerrar,'_open',1)