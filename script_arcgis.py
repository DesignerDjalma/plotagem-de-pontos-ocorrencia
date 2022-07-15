arcpy.SpatialReference(4674)
a = arcpy.SpatialReference(4674)
a.PCSName
a.GCS
a.datumName
cursor = arcpy.SearchCursor(
                dataset='novo')
                
cursor

class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS = 4170
    GCS_WGS_1984 = 4326
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    GCS_South_American_1969 = 4618
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015


class ReferenciaEspacial:
    def __init__(self, projecao):
        """Retorna o objeto referencial espacial apartir de uma Projeção

        Args:
            projecao (Projecao): Projecao(valor EPSG)
        """
        self._retornaObjetoReferencialEspacial(projecao)

    def _retornaObjetoReferencialEspacial(projecao):
        return arcpy.SpatialReference(projecao)




class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS_2000 = 4674
    GCS_SIRGAS = 4170
    GCS_WGS_1984 = 4326
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    GCS_South_American_1969 = 4618
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015


class ReferenciaEspacial:
    def __init__(self, projecao):
        """Retorna o objeto referencial espacial apartir de uma Projeção

        Args:
            projecao (Projecao): Projecao(valor EPSG)
        """
        self._retornaObjetoReferencialEspacial(projecao)

    def _retornaObjetoReferencialEspacial(projecao):
        return arcpy.SpatialReference(projecao)


ReferenciaEspacial(Projecao.GCS_SIRGAS_2000)
class ReferenciaEspacial:
    def __init__(self, projecao):
        """Retorna o objeto referencial espacial apartir de uma Projeção

        Args:
            projecao (Projecao): Projecao(valor EPSG)
        """
        self._retornaObjetoReferencialEspacial(projecao)
        
    @staticmethod
    def _retornaObjetoReferencialEspacial(projecao):
        return arcpy.SpatialReference(projecao)
        
ReferenciaEspacial(Projecao.GCS_SIRGAS_2000)

class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS_2000 = 4674
    GCS_SIRGAS = 4170
    GCS_WGS_1984 = 4326
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    GCS_South_American_1969 = 4618
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015


class ReferenciaEspacial:
    @staticmethod
    def get(projecao):
        return arcpy.SpatialReference(projecao)
        
ReferenciaEspacial.get
ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)

class ReferenciaEspacial:
    def __init__(self, projecao):
        self.get(projecao)

    @staticmethod
    def get(projecao):
        return arcpy.SpatialReference(projecao)

ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)
del ReferenciaEspacial
del Projecao
ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)

class ReferenciaEspacial:
    def __init__(self, projecao):
        self.get(projecao)

    @staticmethod
    def get(projecao):
        return arcpy.SpatialReference(projecao)



class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS_2000 = 4674
    GCS_SIRGAS = 4170
    GCS_WGS_1984 = 4326
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    GCS_South_American_1969 = 4618
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015
    

ReferenciaEspacial(Projecao.GCS_SIRGAS_2000)
del ReferenciaEspacial
class ReferenciaEspacial:
    """use .get para pegar o objeto"""
    @staticmethod
    def get(projecao):
        return arcpy.SpatialReference(projecao)
        
ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)


class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS_2000 = 4674
    GCS_SIRGAS = 4170
    GCS_WGS_1984 = 4326
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    GCS_South_American_1969 = 4618
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015


class ReferenciaEspacial:
    """use .get para pegar o objeto"""
    @staticmethod
    def get(projecao):
        return arcpy.SpatialReference(projecao)



class TipoDeGeometria:
    ponto = "POINT"
    polilinha = "POLYLINE"
    poligono = "POLYGON"
    multiponto = "MULTIPOINT"
    multilinhas = "MULTIPATCH"



class Geometria:
    referencia_espacial = None
    tipo_de_geometria = None
    diretorio_saida = None
    nome_saida = None

    def __init__(self):
        pass

    #def setValoresGeometria(self, referencia_espacial:ReferencialEspacial, tipo_de_geometria: TipoDeGeometria, diretorio_saida: str, nome_saida: str):
    def setValoresGeometria(self, referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida):
        """São setados os valores que depois serão plotados.

        Args:
            referencia_espacial (ReferenciaEspacial(Projecao)): _description_
            diretorio_saida (str): _description_
            nome_saida (str): _description_
            tipo_de_geometria (TipoDeGeometria): _description_
        """
        self.referencia_espacial = referencia_espacial
        self.tipo_de_geometria = tipo_de_geometria
        self.diretorio_saida = diretorio_saida
        self.nome_saida = nome_saida

    def criarGeometriaVazia(self):
        arcpy.CreateFeatureclass_management(
            spatial_reference=self.referencia_espacial,
            out_path=self.diretorio_saida,
            out_name=self.nome_saida,
            geometry_type=self.tipo_de_geometria,
            )

    def plotarCoordenadas(self, shape, latitude, longitude):
        """Plota um ponto dentro do shape

        Args:
            shape (str): _description_
            latitude (float, int): Y
            longitude (float, int): X
        """
        
        # Fique "long" de "eX"
        valores = latitude, longitude

        for val in valores:
            assert ( isinstance(val, float) or isinstance(val, int)
                ),''.join(("Erro no valor. Valor númerico não fornecido. ",
                            "Valor Recebido: {0}. ",
                            "Tipo de Valor: {1}. ",)).format(val, type(val))

        # longitude = X , latitude = Y
        ponto = arcpy.Point(longitude, latitude)
        cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
        cursor.insertRow([ponto])
        
referencia_espacial = ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)
tipo_de_geometria = TipoDeGeometria.ponto 
diretorio_saida = r'C:\Users\djalma.filho\repositorios\plotagem-de-pontos-ocorrencia\outputShapes'
nome_saida = 'novo_automatico'
Geometria.setValoresGeometria(self, referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida)
setValoresGeometria( referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida)
Geometria.setValoresGeometria( referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida)
g = Geometria()
g.setValoresGeometria(referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida)
g

g.criarGeometriaVazia()
g.plotarCoordenadas(r"C:\Users\djalma.filho\repositorios\plotagem-de-pontos-ocorrencia\outputShapes\novo_automatico.shp", -2.279, -48.288)
g.plotarCoordenadas(r"C:\Users\djalma.filho\repositorios\plotagem-de-pontos-ocorrencia\outputShapes\novo_automatico.shp", -2.279, -48.288)

