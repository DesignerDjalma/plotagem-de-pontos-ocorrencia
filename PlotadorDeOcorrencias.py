# -*- coding: utf-8 -*-

import arcpy
import os
import sys


# RESPONSÁVEL PELO FORMATAÇÃO DE TEXTO DA FERRAMENTA
reload(sys)
sys.setdefaultencoding("utf-8")

def texto(txt):
    """Recebe uma string e formata ao padrão utf-8"""
    return txt.encode('cp1252')





class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Plotagem Automatica"
        self.alias = "AutoPlot"

        # List of tool classes associated with this toolbox
        self.tools = [PlotagemAutomatica]


class PlotagemAutomatica(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Plotagem Automatica"
        self.description = "Essa Ferramenta faz a plotagem automatica de coordenadas"
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
            ["Tipo de Ocorrencia","tipo_de_ocorrencia"],
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
        return True

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

        messages.addMessage(parameters[0])
        messages.addMessage(dir(parameters[0]))
        for i in parameters:
            messages.addMessage(i.valueAsText)

        return
