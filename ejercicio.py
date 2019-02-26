# Importar paquetes necesarios: pandas y folium
# Es necesario instalar el paquete folium desde Anaconda Navigator a√±adiendo el canal 'conda-forge'
# Tambi√©n se puede hacer desde el Anaconda Prompt con el comando: 'conda install -c conda-forge folium'
import folium

# Debeis descargaros un fichero csv con un conjunto de ocurrencias de una especie
# desde la pagina del GBIF (es necesario registrarse): https://www.gbif.org y leerla en un DataFrame
# de pandas. El fichero descargado es zip, as√≠ que hay que
# descomprimirlo para obtener el csv
# ########################################################
import pandas as pd
# Funcion: read_csv (pandas)
datos= pd.read_csv('lynx_pardinus.csv', sep = '\t')
especie= pd.read_csv('mustela_lutreola.csv', sep = '\t')

# Parametros: sep, [index_col], [parse_dates]
# Tutorial: http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#getting-data-in-out
# Referencia: http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# ########################################################

# Debeis crear un mapa para la visualizacion de la especie.
# Es necesario ajustar las coordenadas (norte-este) y el zoom del mapa a la localizacion de la especie
# ########################################################
# Funcion: Map (folium)
# Parametros: location, [zoom_start], [tiles]
# Tutorial: http://python-visualization.github.io/folium/quickstart.html#Getting-Started
# Referencia: http://python-visualization.github.io/folium/modules.html#folium.folium.Map
# ########################################################
specie_map = folium.Map()

# Iteramos por las ocurrencias y las a√±adimos al conjunto de puntos
for label, ocurrence in datos.iterrows():
    # Obtenemos la latitud y la longitud
    longitude = ocurrence['decimalLongitude']
    latitude = ocurrence['decimalLatitude']

    # Comprobamos que existen coordenadas
    if not pd.isnull(latitude): 
        # Creamos el marcador
        # ########################################################
        # Funcion: Marker (folium)
        # Parametros: location, [popup]
        # Tutorial: http://python-visualization.github.io/folium/quickstart.html#Markers
        # Referencia: http://python-visualization.github.io/folium/modules.html#folium.map.Marker
        # ########################################################
        marker = folium.Marker(location=[latitude,longitude],popup='peligro de extinciÛn',icon=folium.Icon(color='green'))
        # Lo insertamos en el mapa
        marker.add_to(specie_map)
for label, ocurrence in especie.iterrows():
    # Obtenemos la latitud y la longitud
    longitude = ocurrence['decimalLongitude']
    latitude = ocurrence['decimalLatitude']       
    if not pd.isnull(latitude): 
        # Creamos el marcador
        # ########################################################
        # Funcion: Marker (folium)
        # Parametros: location, [popup]
        # Tutorial: http://python-visualization.github.io/folium/quickstart.html#Markers
        # Referencia: http://python-visualization.github.io/folium/modules.html#folium.map.Marker
        # ########################################################
        marker = folium.Marker(location=[latitude,longitude],popup='peligro crÌtico de extinciÛn',icon=folium.Icon(color='red'))
        # Lo insertamos en el mapa
        marker.add_to(specie_map)       

# Se guarda el mapa como una pagina web
specie_map.save('mapa.html')
