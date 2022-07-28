# -*- coding: utf-8 -*-


from ast import alias
import arcpy
import getpass
import itertools
import inspect


# Importante pra formatação
import sys 
reload(sys) # ignore o erro
sys.setdefaultencoding("utf-8")


# FUNÇÕES


def texto(txt):
    """Recebe uma string e formata ao padrão utf-8."""
    return txt.encode('cp1252')


def textoLista(lista):
    """Recebe uma lista e formata ao padrão utf-8."""
    return [texto(i) for i in lista]


# CLASSES #



class Textos:
    tblabel = texto("Plotadem de Pontos Ocorrência")
    tbalias = texto("plotagemOcorrencias")
    titulo = texto("Plotagem de Coordenadas")
    apresentacao = texto("Esse é o Python Toolbox definitivo que será criado a ferramenta para plotagem de pontos")



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
    checkBoxes = {"datatype":"GPString", "direction":"Input", "multiValue":True}



class Campos:

    """Definição dos Campos que ficaram dentro."""

    c1 = [["Tipo de Ocorrência. (Selecione apenas uma alternativa)","tipo_de_ocorrencia", "Required"],
            Argumentos.checkBoxes]

    c2 = [
          [" NOME DO PONTO || LATITUDE (NY) || LONGITUDE (EX) || Formato: Grau Decimal com PONTO como separador decimal ", "latitude","Required"],
          #[" LATITUDE [ N-Y ]. Formato: Grau Decimal. ( Valores: min: - 9.85   max: 2.60 )                       | Utilizar ponto como separador decimal", "latitude","Required"],
          #["LONGITUDE [ E-X ]. Formato: Grau Decimal. ( Valores: max: - 46.05   min: - 58.90 )               | Utilizar ponto como separador decimal","longitude","Required"],
          ["Propriedade","propriedade","Optional"],
          ["Data da Ocorrência | Formato: DD/MM/AAAA. Ex.: 01/01/2000 -> 31/12/2022","data", "Required"],
            Argumentos.string]

    c3 = [["Salvar no Banco de Dados em:","banco","Required"],
            Argumentos.featureLayer]

    c4 = [["Saída/Ajuda (Output)","saida","Optional"],
            Argumentos.string]


class Parametros:

    """Responsável por recursivamente criar Parametros."""

    def __init__(self):
        self.campos = Campos()

    def get(self):
        """Define recursivamente todos os Parametros baseado nos Campos."""
        parametros = []
        for i in inspect.getmembers(self.campos):
            if not i[0].startswith("_"):
                nome_var = i[0]
                lista_variante = i[1]
                argumento = i[1][-1]
                for j in lista_variante:
                    if j != argumento:
                        parametros.append(arcpy.Parameter(displayName=texto(j[0]),name=j[1],parameterType=j[2],**argumento))
        return parametros

    

    def setup(self, params):
        pd = { p.name:p for p in params } # setting dict
        pd['banco'].value = Caminhos.diretorio_gdb
        pd['tipo_de_ocorrencia'].filter.list = Ocorrencias.tipos
        pd['latitude'].columns = Ocorrencias.colunas_tabela
        pd['latitude'].filters[1].type = 'GPString'
        pd['latitude'].filters[2].type = 'GPString'

        return pd




class Validacao:

    """Responsável por Validar a execução do Programa."""
    
    @staticmethod
    def autenticar():
        usuariosPermitidos = [
            'djalma.filho',
            'maria7',
            'desig',
            'dflfilho',]
        user = getpass.getuser()
        allowed = usuariosPermitidos
        return True if user in allowed else False


class Ocorrencias:
    tipos = textoLista([
        "Ameaça/Agressão",
        "Bloqueio de Via",
        "Crime Ambiental",
        "Invasão",
        "Roubo/Furto",
        "Outros",
        ])
    colunas_tabela = [
            ['GPString', 'NOME DO PONTO'],
            ['GPString', 'LATITUDE ( min: - 9.85   max: 2.60 ) '],
            ['GPString', 'LONGITUDE ( max: - 46.05   min: - 58.90 )' ]
            ]



class Toolbox(object):
    def __init__(self):
        self.label =  Textos.tblabel
        self.alias =  Textos.tbalias
        self.tools = [PlotagemOcorrencias]



class PlotagemOcorrencias(object):
    def __init__(self):
        self.label = Textos.titulo
        self.description = Textos.apresentacao
        self.canRunInBackground = False

    def getParameterInfo(self):
        parametros = Parametros()
        params = parametros.get()
        parametros.setup(params)

        return params

    def isLicensed(self):
        return Validacao.autenticar()

    def updateParameters(self, parameters):
        pass

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        return





if __name__ == "__main__":

    # parametros = Parametros()
    # params = parametros.get()
    # pd = parametros.setup(params)

    # print(type(params))
    # print(params)
    # print(type(pd))
    # print(pd)
    campos = Campos()
    print('\n'*3)
    for i in inspect.getmembers(campos):
        if not i[0].startswith("_"):
            print(i)

