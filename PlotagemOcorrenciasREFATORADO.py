# -*- coding: utf-8 -*-


import arcpy
import getpass
import itertools
import inspect


# Importante pra formatação
import sys 
reload(sys) # ignore o erro
sys.setdefaultencoding("utf-8")


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
    """Argumentos usados para criar os parametros.
    
    Atributos:
        string
        featureLayer
        checkBoxes
    """

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


class Validacao:
    
    """Responsável por Autenticar a ferramenta."""
    
    @staticmethod
    def autenticar():
        usuariosPermitidos = [
            'djalma.filho','dflfilho',
            'maria7','desig',
            ]
        user = getpass.getuser()
        allowed = usuariosPermitidos
        return True if user in allowed else False


class Parametros:
    def __init__(self):
        self.campos = Campos()

    def setup(self):
        elementos = []
        argumentos = []

        for i in inspect.getmembers(self.campos):
            if not i[0].startswith("_"):
                setattr(self, i[0], i[1][:-1])
                elementos = elementos + i[1][:-1]
                argumentos = argumentos + [i[1][-1]] # somente o -1

        lc = [j for i in elementos for j in i]
        largs = [j for i in argumentos for j in i]
        
        variaveis = list(zip(*elementos)[1]) 
        args = list(itertools.chain(*[[a]*len(c) for a, c in zip(largs, lc)]))

        params = [ arcpy.Parameter(displayName=texto(i[0]),name=i[1], parameterType=i[2], **i[3]
        ) for i in [e + [arg] for e, arg in zip(elementos, args)]]

        return params



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

    def getParameterInfo(self):
        parametros = Parametros()
        params = parametros.setup()
        return params

    def isLicensed(self):
        return Validacao.autenticar

    def updateParameters(self, parameters):
        pass

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        return



class Teste:
    atributo_1 = "texto"
    atributo_2 = 999
    atributo_3 = ['a','b','c']



if __name__ == "__main__":
    # setattr(objeto, 'nome', 'valor')
    # getattr(objeto, 'nome')

    # t = Teste()
    # setattr(t, 'novo_atributo', ['lista','de','string'])


    # Para poder mudar um atributo é necessario instanciar a classe
    # for i in inspect.getmembers(t):
    #     if not i[0].startswith("_"):
    #         print(i)


    print('Iniciando Testes')

    teste = Teste()
    campos = Campos()
    elementos = []

    # SETANDO TODOS OS ATRIBUTOS DE UMA CLASSE EM OUTRA
    # ASSIM COMO FAZER UMA SUPER LISTA
    for i in inspect.getmembers(campos):
        if not i[0].startswith("_"):
            nome = i[0]
            valor = i[1][:-1]
            setattr(teste, nome, valor)
            elementos = elementos + valor
    
    print("ATRIBUTOS DE TESTE")
    for i in inspect.getmembers(campos):
        if not i[0].startswith("_"):
            print(i)

    print("\nA SUPER LISTA\n")
    print(elementos)
