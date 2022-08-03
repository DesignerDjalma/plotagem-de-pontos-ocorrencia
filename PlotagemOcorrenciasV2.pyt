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


def calcularCentroid(lista_de_pontos):
    """Calcula o Centroide dos pontos fornecidos."""
    x = 0
    y = 0

    for i in list:
        x += i[0]
        y += i[1]

    centroide = [x,y]

    return centroide


def gd_para_gms(valor, casas=6):
    """transforma as coordenadas de grau decimal para grau minuto

    Args:
        valor (_type_): _description_
        casas (int, optional): _description_. Defaults to 15.
    """
    def NEWS(v):
        if -60 < v < -46:
            return "W"
        if -10 < v < 3:
            if v > 0:
                return "N"
            if v < 0:
                return "S"
            if v == 0:
                return ""
    letra = NEWS(valor)
    # Verifcação trocar de sinal
    sinal = ""
    if valor < 0:
        valor = abs(valor)
        sinal = "-"

    graus, r = int(valor), valor-int(valor)
    minutos, r2 = int(r*60), r*60-int(r*60) 
    segundos = round(r2*60, casas)
    resultado = '{}{}°{}\'{:.06f}\" {}'.format(sinal,graus, minutos, segundos, letra)
    print(resultado)
    return resultado

# looks like its working
# 100% working
def adiciona_multipontos(lista_de_pontos_quadro, shape_a_adicionar):
    """Pega a lista que é gerada do quadro e tranforma em multipontos"""

    # A list of features and coordinate pairs
    # feature_info = [
    #     [ [1, 2], [2, 4], [3, 7] ],  # lista de pontos = 1 feature
    #     [ [6, 8], [5, 7], [7, 2], [9, 5] ], # lista de pontos = 1 feature
    #     ] # a lista maior # 

    # primeiro formata os pontos para o formato adequado
    ldc = lista_de_pontos_quadro
    l_ldc = ldc.split(';')
    l_l_ldc = [ i.split(' ')[1:] for i in l_ldc ]

    coordenadas_centroides = calcularCentroid(l_l_ldc)

    for j in range(2):
        for i in range(len(l_l_ldc)):
            l_l_ldc[i][j] = float(l_l_ldc[i][j])

    # A list that will hold each of the Multipoint objects
    features_multipontos = []

    # bug correction
    for feature in [l_l_ldc]:
        # Create a Multipoint object based on the array of points
        # Append to theS list of Multipoint objects
        features_multipontos.append(
            arcpy.Multipoint(
                arcpy.Array(
                    [ arcpy.Point(*coords) for coords in feature ]
                )
            )
        )
    # As ultimas duas linhas se referem a inserir no shape/geodatabase 
    # as coordenadas
    cursor = arcpy.da.InsertCursor(shape_a_adicionar, ["SHAPE@"])
    cursor.insertRow(features_multipontos)





# 100%
def atualiza_ultima_linha_tda(nome_da_camada, nome_da_coluna, valor_novo, valor_antigo=' '):
    """Atualiza o ultimo shape criado na tabela de atributos se o mesmo estiver vazio."""

    mxd = arcpy.mapping.MapDocument("CURRENT")
    cmds = arcpy.mapping.ListLayers(mxd)
    d = {i.name:i for i in cmds}

    with arcpy.da.UpdateCursor(d[nome_da_camada], [nome_da_coluna]) as cursor:
        for row in cursor:
            if row[0] == valor_antigo:
                row[0] = valor_novo
                cursor.updateRow(row)








# Funciona Solo
def criarGeometriaVazia(_referencia_espacial,_tipo_de_geometria,_diretorio_saida,_nome_saida):
    """Cria um Shape vazio para inserção de pontos."""

    arcpy.CreateFeatureclass_management(
        spatial_reference=_referencia_espacial,
        geometry_type=_tipo_de_geometria,
        out_path=_diretorio_saida,
        out_name=_nome_saida,
        )





# CLASSES #



class Caminhos:

    """Caminhos utilizados na ToolBox."""

    # diretorio_gdb = "C:\\Users\\{}\\Documents\\BancoDeDadosLocal\\Ocorrencias.gdb\\Poligonos\\MeusPoligonos".format(getpass.getuser())
    diretorio_gdb = r'C:\Users\{}\OneDrive - Brasil BioFuels S.A\GBD_BBF_ocorrencias\GBD_BBF_ocorrencias\ocorrencias_2022.shp'.format(getpass.getuser())
    diretorio_gdb_temp = r"C:\Users\djalma.filho\repositorios\plotagem-de-pontos-ocorrencia\outputShapes\testes\ocorrencias_2022.shp"





class Textos:
    tblabel = texto("Plotadem de Pontos Ocorrência")
    tbalias = texto("plotagemOcorrencias")
    titulo = texto("Plotagem de Coordenadas")
    apresentacao = texto("Esse é o Python Toolbox definitivo que será criado a ferramenta para plotagem de pontos")




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
        pd['banco'].value = Caminhos.diretorio_gdb_temp
        pd['tipo_de_ocorrencia'].filter.list = Ocorrencias.tipos
        pd['latitude'].columns = Ocorrencias.colunas_tabela
        pd['latitude'].filters[1].type = 'GPString'
        pd['latitude'].filters[2].type = 'GPString'

        return pd


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
            ['GPString', 'LONGITUDE ( max: - 46.05   min: - 58.90 )' ],
            ['GPString', 'LATITUDE ( min: - 9.85   max: 2.60 ) '],
            ]


class Informacoes:
    def salvar(valores):
        with open('C:\Banco_de_Dados_Ferramenta\INFO.txt', 'w') as f:
            f.write(valores)


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
        pd = {p.name:p for p in parameters}
        pd['saida'].value = pd['latitude'].valueAsText

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        pd = { p.name:p for p in parameters }
        adiciona_multipontos( pd['latitude'].valueAsText, Caminhos.diretorio_gdb_temp )
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

