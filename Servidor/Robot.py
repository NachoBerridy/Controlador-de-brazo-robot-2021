from Articulacion import*

class Robot:
    def __init__(self):
        self.x=0
        self.y=0
        self.efector=False
        self.articulacion1 = Articulacion(0.1)
        self.articulacion2 = Articulacion(0.1)
        self.articulacion3 = Articulacion(0.1)
        