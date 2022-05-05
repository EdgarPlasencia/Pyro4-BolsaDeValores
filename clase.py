import Pyro4

class Empresa:
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.acciones=100
        self.valor=10000
    def comprarA(self,num):
        self.acciones=self.acciones-num
        self.valor=self.valor+(10*num)
    def venderA(self,num):
        self.acciones=self.acciones+num
        self.valor=self.valor-(10*num)
@Pyro4.expose
class Bolsa:
    empresas=[]
    historial=[]
    def agregarE(self,nombre):
        codigo=len(self.empresas)+1
        self.empresas.append(Empresa(nombre,codigo))
        txt='La empresa '+nombre+' se agrego a la bolsa'
        print(txt)
        return txt
    def listar(self):
        txt='Empresa||'+'Codigo||'+'Acciones||'+'Valor'+'\n'
        for i in self.empresas:
            txt=txt+str(i.nombre)+'\t'+str(i.codigo)+'\t'+str(i.acciones)+'\t'+str(i.valor)+'\n'
        print(txt)
        return txt
        
    def comprarB(self,num,codigo):
        for i in self.empresas:
            if(i.codigo==codigo):
                i.comprarA(num)
                txt='Se compro '+str(num)+' acciones en '+i.nombre
                print(txt)
                return txt
    def venderB(self,num,codigo):
        for i in self.empresas:
            if(i.codigo==codigo):
                i.venderA(num)
                txt='Se vendieron '+str(num)+' acciones en '+i.nombre
                print(txt)
                return txt




