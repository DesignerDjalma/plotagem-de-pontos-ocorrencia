var shp = 'users/arthurrocha/zonas_frigorificos'
var zonas = ee.FeatureCollection(shp)
var lista_de_ids = zonas.aggregate_array('ID_1')

print(lista_de_ids.length

for (var i = 0; i < lista_de_ids.length() ; i++){
  print(lista_de_ids[i])
}


function myFunction(item) {
    var zonas_filtrado = ee.FeatureCollection(shp).filter(ee.Filter.eq(item));
    var empty = ee.Image().byte();
    var outline = empty.paint({featureCollection: zonas,color: 1,width: 1});
    Map.addLayer(outline, {palette: 'black'}, 'Zonas Frigoríficas');
    var dissolve = zonas.union()
    var mapbiomas = ee.Image('users/arthurrocha/brasil_coverage_2020').clip(zonas);
    var pasto = ee.Image(1).mask(mapbiomas.select('b1').eq(15));
    Map.addLayer(pasto, {palette:'red'}, 'Classificação MapBiomas')
    var area_pxa = pasto.multiply(ee.Image.pixelArea()).reduceRegion(ee.Reducer.sum(),zonas,30,null,null,false,1e13).get('constant')
    print ('Área usando o ee.Image.pixelArea', ee.Number(area_pxa).divide(1e3));
}
