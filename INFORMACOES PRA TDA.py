
Id, LONG, 6
LAT_GD, DOUBLE, 12, 8
LONG_GD, DOUBLE, 12, 8
LAT_GMS, STRING, 50
LONG_GMS, STRING, 50
TIPO_OCO, STRING, 50
PROP, STRING, 50
DATA, DATE # DIA/MES/ANO 01/01/1999 - 31/12/2099
POLO, STRING, 50


args_double = {
    "field_type":"DOUBLE",
    "field_precision":12,
    "field_scale":8,
    }
args_long = {
    "field_type":"LONG",
    "field_precision":6,
    }
args_string = {
    "field_type":"STRING",
    "field_length":50,
}
args_date = {}

campos_tda = [
    "Id", # LONG
    "LAT_GD",
    "LONG_GD", # DOUBLE
    "LAT_GMS",
    "LONG_GMS", # STRING
    "TIPO_OCO",
    "PROP", # STRING
    "DATA", # DATE
    "POLO", # STRING
    ]



arcpy.management.AddField(
    in_table=,
    field_name=,
    field_alias=,
    field_type=,
    field_precision=,
    field_scale=,
    field_length=,
    )
