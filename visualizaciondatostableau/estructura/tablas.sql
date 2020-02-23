-- ESTRUCTURA PARA ALOJAR LOS DATOS EN BRUTO DE AIRBNB
CREATE TABLE public.airbnbmadrid
(
    id integer,
    listing_url character varying(500) COLLATE pg_catalog."default",
    scrape_id character varying(200) COLLATE pg_catalog."default",
    last_scraped character varying(200) COLLATE pg_catalog."default",
    name character varying(1000) COLLATE pg_catalog."default",
    summary character varying(1000) COLLATE pg_catalog."default",
    space character varying(1000) COLLATE pg_catalog."default",
    description character varying(1000) COLLATE pg_catalog."default",
    experiences_offered character varying(1000) COLLATE pg_catalog."default",
    neighborhood_overview character varying(1000) COLLATE pg_catalog."default",
    notes character varying(1000) COLLATE pg_catalog."default",
    transit character varying(1000) COLLATE pg_catalog."default",
    access character varying(1000) COLLATE pg_catalog."default",
    interaction character varying(1000) COLLATE pg_catalog."default",
    house_rules text COLLATE pg_catalog."default",
    thumbnail_url text COLLATE pg_catalog."default",
    medium_url text COLLATE pg_catalog."default",
    picture_url text COLLATE pg_catalog."default",
    xl_picture_url text COLLATE pg_catalog."default",
    host_id character varying(500) COLLATE pg_catalog."default",
    host_url text COLLATE pg_catalog."default",
    host_name character varying(1000) COLLATE pg_catalog."default",
    host_since character varying(500) COLLATE pg_catalog."default",
    host_location character varying(500) COLLATE pg_catalog."default",
    host_about text COLLATE pg_catalog."default",
    host_response_time character varying(500) COLLATE pg_catalog."default",
    host_response_rate character varying(500) COLLATE pg_catalog."default",
    host_acceptance_rate character varying(500) COLLATE pg_catalog."default",
    host_thumbnail_url character varying(500) COLLATE pg_catalog."default",
    host_picture_url character varying(500) COLLATE pg_catalog."default",
    host_neighbourhood character varying(500) COLLATE pg_catalog."default",
    host_listings_count integer,
    host_total_listings_count integer,
    host_verifications text COLLATE pg_catalog."default",
    street character varying(500) COLLATE pg_catalog."default",
    neighbourhood character varying(500) COLLATE pg_catalog."default",
    neighbourhood_cleansed character varying(500) COLLATE pg_catalog."default",
    neighbourhood_group_cleansed character varying(500) COLLATE pg_catalog."default",
    city character varying(500) COLLATE pg_catalog."default",
    state character varying(500) COLLATE pg_catalog."default",
    zipcode character varying(500) COLLATE pg_catalog."default",
    market character varying(500) COLLATE pg_catalog."default",
    smart_location character varying(500) COLLATE pg_catalog."default",
    country_code character varying(500) COLLATE pg_catalog."default",
    country character varying(500) COLLATE pg_catalog."default",
    latitude character varying(500) COLLATE pg_catalog."default",
    longitude character varying(500) COLLATE pg_catalog."default",
    property_type character varying(500) COLLATE pg_catalog."default",
    room_type character varying(500) COLLATE pg_catalog."default",
    accommodates integer,
    bathrooms numeric(15,5),
    bedrooms numeric(15,5),
    beds numeric(15,5),
    bed_type character varying(500) COLLATE pg_catalog."default",
    amenities text COLLATE pg_catalog."default",
    square_feet numeric(15,5),
    price numeric(15,5),
    weekly_price numeric(15,5),
    monthly_price numeric(15,5),
    security_deposit numeric(15,5),
    cleaning_fee numeric(15,5),
    guests_included integer,
    extra_people integer,
    minimum_nights integer,
    maximum_nights integer,
    calendar_updated character varying(500) COLLATE pg_catalog."default",
    has_availability character varying(500) COLLATE pg_catalog."default",
    availability_30 character varying(500) COLLATE pg_catalog."default",
    availability_60 character varying(500) COLLATE pg_catalog."default",
    availability_90 character varying(500) COLLATE pg_catalog."default",
    availability_365 character varying(500) COLLATE pg_catalog."default",
    calendar_last_scraped character varying(500) COLLATE pg_catalog."default",
    number_of_reviews integer,
    first_review character varying(500) COLLATE pg_catalog."default",
    last_review character varying(500) COLLATE pg_catalog."default",
    review_scores_rating numeric(15,5),
    review_scores_accuracy numeric(15,5),
    review_scores_cleanliness numeric(15,5),
    review_scores_checkin numeric(15,5),
    review_scores_communication numeric(15,5),
    review_scores_location numeric(15,5),
    review_scores_value numeric(15,5),
    license character varying(500) COLLATE pg_catalog."default",
    jurisdiction_names character varying(500) COLLATE pg_catalog."default",
    cancellation_policy character varying(500) COLLATE pg_catalog."default",
    calculated_host_listings_count integer,
    reviews_per_month numeric(15,5),
    geolocation character varying(500) COLLATE pg_catalog."default",
    features character varying(500) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airbnbmadrid
    OWNER to postgres;

-- ESTRUCTURA PARA ALOJAR LOS DATOS UN POCO MÁS CONCRETOS DE AIRBNB
CREATE TABLE public.airbnb
(
    id integer,
    listing_url character varying(500) COLLATE pg_catalog."default",
    host_since character varying(500) COLLATE pg_catalog."default",
    host_location character varying(500) COLLATE pg_catalog."default",
    street character varying(500) COLLATE pg_catalog."default",
    neighbourhood character varying(500) COLLATE pg_catalog."default",
    neighbourhood_cleansed character varying(500) COLLATE pg_catalog."default",
    city character varying(500) COLLATE pg_catalog."default",
    zipcode character varying(500) COLLATE pg_catalog."default",
    market character varying(500) COLLATE pg_catalog."default",
    latitude numeric(18,16),
    longitude numeric(18,16),
    property_type character varying(500) COLLATE pg_catalog."default",
    room_type character varying(500) COLLATE pg_catalog."default",
    accommodates integer,
    bathrooms numeric(15,5),
    bedrooms numeric(15,5),
    beds numeric(15,5),
    bed_type character varying(500) COLLATE pg_catalog."default",
    square_feet numeric(15,5),
    price numeric(15,5),
    security_deposit numeric(15,5),
    minimum_nights integer,
    maximum_nights integer,
    number_of_reviews integer,
    first_review character varying(500) COLLATE pg_catalog."default",
    last_review character varying(500) COLLATE pg_catalog."default",
    review_scores_rating numeric(15,5),
    review_scores_accuracy numeric(15,5),
    review_scores_cleanliness numeric(15,5),
    review_scores_checkin numeric(15,5),
    review_scores_communication numeric(15,5),
    review_scores_location numeric(15,5),
    review_scores_value numeric(15,5),
    cancellation_policy character varying(500) COLLATE pg_catalog."default",
    reviews_per_month numeric(15,5),
    metro integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airbnb
    OWNER to postgres;

-- ESTRUCTURA PARA ALOJAR LOS DATOS DEL METRO DE MADRID
CREATE TABLE public.metromadrid
(
    nombre character varying(500) COLLATE pg_catalog."default",
    latitud numeric(18,16),
    longitud numeric(18,16),
    city character varying(50) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.metromadrid
    OWNER to postgres;


-- ESTRUCTURA PARA ALOJAR EL RESULTADO DE LOS CÁLCULOS DE DISTANCIA ENTRE LOS DATOS DE AIRBNB Y LAS PARADAS DE METRO DE MADRID
CREATE TABLE public.airbnbmetro
(
    id integer,
    nombre character varying(500) COLLATE pg_catalog."default",
    distancia smallint
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airbnbmetro
    OWNER to postgres;



-- CARGA DE LOS DATOS DE DISTANCIA EN LA TABLA AIRBNBMETRO (DISTANCIA EN KM)
Insert Into airbnbmetro(id, nombre, distancia)
select 
	airbnb.id,
	metromadrid.nombre,
	ROUND(6371 * acos(cos(radians(airbnb.latitude)) * cos(radians(metromadrid.latitud)) * cos(radians(metromadrid.longitud) - radians(airbnb.longitude)) + sin(radians(airbnb.latitude)) * sin(radians(metromadrid.latitud)))) as distancia
from airbnb
	left join metromadrid on Upper(metromadrid.city) = Upper(airbnb.market)

-- ELIMINACIÓN DE TODOS AQUELLOS REGISTROS QUE NO TENGAN 1KM O MENOS DE DISTANCIA
DELETE FROM airbnbmetro WHERE DISTANCIA > 1

--CONSULTA DE LOS DATOS A ANALIZAR FINALMENTE
Select airbnb.*, coalesce(paradas.nparadas, 0) as NParadas
from airbnb
	left join (
				select id, count(nombre) as nparadas
				from airbnbmetro
				group by id
	) as paradas on paradas.id = airbnb.id