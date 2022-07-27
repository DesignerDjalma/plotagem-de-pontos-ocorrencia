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

    c2 = [["Latitude (min:-9.85   max:2.60) Formato: Grau Decimal","latitude", "Required"],
          ["Longitude (min:-46.05   max:-58.90) Formato: Grau Decimal","longitude", "Required"],
          ["Propriedade","propriedade","Required"],
          ["Data da Ocorrência","data", "Required"],
            Argumentos.string]

    c3 = [["Salvar no Banco de Dados em:","banco","Required"],
            Argumentos.featureLayer]

    c4 = [["Saída/Ajuda (Output)","ajuda","Optional"],
            Argumentos.string]



class Validacao:

    """Responsável por Validar a execução do Programa."""
    
    @staticmethod
    def verificar():
        usuariosPermitidos = [
            'djalma.filho',
            'maria7',
            'desig',
            'dflfilho',]

        user = getpass.getuser()
        allowed = usuariosPermitidos
        return True if user in allowed else False



class Parametros:

    """Responsável por recursivamente criar Parametros."""

    def __init__(self):
        self.campos = Campos()

    def setup(self):
        parametros = []
        for i in inspect.getmembers(self.campos):
            if not i[0].startswith("_"):
                p = i[1][0]
                if len(i) > 2:
                    for j in p:
                        parametros.append(
                            arcpy.Parameter(
                            displayName=texto(j[0]),
                            name=j[1],
                            parameterType=j[2],
                            **i[1][-1]
                            )
                        )
                else:
                    parametros.append(
                        arcpy.Parameter(
                            displayName=texto(p[0]),
                            name=p[1],
                            parameterType=p[2],
                            **i[1][-1]
                        )
                    )
        return parametros



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

    def getParameterInfo(self):
        parametros = Parametros()
        params = parametros.setup()
        return params

    def isLicensed(self):
        return Validacao.verificar()

    def updateParameters(self, parameters):
        pass

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        return




if __name__ == "__main__":
    parametros = Parametros()
    params = parametros.setup()
    

