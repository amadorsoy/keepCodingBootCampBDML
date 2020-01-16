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
    "https://datos.madrid.es/egob/catalogo/212769-0-atencion-medica.csv"
]

names_array = [
    "airbnbmadrid.csv",
    "colegiospublicos.csv",
    "mercadosmunicipales.csv",
    "parquesmunicipales.csv",
    "centrosmedicos.csv"
]

path_temp_array = [
    "/tmp/airbnbmadridtemp.csv",
    "/tmp/colegiospublicostemp.csv",
    "/tmp/mercadosmunicipalestemp.csv",
    "/tmp/parquesmunicipalestemp.csv",
    "/tmp/centrosmedicostemp.csv"
]

encodes_array = [
    "utf8",
    "ISO-8859-1",
    "ISO-8859-1",
    "ISO-8859-1",
    "ISO-8859-1"
]

strBucketName = "ismalp-bda5-keepcoding"
strPathInputDataMadrid = "inputdatamadrid/"

def download_files(request):
    intCounter = 0
    url = ""
    name = ""
    temp = ""
    encode = ""
    gcClient = storage.Client()
    gcBucket = gcClient.get_bucket(strBucketName)
    while intCounter < len(url_array):
        url = url_array[intCounter]
        name = names_array[intCounter]
        temp = path_temp_array[intCounter]
        encode = encodes_array[intCounter]
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
        gcTempFile.writelines(strContentFile)
        print("Loaded from " + temp + " into Temp File Google Cloud")
        print("Upload data to " + strBucketName + " in path " + strPathInputDataMadrid)
        gcFile = gcBucket.blob(strPathInputDataMadrid + name)
        gcFile.upload_from_filename(gcTempFile.name, content_type='text/csv')
        print("Uploaded data to " + strBucketName + " in path " + strPathInputDataMadrid)
        print("Closing files")
        tempFile.close()
        gcTempFile.close()
        print("Files Closed")
        intCounter = intCounter + 1
    return "Success!"