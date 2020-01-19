import pyhs2

drops = [
        "DROP TABLE IF EXISTS metro",
        "DROP TABLE IF EXISTS centrosmedicos",
        "DROP TABLE IF EXISTS colegios",
        "DROP TABLE IF EXISTS mercados",
        "DROP TABLE IF EXISTS parques",
        "DROP TABLE IF EXISTS servicios",
        "DROP TABLE IF EXISTS airbnb",
        "DROP TABLE IF EXISTS casas",
        "DROP TABLE IF EXISTS todojunto"
]

creates = [
        "CREATE TABLE metro(nombre varchar(200), longitud float, latitud float) row format delimited fields terminated by ','",
        "CREATE TABLE centrosmedicos(pk int, nombre STRING, descripcion_entidad STRING, horario STRING, equipamiento STRING, "+
                "transporte STRING, descripcion STRING, accesibilidad int,  content_url STRING, nombre_via STRING, "+
                "clase_vial STRING, tipo_num STRING, num int, planta STRING, puerta STRING, escaleras STRING, orientacion STRING, "+
                "localidad STRING, provincia STRING, codigo_postal STRING, barrio STRING, distrito STRING, "+
                "coordenada_x STRING, coordenada_y STRING, latitud STRING, longitud STRING, telefono STRING, fax STRING, email STRING, "+
                " tipo STRING ) row format delimited fields terminated by ';'",
        "CREATE TABLE colegios(pk int, nombre STRING, descripcion_entidad STRING, horario STRING, equipamiento STRING, "+
                "transporte STRING, descripcion STRING, accesibilidad int,  content_url STRING, nombre_via STRING, "+
                "clase_vial STRING, tipo_num STRING, num int, planta STRING, puerta STRING, escaleras STRING, orientacion STRING, "+
                "localidad STRING, provincia STRING, codigo_postal STRING, barrio STRING, distrito STRING, "+
                "coordenada_x STRING, coordenada_y STRING, latitud STRING, longitud STRING, telefono STRING, fax STRING, email STRING, "+
                " tipo STRING ) row format delimited fields terminated by ';'",
        "CREATE TABLE mercados(pk int, nombre STRING, descripcion_entidad STRING, horario STRING, equipamiento STRING, "+
                "transporte STRING, descripcion STRING, accesibilidad int,  content_url STRING, nombre_via STRING, "+
                "clase_vial STRING, tipo_num STRING, num int, planta STRING, puerta STRING, escaleras STRING, orientacion STRING, "+
                "localidad STRING, provincia STRING, codigo_postal STRING, barrio STRING, distrito STRING, "+
                "coordenada_x STRING, coordenada_y STRING, latitud STRING, longitud STRING, telefono STRING, fax STRING, email STRING, "+
                " tipo STRING ) row format delimited fields terminated by ';'",
        "CREATE TABLE parques(pk int, nombre STRING, descripcion_entidad STRING, horario STRING, equipamiento STRING, "+
                "transporte STRING, descripcion STRING, accesibilidad int,  content_url STRING, nombre_via STRING, "+
                "clase_vial STRING, tipo_num STRING, num int, planta STRING, puerta STRING, escaleras STRING, orientacion STRING, "+
                "localidad STRING, provincia STRING, codigo_postal STRING, barrio STRING, distrito STRING, "+
                "coordenada_x STRING, coordenada_y STRING, latitud STRING, longitud STRING, telefono STRING, fax STRING, email STRING, "+
                " tipo STRING ) row format delimited fields terminated by ';'",
        "CREATE TABLE servicios(pk int, nombre string, longitud float, latitud float, tipo string, lugar string) row format delimited fields terminated by ';'",
        "CREATE TABLE airbnb (ID INT, Listing_Url STRING, Scrape_ID STRING, Last_Scraped STRING, Name STRING, Summary STRING, Space STRING, "+
                "Description STRING, Experiences_Offered STRING, Neighborhood_Overview STRING, Notes STRING, Transit STRING, Access STRING, "+
                "Interaction STRING, House_Rules STRING, Thumbnail_Url STRING, Medium_Url STRING, Picture_Url STRING, XL_Picture_Url STRING, "+
                "Host_ID STRING, Host_URL STRING, Host_Name STRING, Host_Since STRING, Host_Location STRING, Host_About STRING, "+
                "Host_Response_Time STRING, Host_Response_Rate STRING, Host_Acceptance_Rate STRING, Host_Thumbnail_Url STRING, Host_Picture_Url STRING, "+
                "Host_Neighbourhood STRING, Host_Listings_Count STRING, Host_Total_Listings_Count STRING, Host_Verifications STRING, Street STRING, "+
                "Neighbourhood STRING, Neighbourhood_Cleansed STRING, Neighbourhood_Group_Cleansed STRING, City STRING, State STRING, Zipcode STRING, "+
                "Market STRING, Smart_Location STRING, Country_Code STRING, Country STRING, Latitude STRING, Longitude STRING, Property_Type STRING, "+
                "Room_Type STRING, Accommodates STRING, Bathrooms STRING, Bedrooms STRING, Beds STRING, Bed_Type STRING, Amenities STRING, Square_Feet STRING, "+
                "Price FLOAT, Weekly_Price STRING, Monthly_Price STRING, Security_Deposit STRING, Cleaning_Fee STRING, Guests_Included STRING, Extra_People STRING, "+
                "Minimum_Nights INT, Maximum_Nights INT, Calendar_Updated STRING, Has_Availability STRING, Availability_30 STRING, Availability_60 STRING, "+
                "Availability_90 STRING, Availability_365 STRING, Calendar_last_Scraped STRING, Number_of_Reviews STRING, First_Review STRING, "+
                "Last_Review STRING, Review_Scores_Rating STRING, Review_Scores_Accuracy STRING, Review_Scores_Cleanliness STRING, Review_Scores_Checkin STRING, "+
                "Review_Scores_Communication STRING, Review_Scores_Location STRING, Review_Scores_Value STRING, License STRING, Jurisdiction_Names STRING, "+
                "Cancellation_Policy STRING, Calculated_host_listings_count STRING, Reviews_per_Month STRING, Geolocation STRING, Features STRING) "+
                "ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'",
        "CREATE TABLE casas(id int, lastscrapy string, latitude float, longitude float, lugar string)",
        "CREATE TABLE todojunto(casaid int, casaslatitud float, casaslongitud float, servicioid int, serviciolongitud float, serviciolatitud float, tipo string )"
]

loads = [
        'load data inpath "gs://ismalp-bda5-keepcoding/inputdatamadrid/metro.csv" overwrite into table metro',
        'load data inpath "gs://ismalp-bda5-keepcoding/inputdatamadrid/centrosmedicos.csv" overwrite into table centrosmedicos',
        'load data inpath "gs://ismalp-bda5-keepcoding/inputdatamadrid/colegiospublicos.csv" overwrite into table colegios',
        'load data inpath "gs://ismalp-bda5-keepcoding/inputdatamadrid/mercadosmunicipales.csv" overwrite into table mercados',
        'load data inpath "gs://ismalp-bda5-keepcoding/inputdatamadrid/parquesmunicipales.csv" overwrite into table parques',
        "",
        'load data inpath "gs://ismalp-bda5-keepcoding/inputdatamadrid/airbnbmadrid.csv" overwrite into table airbnb',
        "",
        ""
]

transforms = [
        "insert into servicios(pk, nombre, longitud, latitud, tipo, lugar) select pk, nombre, "+
                "cast(regexp_replace(rtrim(ltrim(longitud)), '"+'"'+"'"+", '') as decimal(19,15)) as longi, "+
                "cast(regexp_replace(rtrim(ltrim(latitud)), '"+'"'+"'"+", '') as decimal(19,15)), 'COLEGIOS', 'MADRID' "+
                " from colegios where longitud like '%.%' and latitud like '%.%'",
        "insert into servicios(pk, nombre, longitud, latitud, tipo, lugar) select pk, nombre, "+
                "cast(regexp_replace(rtrim(ltrim(longitud)), '"+'"'+"'"+", '') as decimal(19,15)) as longi, "+
                "cast(regexp_replace(rtrim(ltrim(latitud)), '"+'"'+"'"+", '') as decimal(19,15)), 'CENTROSMEDICOS', 'MADRID' "+
                " from centrosmedicos where longitud like '%.%' and latitud like '%.%'",
        "insert into servicios(pk, nombre, longitud, latitud, tipo, lugar) select pk, nombre, "+
                "cast(regexp_replace(rtrim(ltrim(longitud)), '"+'"'+"'"+", '') as decimal(19,15)) as longi, "+
                "cast(regexp_replace(rtrim(ltrim(latitud)), '"+'"'+"'"+", '') as decimal(19,15)), 'MERCADOS', 'MADRID' "+
                " from mercados where longitud like '%.%' and latitud like '%.%'",
        "insert into servicios(pk, nombre, longitud, latitud, tipo, lugar) select pk, nombre, "+
                "cast(regexp_replace(rtrim(ltrim(longitud)), '"+'"'+"'"+", '') as decimal(19,15)) as longi, "+
                "cast(regexp_replace(rtrim(ltrim(latitud)), '"+'"'+"'"+", '') as decimal(19,15)), 'PARQUES', 'MADRID' "+
                " from parques where longitud like '%.%' and latitud like '%.%'",
        "insert into servicios(pk, nombre, longitud, latitud, tipo, lugar) select "+
                " row_number() over(order by nombre) as pk, nombre, longitud, latitud, 'METRO', 'MADRID' "+
                " from metro",
        "insert into casas(id,lastscrapy,latitude,longitude, lugar) select id, last_scraped, latitude, longitude, 'MADRID' "+
                " from airbnb where city like '%Madrid%' and latitude like '%.%' and longitude like '%.%'",
        "Insert Into todojunto(casaid, casaslatitud, casaslongitud, servicioid, serviciolongitud, serviciolatitud, tipo) "+
                " select casas.id as casasid, casas.latitude, casas.longitude, servicios.pk as serviciosid, servicios.longitud, servicios.latitud, servicios.tipo "+
                " from casas left join servicios on casas.lugar = coalesce(servicios.lugar, 'MADRID')"
]

intcounter = 0
strdrop = ""
strcreate = ""
strload = ""

with pyhs2.connect(host='localhost', port=10000, authMechanism="PLAIN", user="hive", password="hive-password") as conn:
        with conn.cursor() as cursor:
                while intcounter < len(drops):
                        strdrop = drops[intcounter]
                        strcreate = creates[intcounter]
                        strload = loads[intcounter]
                        if strdrop != "":
                                cursor.execute(strdrop)
                        if strcreate != "":
                                cursor.execute(strcreate)
                        if strload != "":
                                cursor.execute(strload)
                        intcounter = intcounter + 1
                intcounter = 0
                while intcounter < len(transforms):
                        cursor.execute(transforms[intcounter])
                        intcounter = intcounter + 1
        conn.close()