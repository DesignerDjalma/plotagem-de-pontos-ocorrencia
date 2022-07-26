# Bibliotecas necessárias
import getpass
import itertools
import re
import arcpy
import os
import sys
import ctypes

# RESPONSÁVEL PELO FORMATAÇÃO DE TEXTO DA FERRAMENTA
reload(sys)
sys.setdefaultencoding("utf-8")

extend_para = {
    "XMax":"-46.05222028269081",
    "XMin":"-58.90753293530914",
    "YMax":"2.6002315813091905",
    "YMin":"-9.850358012309146"
}


### FUNÇÕES ###

def texto(txt):
    """Recebe uma string e formata ao padrão utf-8"""
    return txt.encode('cp1252')


def gms_para_dg(valor, casas=15):
    grau, _, minuto, segundo, direcao =  re.split('[°\'"]', valor)
    gdc = (float(grau) + float(minuto)/60 + float(segundo)/(60*60)) * (-1 if direcao in ['W', 'S', 'O'] else 1)
    return round(gdc, casas)


def gd_para_gms(valor, casas=15):
    """transforma as coordenadas de grau decimal para grau minuto

    Args:
        valor (_type_): _description_
        casas (int, optional): _description_. Defaults to 15.
    """
    graus, r = int(valor), valor-int(valor)
    minutos, r2 = int(r*60), r*60-int(r*60) 
    segundos = round(r2*60, casas)
    resultado = '{}°{}\'{}\"'.format(graus, minutos, segundos)
    print(resultado)


def gms_para_gd_lista(arquivo_texto):
    """
    Args:
        valores (list): lista contendo os valores das coordenadas

    Returns:
        list: coordenadas transformadas
    """ 
    with open(arquivo_texto, 'r') as f:
        a = f.read().split('\n')
        for i in a:
            if not i:
                a.remove(i)


def gms_para_gd_converte(arq):
    with open(arq, 'r') as f:
        a = f.read()
        with open(arq[:-4]+'BKP.txt', "w") as g:
            g.write(a)

        b = a.split('\n')
        for i in b:
            if not i:
                b.remove(i)
        c = []
        for i in b:
            d = i.split(',')
            la = gms_para_dg(d[0].strip())
            lo = gms_para_dg(d[1].strip())
            c.append("{0}, {1}".format(la, lo))
    print(c)
    cor = ''
    for i in c:
        cor += str(i) + '\n'
        
    with open(arq, "w") as f:
        f.write(cor)
        

def string_to_map(mxd, string_da_camada):
    """Retorna o map correspondente a string."""

    if isinstance(string_da_camada, str):
        print("convertendo str to <map>")
        for i in arcpy.mapping.ListLayers(mxd):
            if i.name == string_da_camada:
                string_da_camada = i
                return string_da_camada
    else:
        return string_da_camada


def limpar_selecao(camada):
    """Retira a Selecao feita sobre uma determinada camada"""

    arcpy.SelectLayerByAttribute_management(camada,"CLEAR_SELECTION")


def intersecao(camada_alvo, camada_dica, tipo="INTERSECT"):
    """Pega a camada_dica e seleciona as feicoes na camada alvo,
    retornando o valor na tabela de atributos, para oo atributo especificado"""

    arcpy.SelectLayerByLocation_management(
        camada_dica,
        camada_alvo,
        "INTERSECT",
        )


def zoom_camada(mxd, camada, data_frame):
    """Aplica um zoom numa escala media e numero inteiro."""

    cmds = arcpy.mapping.ListLayers(mxd)
    for i in cmds:
        if i.name == camada.name:
            camada = i

    obj_zoom = camada.getSelectedExtent()
    data_frame.extent = obj_zoom

    # Numbers Trick
    fator = len(str(data_frame.scale).split('.')[0])-1
    z = '1'+'0'*fator
    escala = data_frame.scale/int(z)

    # Exception
    if escala > 2:
        escala = (round(escala,0)*3)*int(z)
        z2 = z + '0'
        escala = round(escala/int(z2),0)*int(z2)
        data_frame.scale = escala
        arcpy.RefreshActiveView()
        return 1

    # Final 
    escala = (round(escala,0)*3)*int(z)
    data_frame.scale = escala
    arcpy.RefreshActiveView()
    return 2


def get_atributo_tda(camada_interesse, ref_cmd, atributo, mostrar=False):
    """Retorna o valor da tabela de atributos da intersecao de camadas"""

    camada_interesse = (camada_interesse)
    camada_alvo = string_to_map(mxd, CMD[ref_cmd])
    intersecao(
        camada_alvo=camada_alvo,camada_dica=camada_interesse
        )
    return get_valor_tda(camada_interesse=camada_alvo, atributo=atributo)


def get_valor_tda(camada_interesse, atributo,):
    """Retorna uma lista com o valor de cada linha no atributo selecionada."""

    cursor = arcpy.SearchCursor(
                dataset=string_to_map(mxd, camada_interesse)
                )
    return [i.getValue(atributo) for i in cursor]



def zoom(mxd, camada, data_frame):
    """Aplica um zoom numa escala media e numero inteiro."""

    cmds = arcpy.mapping.ListLayers(mxd)
    for i in cmds:
        if i.name == camada.name:
            camada = i

    obj_zoom = camada.getSelectedExtent()
    data_frame.extent = obj_zoom

    # Numbers Trick
    fator = len(str(data_frame.scale).split('.')[0])-1
    z = '1'+'0'*fator
    escala = data_frame.scale/int(z)

    # Exception
    if escala > 2:
        escala = (round(escala,0)*3)*int(z)
        z2 = z + '0'
        escala = round(escala/int(z2),0)*int(z2)
        data_frame.scale = escala
        arcpy.RefreshActiveView()
        return [1, camada]

    # Final 
    escala = (round(escala,0)*3)*int(z)
    data_frame.scale = escala
    arcpy.RefreshActiveView()
    print("Escala Selecionada: {}".format(escala))
    return [2, camada]



class TipoDeGeometria:
    ponto = "POINT"
    multiponto = "MULTIPOINT"
    poligono = "POLYGON"
    polilinha = "POLYLINE"


class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS = 4170
    GCS_WGS_1984 = 4326
    GCS_South_American_1969 = 4618
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015

    def referenciaEspacial(self, projecao):
        """Retorna o objeto referencial espacial apartir de uma Projeção

        Args:
            projecao (Projecao): Valor número correpondente ao EPSG
        """
        arcpy.SpatialReference(projecao)


class Constantes:

    """Constantes necessarias para o projeto"""
 
    lLong = [ 'LONG' 		, 9, 0, 0 	]
    lText = [ 'TEXT' 		, 0, 0, 254 ]
    lDate = [ 'DATE' 		, 0, 0, 0 	]
    lDouble=[ 'DOUBLE' 	    , 0, 0, 0 	]

    operacoes_da_tabela_de_atributos = {0:{'OBJECTID':lLong},
        1 :{ 'id'			:lLong},
        2 :{ 'interessad'	:lText},
        3 :{ 'imovel'		:lText},
        4 :{ 'ano'			:lLong},
        5 :{ 'processo'		:lLong},
        6 :{ 'municipio'	:lText},
        7 :{ 'parcela'		:lText},
        8 :{ 'situacao'		:lText},
        9 :{ 'georref'		:lText},
        10:{ 'data'			:lDate},
        11:{ 'complement'	:lText},
        12:{ 'created_us'	:lText},
        13:{ 'created_da'	:lDate},
        14:{ 'last_edite'	:lDate},
        15:{ 'last_edi_1'	:lDate},
        16:{ 'Shape_Leng'	:lDouble},
        17:{ 'Shape_Area'	:lDouble},
        }


class Argumentos:
    pString = {"datatype":"GPString","direction":"Input",}
    pFeatureSelect = {"datatype":"GPFeatureLayer","direction":"Input",}


class Variaveis:
    usuarios_autorizados = [
        'djalma.filho',
        'maria7',
        'desig',
        'dflfilho',
        ]
    campos_string = [
        ["Tipo de Ocorrência","tipo_de_ocorrencia", "Required"],
        ["Propriedade","propriedade","Required"],
        ["Latitude (min:-9.85   max:2.60)","latitude", "Required"],
        ["Longitude (min:-46.05   max:-58.90)","longitude", "Required"],
        ["Data da Ocorrência","data", "Required"],
        ]
    campos_gdb_select = [
        ["Salvar no Banco de Dados em:","banco","Required"]
        ]
    campos_ajuda = [
        [" ","_","Optional"]
    ]

    cs = campos_string
    cgdbs = campos_gdb_select
    ca = campos_ajuda

    apfs = Argumentos.pFeatureSelect
    apgdbs = Argumentos.pFeatureSelect
    aps = Argumentos.pString

    # Pra adicionar mais argumentos basta adicionar eles nos 'elementos'
    # logo em seguinda adicionar a lista de agumentos 'largs'
    # e a lista de campos 'lc'
    elementos = cs + cgdbs + ca
    largs = [aps, aps, aps]
    lc = [cs, cgdbs, ca]


    # super lista de argumentos agrupados de acordo com o numero de elementos presentes nos elementos
    variaveis = list(zip(*elementos)[1]) # sintetizou dezenas de linhas
    args = list(itertools.chain(*[[a]*len(c) for a, c in zip(largs, lc)]))

class Geometria:

    """Geometria(caminho_coordenadas, caminho_shape, tipo_geometria, epsg, plotar)
    
    Inseri um conjunto de Coordenadas apartir de um arquivo .txt
    em um Shape.
    """

    def __init__(self, caminho_coordenadas, caminho_shape, tipo_geometria, epsg, plotar=False):
        self.caminho_coordenadas = caminho_coordenadas
        self.caminho_shape = caminho_shape
        self.tipo_geometria = tipo_geometria
        self.epsg = epsg

        if plotar:
            self.plotar()

    @staticmethod
    def _lerArquivo(caminho_arquivo):
        """Le o arquivos com as coordenadas em formato x,y.

        Args:
            caminho_arquivo (str): caminho contendo o arquivo .txt.

        Returns:
            str: String contendo as coordenadas pseudo-formatadas
        """
        with open(caminho_arquivo, 'r') as f:
            coordenadas = f.read()
            return coordenadas

    @staticmethod
    def _criarGeometriaVazia(caminho_salvar, tipo_geometria, EPSG=4674):
        """Cria uma geometria do tipo POINT vazio.

        Args:
            caminho_salvar (str): caminho no qual o .shp sera salvo
            tipo_geometria (str): "POINT", "POLYLINE" ou "POLYGON".
            EPSG (int, optional): Projecao do Shape. Padrao 4674 SIRGAS 2000.

        Returns:
            str: caminho no qual o .shp foi salvo
        """
        arcpy.CreateFeatureclass_management(
            spatial_reference=arcpy.SpatialReference(EPSG),
            out_path=os.path.dirname(caminho_salvar),
            out_name=os.path.basename(caminho_salvar),
            geometry_type=tipo_geometria,
        )
        return caminho_salvar

    def _plotarCoordenadas(self, coordenadas, shape):
        """Formata as coordenadas e ensira pra cada ponto uma linha na TDA do .shp

        Args:
            coordenadas (str): coordenadas pseudo-formatadas
            shape (str): Caminho do .shp que sera inserida coordenadas
        """
        def _ponto():
            cc = coordenadas.split('\n')
            cc.pop()
            for i in cc:
                xey = i.split(',')
                x, y = float(xey[0]), float(xey[1])
                p = arcpy.Point(x,y)
                cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
                cursor.insertRow([p])

        def _poligono():
            cc = coordenadas.split('\n')
            cc.pop()
            lista = []
            for i in cc:
                xey = i.split(',')
                x, y = float(xey[0]), float(xey[1])
                p = arcpy.Point(x,y)
                lista.append(p)
            array = arcpy.Array(items=lista)
            poligono = arcpy.Polygon(array)
            cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
            cursor.insertRow([poligono])

        if self.tipo_geometria == "POINT":
            _ponto()
        if self.tipo_geometria == "POLYGON":
            _poligono()
            
    def plotar(self):
        """Faz os procedimentos necessarios."""
        
        coordenadas = self._lerArquivo(
            caminho_arquivo=self.caminho_coordenadas)

        shape = self._criarGeometriaVazia(
            caminho_salvar=self.caminho_shape,
            tipo_geometria=self.tipo_geometria,
            EPSG=self.epsg)
        
        
        self._plotarCoordenadas(
            coordenadas=coordenadas,
            shape=shape)



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
        params= [ arcpy.Parameter(displayName=texto(i[0]),name=i[1],parameterType=i[2],**i[3]
            ) for i in [e + [arg] for e, arg in zip(self.elementos, self.args)]]
        params[-2].value = Argumentos.diretorio_gdb
        return params

    def isLicensed(self):
        return True if getpass.getuser() in self.vars.usuarios_autorizados else False

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        for param in parameters:
            messages.addMessage(param.valueAsText)

        return
