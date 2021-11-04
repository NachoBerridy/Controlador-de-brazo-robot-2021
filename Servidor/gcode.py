import string
class gcode:
    def __init__(self):
        self.codigo=[]
        
    def leergcode(self, A):
        if (A=="Mover efector"):            
           self.codigo.append("Mover efector: ME01")
        if (A=="Girar articulacion 1"):
            self.codigo.append("Girar articulacion 1: GA01")
        if (A=="Girar articulacion 2"):
            self.codigo.append("Girar articulacion 2: GA02")
        if (A=="Girar articulacion 3"):
            self.codigo.append("Girar articulacion 3: GA03")
        if (A=="Accionar efector"):
            self.codigo.append("Accionar efector: AE01")
    
    def escribirgcode(self):
        n=open("Gcode.txt","a")
        for i in self.codigo:
            n.write(i)
            n.write("\n")
        n.close()