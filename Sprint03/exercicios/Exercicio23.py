class Calculo:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def soma(self):
        return(self.x+self.y)
    
    def subtracao(self):
        return(self.x-self.y)
    
calcular=Calculo(4,5)
print(f"Somando: {calcular.x}+{calcular.y} = {calcular.soma()}")
print(f"Subtraindo: {calcular.x}-{calcular.y} = {calcular.subtracao()}")