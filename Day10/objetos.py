class Coete:
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas
        
    def set_cordemadas(self, coordenadas):
        self.coordenadas = coordenadas
        
    def get_cordemadas(self):
        return self.coordenadas

    def move(self):
        self.coordenadas[1] += 2
        
        
