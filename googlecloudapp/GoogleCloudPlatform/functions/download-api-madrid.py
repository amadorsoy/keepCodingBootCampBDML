from google.cloud import storage
from requests import get
import tempfile
import wget
import os

url_array = [
    "https://public.opendatasoft.com/explore/dataset/airbnb-listings/download/?format=csv&disjunctive.host_verifications=true&disjunctive.amenities=true&disjunctive.features=true&q=Madrid&refine.city=Madrid&timezone=Europe/London&use_labels_for_header=true&csv_separator=%3B",
    "https://datos.madrid.es/egob/catalogo/202311-0-colegios-publicos.csv",
    "https://datos.madrid.es/egob/catalogo/200967-0-mercados.csv",
    "https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.csv",
    "https://datos.madrid.es/egob/catalogo/212769-0-atencion-medica.csv",
    "https://datos.madrid.es/datosabiertos/BDC/POIS_TRANSPORTE/Interurbanos/2019/Interurbanos_2019_12.rdf"
]

names_array = [
    "airbnbmadrid.csv",
    "colegiospublicos.csv",
    "mercadosmunicipales.csv",
    "parquesmunicipales.csv",
    "centrosmedicos.csv",
    "metro.csv"
]

path_temp_array = [
    "/tmp/airbnbmadridtemp.csv",
    "/tmp/colegiospublicostemp.csv",
    "/tmp/mercadosmunicipalestemp.csv",
    "/tmp/parquesmunicipalestemp.csv",
    "/tmp/centrosmedicostemp.csv",
    "/tmp/metro.rdf"
]

encodes_array = [
    "utf8",
    "ISO-8859-1",
    "ISO-8859-1",
    "ISO-8859-1",
    "ISO-8859-1",
    "utf8"
]

process_rdf = [
    False,
    False,
    False,
    False,
    False,
    True
]

strBucketName = "ismalp-bda5-keepcoding"
strPathInputDataMadrid = "inputdatamadrid/"

def download_files(request):
    intCounter = 0
    url = ""
    name = ""
    temp = ""
    encode = ""
    process = False
    gcClient = storage.Client()
    gcBucket = gcClient.get_bucket(strBucketName)
    while intCounter < len(url_array):
        url = url_array[intCounter]
        name = names_array[intCounter]
        temp = path_temp_array[intCounter]
        encode = encodes_array[intCounter]
        process = process_rdf[intCounter]
        print("Donwload " + name)
        wget.download(url, out=temp)
        print("Donwload " + name + " finish")
        print("Open temp file " + temp)
        tempFile = open(temp, "rb")
        print("Opened temp file " + temp)
        print("Read data from temp file " + temp)
        contentFile = tempFile.read()
        strContentFile = contentFile.decode(encode)
        print("Readed data from temp file " + temp)
        print("Load from " + temp + " into Temp File Google Cloud")
        gcTempFile = tempfile.NamedTemporaryFile(delete=True, mode='w+t')
        if process == False:
            gcTempFile.writelines(strContentFile)
        else:
            dataContentFile = strContentFile.splitlines(keepends=False)
            gcTempFile.write('nombre,latitud,longitud' + '\n')
            rowDataContentFile = ""
            for lineDataContentFile in dataContentFile:
                if lineDataContentFile.startswith("<geo:feature>"):
                    lineDataContentFile = lineDataContentFile[lineDataContentFile.rfind('>')+1:].lstrip().rstrip()
                    rowDataContentFile = lineDataContentFile.replace(' ', ',')
                if lineDataContentFile.startswith("</cal:location>"):
                    lineDataContentFile = lineDataContentFile[lineDataContentFile.rfind('<geo:name>')+10:].lstrip().rstrip()
                    lineDataContentFile = lineDataContentFile[:lineDataContentFile.rfind('</')-2].lstrip().rstrip()
                    rowDataContentFile = '"' + lineDataContentFile + '",' + rowDataContentFile
                    gcTempFile.write(rowDataContentFile + '\n')
                    rowDataContentFile = ""
        print("Loaded from " + temp + " into Temp File Google Cloud")
        print("Upload data to " + strBucketName + " in path " + strPathInputDataMadrid)
        gcFile = gcBucket.blob(strPathInputDataMadrid + name)
        if gcFile.exists() == True:
            gcFile.delete()
        gcFile.upload_from_filename(gcTempFile.name, content_type='text/csv')
        print("Uploaded data to " + strBucketName + " in path " + strPathInputDataMadrid)
        print("Closing files")
        tempFile.close()
        gcTempFile.close()
        print("Files Closed")
        intCounter = intCounter + 1
    return "Success!"