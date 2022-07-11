# -*- coding: utf-8 -*-

# Bibliotecas necessárias
import getpass
import arcpy
import os
import sys


# RESPONSÁVEL PELO FORMATAÇÃO DE TEXTO DA FERRAMENTA
# reload(sys)
sys.setdefaultencoding("utf-8")

def texto(txt):
    """Recebe uma string e formata ao padrão utf-8"""
    return txt.encode('cp1252')





class PlotadorDeOcorrencias(object):

    usuarios_autorizados = [
        'djalma.filho',
        'maria7',
        'desig',
        'dflfilho',
    ]

    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Plotador de Ocorrências"
        self.alias = "PlotadorDeOcorrencias"

        # List of tool classes associated with this toolbox
        self.tools = [PotadorDeOcorrencias]


class PotadorDeOcorrencias(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "PPlotador de Ocorrências"
        self.description = "Esse é o Python Toolbox definitivo que será criado a ferramenta para plotagem de pontos"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
            ## Define parameter definitions

        ps = {
            "datatype":"GPString",
            "parameterType":"Required",
            "direction":"Input",
            }

        campos = [
            ["Tipo de Ocorrência","tipo_de_ocorrencia"],
            ["Propriedade","propriedade"],
            ["Latitude","latitude"],
            ["Longitude","longitude"],
            ["Data da Ocorrência","data"],
            ]

        # clever magic
        params = [arcpy.Parameter(displayName=texto(i[0]),name=i[1],**ps) for i in campos]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""

        if getpass.getuser() == self.usuarios_autorizados:
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
