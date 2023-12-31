import pandas as pd

datos={
        "nombre":["Maria","Luis","Carmen"],
        "materias":["Matematicas","Programacion","Mercadotecnia"],
        "promedios":[80,90,100]
}

df_alumnos=pd.DataFrame(datos)
print(df_alumnos)

df_colesterol=pd.read_csv("http://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv",sep=";",decimal=",")
print(df_colesterol)

print(df_colesterol.head())
print(df_colesterol.sample(5))
print(df_colesterol.describe())

print(df_colesterol.shape)
print(df_colesterol.columns)
print(df_colesterol.dtypes)
print(df_colesterol.index)

print("fin")