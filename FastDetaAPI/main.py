from fastapi import FastAPI
import pandas as pd

#Instanciar un objeto FastAPI
app=FastAPI()

#Leer el dataset
df=pd.read_csv('https://raw.githubusercontent.com/JcEC13/PI01-DataEngineering/main/dataset/data.csv')

#Funcion de presentacion
@app.get('/')
def index():
    return {'message':'Bienvenido a mi Api',
    'opcion 1': 'get_word_count',
    'opcion 2': 'get_score_count',
    'opcion 3': 'get_second_score',
    'opcion 4': 'get_longest',
    'opcion 5': 'get_rating_count'}

#Funcion que cuenta la cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get('/get_word_count/{platform}/{keyword}')
def get_word_count(platform,keyword):
    query1 = df.query(f'title.str.contains("{keyword}") and show_id.str.startswith("{platform[0]}")', engine='python')
    df_q1=pd.DataFrame([[platform,len(query1)]],columns=['platform','cantidad'])
    return {'platform':df_q1.iloc[0][0],'cantidad':int(df_q1.iloc[0][1])}

#Funcion que cuenta la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get('/get_score_count/{platform}/{score}/{year}')
def get_score_count(platform,score,year):
    query2=df.query(f'show_id.str.startswith("{platform[0]}") and score>{score} and release_year =={year} ', engine='python')
    df_q2=pd.DataFrame([[platform,len(query2)]],columns=['platform','cantidad'])
    return {'platform':df_q2.iloc[0][0],'cantidad':int(df_q2.iloc[0][1])}

#Funcion que muestra la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos
@app.get('/get_second_score/{platform}')
def get_second_score(platform):
    query3=df.query(f'show_id.str.startswith("{platform[0]}")',engine='python')
    query3=query3[query3['score']==query3['score'].max()]
    query3=query3.sort_values('title')
    query3=query3[['title','score']]
    df_q3=pd.DataFrame([[query3.iloc[1][0],query3.iloc[1][1]]],columns=['title','score'])
    return {'title':df_q3.iloc[0][0],'score':int(df_q3.iloc[0][1])}

#Funcion que muestra la película que más duró según año, plataforma y tipo de duración
@app.get('/get_longest/{platform}/{duration_type}/{year}')
def get_longest(platform,duration_type,year):
    query4=df.query(f'show_id.str.startswith("{platform[0]}") and release_year =={year} and duration_type=="{duration_type}"', engine='python')
    query4=query4[query4['duration_int']==query4['duration_int'].max()]
    query4=query4[['title','duration_int','duration_type']]
    df_q4=pd.DataFrame([[query4.iloc[0][0],query4.iloc[0][1],query4.iloc[0][2]]],columns=['title','duration','duration_type'])
    return {'title':df_q4.iloc[0][0],'duration':int(df_q4.iloc[0][1]),'duration_type':df_q4.iloc[0][2]}

#Funcion que cuenta la cantidad de series y películas por rating
@app.get('/get_rating_count/{rating}')
def get_rating_count(rating):
    query5=df.query(f'rating=="{rating}"')
    df_q5=pd.DataFrame([[rating,len(query5)]],columns=['rating','cantidad'])
    return {'rating':df_q5.iloc[0][0],'cantidad':int(df_q5.iloc[0][1])}