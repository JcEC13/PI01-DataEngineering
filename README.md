# Introducción

Este proyecto se realizó con la finalidad de procesar la información de 4 archivos .csv , limpiar los datos para facilitar el reporte y mediante la publicación de un API publicar los resultados obtenidos.

## Proceso para realizar  el proyecto
### Pasos para la lectura y limpieza de los datos
El objetivo del proyecto es transformar la informacion de los 4 archivos .csv que estan alojados en las siguientes rutas:

`\Datasets\Dirtydata\amazon_prime_titles-score.csv`

`\Datasets\Dirtydata\disney_plus_titles-score.csv`

`\Datasets\Dirtydata\hulu_titles-score (2).csv`

`\Datasets\Dirtydata\netflix_titles-score.csv`

Posteriormente vamos a seguir los siguientes para realizar su respectiva limpieza:

- **Paso 1:** Clonar este repositorio a tu cuenta de GitHub o simplemente descargarlo.
- **Paso 2:** Abrir y ejecutar el notebook "Cleaner.ipynb" que esta ubicado en la ruta:

`\Datasets\Cleaner.ipynb`

- **Paso 3:** Ejecutar todo código que tiene el archivo "Cleaner.ipynb" hasta obtener un nuevo dataframe que sera exportado en la misma carpeta Datasets llamado "data.csv"

------------
### Pasos para realizar el reporte de datos
Para el reporte se decidió realizar mediante la publicacion de un API en un servicio cloud que este caso se hizo en "Deta"(Cabe resaltar que no es necesario subir especificamente en mencionado servicio cloud, queda a tu elección).
El codigo del API se realizó usando la libreria "FastAPI" y encuentra en la siguiente ruta:

`\FastDetaAPI\main.py`

#### Indicaciones sobre la API
El API creado resuelve principalmente 5 tipos de reporte que son los siguientes:

1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma. Para acceder a esta información se realiza mediante la funcion llamada "get_word_count"

2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. Para acceder a esta información se realiza mediante la funcion llamada "get_score_count"

3. La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos. Para acceder a esta información se realiza mediante la funcion llamada "get_second_score"

4. Película que más duró según año, plataforma y tipo de duración. Para acceder a esta información se realiza mediante la funcion llamada "get_longest"

5. Cantidad de series y películas por rating. Para acceder a esta información se realiza mediante la funcion llamada "get_rating_count"

#### Deploy de la API
Para realizar el deploy en este caso se usó Deta, si deseas implementarlo de forma independiente lo puedes hacer siguiendo los pasos que indica el siguiente enlace:

[Implementacion de API con Deta](https://fastapi.tiangolo.com/deployment/deta/?h=de#__tabbed_1_2 "Implementacion de API con Deta")

Si no deseas implementarlo o deseas ver como debería mostrar la imformación, le comparto el siguiente enlace

https://692kcz.deta.dev/

Donde se implementó siguiendo los pasos que indica el enlace compartido previamente.

Para observar a detalle como funciona la API y el proyecto en general presentado puede observar el siguiente video mediante el siguiente enlace :

#### Documentacion adicional de la API
Cada función que presenta la API necesita de una cantidad determinada de parámetros que serán detallandos a continuación:

**Funciones:**
- /get_word_count/{platform}/{keyword}
- /get_score_count/{platform}/{score}/{year}
- /get_second_score/{platform}
- /get_longest/{platform}/{duration_type}/{year}
- /get_rating_count/{rating}

Por la naturaleza de datos que se uso como fuente, algunos parámetros solo admiten una cantidad limitada de opciones para su correcto funcionamiento. Y se detallan a continuación:
- platform (netflix, amazon, hulu y disney)
- duration_type (min, season)
- rating (g, 13+, all, 18+, r, tv-y, tv-y7, nr, 16+, tv-pg, 7+, tv-14, tv-nr, tv-g, pg-13, tv-ma, pg, nc-17, unrated, 16, ages_16_ , ages_18_, all_ages, not_rate, tv-y7-fv, not rated)
