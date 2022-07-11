# Bibliotecas necessárias
import getpass
import arcpy
import os
import sys
import ctypes

# RESPONSÁVEL PELO FORMATAÇÃO DE TEXTO DA FERRAMENTA
reload(sys)
sys.setdefaultencoding("utf-8")

def texto(txt):
    """Recebe uma string e formata ao padrão utf-8"""
    return txt.encode('cp1252')


arcpy.FeatureSet

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = texto("Plotadem de Pontos Ocorrência")
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [PlotagemOcorrencias]


class PlotagemOcorrencias(object):

    def definirVariaveis(self):

        self.usuarios_autorizados = [
            'djalma.filho',
            'maria7',
            'desig',
            'dflfilho',
        ]
        self.campos_string = [
            ["Tipo de Ocorrência","tipo_de_ocorrencia"],
            ["Propriedade","propriedade"],
            ["Latitude","latitude"],
            ["Longitude","longitude"],
            ["Data da Ocorrência","data"],
            ]


    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Plotagem de Coordenadas"
        self.description = texto("Esse é o Python Toolbox definitivo que será criado a ferramenta para plotagem de pontos")
        self.canRunInBackground = False
        self.definirVariaveis()



    def mostrarBoasVindas(self):
        """Mostra uma janela pro usuário. Altamente Bugada. Não usar."""
        MessageBox = ctypes.windll.user32.MessageBoxA
        MessageBox(0, 'Ola Usuario!', 'Janela de Boas-Vindas', 0)


    def getParameterInfo(self):
        """Define parameter definitions"""

        ps = {
            "datatype":"GPString",
            "parameterType":"Required",
            "direction":"Input",
            }

        # clever magic
        params = [
            arcpy.Parameter(displayName=texto(i[0]),name=i[1],**ps
            ) for i in self.campos_string]


        return params

    def isLicensed(self):
        if getpass.getuser() in self.usuarios_autorizados:
            return True
        else:
            return False

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        for param in parameters:
            messages.addMessage(param.valueAsText)

        return
