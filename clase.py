import Pyro4

class Empresa:
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.acciones=1000
        self.valor=1000
    def comprarA(self,num):
        self.acciones=self.acciones-num
        self.valor=self.valor+(1*num)
    def venderA(self,num):
        self.acciones=self.acciones+num
        self.valor=self.valor-(1*num)
@Pyro4.expose
class Bolsa:
    empresas=[]
    historial=[]
    def agregarE(self,nombre):
        codigo=len(self.empresas)+1
        self.empresas.append(Empresa(nombre,codigo))
        print('La empresa ',nombre,' se agrego a la bolsa')
    def listar(self):
        print('Empresa||','Codigo||','Valor||','Acciones')
        for i in self.empresas:
            print(i.nombre,i.codigo,i.valor,i.acciones)
    def comprarB(self,num,codigo):
        for i in self.empresas:
            if(i.codigo==codigo):
                i.comprarA(num)
                print('Se compro ',num,' acciones en ',i.nombre)
    def venderB(self,num,codigo):
        for i in self.empresas:
            if(i.codigo==codigo):
                i.venderA(num)
                print('Se vendieron ',num,' acciones en ',i.nombre)






