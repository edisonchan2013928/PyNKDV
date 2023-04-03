# Set layer name, which will be displayed in ui.
layer_name = 'test'
# Set the path to the shapefile
path = '/Users/patrick/output_test1.shp'
# You can also use Reds, Blues, Greys, Greens, Spectral to replace Turbo for display
ramp_name = 'Turbo'
value_field = 'value'
num_classes = 20

# You can also use the following classification method classes to replace QgsClassificationQuantile():
# QgsClassificationEqualInterval() # equal interval
# QgsClassificationQuantile() # equal count
# QgsClassificationJenks() # natural breaks
# QgsClassificationStandardDeviation()
classification_method = QgsClassificationQuantile()
# create layer
vlayer1 = QgsVectorLayer(path, layer_name, "ogr")
# add layer to the project
QgsProject.instance().addMapLayer(vlayer1)

# if you want to display the layer containing data points, uncomment the following lines
# data_points_path = '/Users/patrick/points_layer.gpkg'
# vlayer2 = QgsVectorLayer(data_points_path, 'data_points', "ogr")
# vlayer2.renderer().symbol().symbolLayer(0).setSize(0.2) # choose a appropriate size
# QgsProject.instance().addMapLayer(vlayer2)


layer = QgsProject().instance().mapLayersByName(layer_name)[0]

format = QgsRendererRangeLabelFormat()
format.setFormat("%1 - %2")
format.setPrecision(2)
format.setTrimTrailingZeroes(True)

default_style = QgsStyle().defaultStyle()
color_ramp = default_style.colorRamp(ramp_name)

renderer = QgsGraduatedSymbolRenderer()
renderer.setClassAttribute(value_field)
renderer.setClassificationMethod(classification_method)
renderer.setLabelFormat(format)
renderer.updateClasses(layer, num_classes)
renderer.updateColorRamp(color_ramp)
layer.setRenderer(renderer)
layer.triggerRepaint()