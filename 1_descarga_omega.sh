#Definimos el Endpoint base de VizieR

URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

# Guardamos la consulta pura. (Omega Centauri tiene coordenadas RA=201.6970, DE=-47.4795)

ADQL="SELECT Source, RA_ICRS, DE_ICRS, pmRA, pmDE, Gmag, BPmag, RPmag FROM \"I/355/gaiadr3\" WHERE CONTAINS(POINT('ICRS', RA_ICRS, DE_ICRS), CIRCLE('ICRS', 201.6970, -47.4795, 0.5))=1"

# Reemplazamos los espacios por '+' usando 'sed'

URL_ADQL=$(echo $ADQL | sed 's/ /+/g')

wget -q -O omega_bruto.csv "$URL$URL_ADQL" 

echo "Descarga de datos de Omega Centauri completada. Archivo guardado como 'omega_bruto.csv'."