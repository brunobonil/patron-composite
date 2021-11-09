class IForma():
    def print():
        raise NotImplementedError

class Cuadrado(IForma):
    def print(self):
        print('Dibujar un cuadrado')

class Circulo(IForma):
    def print(self):
        print('Dibujar un circulo')

class Triangulo(IForma):
    def print(self):
        print('Dibujar un triangulo')

class CompositeForma(IForma):
    def __init__(self):
        self.child = []
    
    def add(self, forma):
        self.child.append(forma)

    def remove(self, forma):
        self.child.remove(forma)
    
    def print(self):
        for i in self.child:
            i.print()

if __name__ == '__main__':

    cuadrado1 = Cuadrado()
    circulo1 = Circulo()
    triangulo1 = Triangulo()


    composite = CompositeForma()
    composite.add(cuadrado1)        
    composite.add(circulo1)        
    composite.add(triangulo1)       

    composite.print()