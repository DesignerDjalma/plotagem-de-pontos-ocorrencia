# -*- encoding: utf-8 *-*

#import arcpy
import getpass
import itertools
import inspect

# Importante pra formatação
import sys 
reload(sys) # ignore o erro
sys.setdefaultencoding("utf-8")
sys.stdout.encoding.encode("utf-8")

# formatador de texto
def texto(txt):
    """Recebe uma string e formata ao padrão utf-8"""
    return txt.encode('cp1252')

def textoLista(lista):
    """Recebe uma lista e formata ao padrão utf-8"""
    return [texto(i) for i in lista]



class Caminhos:
    """Caminhos utilizados na ToolBox."""

    diretorio_gdb = "C:\\Users\\{}\\Documents\\BancoDeDadosLocal\\Ocorrencias.gdb\\Poligonos\\MeusPoligonos".format(getpass.getuser())


class Argumentos:
    """Argumentos usados para criar os parametros."""

    string = {"datatype":"GPString", "direction":"Input"}
    featureLayer = {"datatype":"GPFeatureLayer", "direction":"Input"}
    checkBoxes = {"datatype":"GPString", "direction":"Input"}

class Campos:
    """Definição dos Campos que ficaram dentro."""

    c1 = [["Tipo de Ocorrência","tipo_de_ocorrencia", "Required"],
            Argumentos.checkBoxes]

    c2 = [["Tipo de Ocorrência","tipo_de_ocorrencia", "Required"],
          ["Latitude (min:-9.85   max:2.60) Formato: Grau Decimal","latitude", "Required"],
          ["Longitude (min:-46.05   max:-58.90) Formato: Grau Decimal","longitude", "Required"],
          ["Propriedade","propriedade","Required"],
          ["Data da Ocorrência","data", "Required"],
            Argumentos.string]

    c3 = [["Salvar no Banco de Dados em:","banco","Required"],
            Argumentos.featureLayer]

    c4 = [["Saída/Ajuda (Output)","ajuda","Optional"],
            Argumentos.string]



class Variaveis:
    cs = Campos.c1
    cgdb = Campos.c2
    ca = Campos.c3


class Parametros:
    pass













class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = texto("Plotadem de Pontos Ocorrência")
        self.alias = ""
        # List of tool classes associated with this toolbox
        self.tools = [PlotagemOcorrencias]



class PlotagemOcorrencias(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Plotagem de Coordenadas"
        self.description = texto("Esse é o Python Toolbox definitivo que será criado a ferramenta para plotagem de pontos")
        self.canRunInBackground = False
        self.definirVariaveis()

    def definirVariaveis(self):
        self.vars = Variaveis()
        self.args = self.vars.args
        self.elementos = self.vars.elementos

    def getParameterInfo(self):

        params = [ arcpy.Parameter(displayName=texto(i[0]),name=i[1],parameterType=i[2],**i[3]
        ) for i in [e + [arg] for e, arg in zip(self.elementos, self.args)]]

        params[-2].value = Argumentos.diretorio_gdb
        self.paraDict = { p.name:p for p in params }
        self.paraDict['tipo_de_ocorrencia'].filter.list = self.vars.tipos_ocorrencias
        return params

    def isLicensed(self):
        return True if getpass.getuser() in self.vars.usuarios_autorizados else False

    def updateParameters(self, parameters):
        # Dicionario de Parametros por nome
        self.paraDict = { p.name:p for p in parameters }
        if parameters[0].altered:
            self.paraDict['ajuda'].value = self.paraDict['tipo_de_ocorrencia'].valueAsText



    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        for param in parameters:
            messages.addMessage(param.valueAsText)

        return

class Teste:
    atributo_1 = "texto"
    atributo_2 = 999
    atributo_3 = ['a','b','c']


if __name__ == "__main__":
    # setattr(objeto, 'nome', 'valor')
    # getattr(objeto, 'nome')
    print('Iniciando Testes')

    # t = Teste()
    # setattr(t, 'novo_atributo', ['lista','de','string'])


    # for i in inspect.getmembers(t):
    #     if not i[0].startswith("_"):
    #         print(i)



    # for i in inspect.getmembers(Campos()):
    #     if not i[0].startswith("_"):
    #         print(i[0],i[1][:-1])
    #         print(type(i[0]),type(i[1][:-1]))

    # Para poder mudar um atributo é necessario instanciar a classe
