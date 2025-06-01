series=[["The Office",2005,2013,9,770815,["Comedia"]],
["Breaking Bad",2008,2013,9.5,2314919,["Crimen", "Drama", "Suspenso"]],
["Band of Brothers",2001,2001,9.4,559518,["Acción", "Drama", "Histórica"]],
["Game of Thrones",2011,2019,9.2,2422280,["Acción","Aventura","Drama"]],
["The Simpsons",1989,"NA",8.6,451961,["Animación", "Comedia"]],
["The Sopranos",1999,2007,9.2,520737,["Crimen", "Drama"]],
["Attack on Titan",2013,2023,9.1,602664,["Acción", "Aventura", "Animación"]],
["Chernobyl",2019,2019,9.3,943168,["Drama", "Histórica", "Suspenso"]],
["Friends",1994,2004,8.9,1140227,["Comedia", "Romance"]],
["Lost",2004,2010,8.3,638100,["Aventura", "Drama", "Fantasía"]],
["Dark",2017,2020,8.7,488096,["Crimen", "Drama", "Misterio"]],
["Sherlock",2010,2017,9.1,1044777,["Crimen", "Drama", "Misterio"]],
["31 minutos",2002,2014,9.1,1710,["Comedia", "Familiar", "Fantasía"]],
["Stranger Things",2016,2025,8.6,1435806,["Drama", "Fantasía", "Terror"]],
["Narcos",2015,2017,8.7,498592,["Biográfica", "Crimen", "Drama"]],
["The Mandalorian",2019,"NA",8.6,621020,["Acción", "Aventura", "Fantasía"]],
["House of Cards",2013,2018,8.6,545828,["Drama"]]]

# Pregunta 1
def generos_mejor_calificados(lista):
    todos_generos = []
    
    for serie in lista:
        calificacion = serie[3]
        generos = serie[5]
        
        for genero in generos:
            todos_generos.append((genero, calificacion))
    
    # listar generos unicos
    generos_unicos = []
    for genero, _ in todos_generos:
        encontrado = False
        for g in generos_unicos:
            if g == genero:
                encontrado = True
        if not encontrado:
            generos_unicos.append(genero)
    
    # calcular promedio
    promedios = []
    for genero in generos_unicos:
        suma = 0
        contador = 0
        for g, calif in todos_generos:
            if g == genero:
                suma += calif
                contador += 1
        promedio = suma / contador
        promedios.append((genero, promedio))
    
    # ordenar
    def obtener_orden(item):
        return (-item[1], item[0])  
    
    promedios.sort(key=obtener_orden)
    
    # top5 generos
    resultado = []
    for i in range(min(5, len(promedios))):
        resultado.append(promedios[i][0])
    
    return resultado

print("P1:")
print(generos_mejor_calificados(series))

# Pregunta 2
def recomendar_series(lista, año, lista_generos):
    series_filtradas = []
    
    for serie in lista:
        nombre = serie[0]
        inicio = serie[1]
        fin = serie[2]
        calificacion = serie[3]
        evaluaciones = serie[4]
        generos = serie[5]
        
        # verif si esta en emision 
        if fin == "NA":
            en_emision = (año >= inicio)
        else:
            en_emision = (inicio <= año <= fin)
        
        if not lista_generos:
            genero_valido = True
        else:
            genero_valido = False
            i = 0
            while i < len(generos) and not genero_valido:
                if generos[i] in lista_generos:
                    genero_valido = True
                i += 1
        
        if en_emision and genero_valido:
            series_filtradas.append([nombre, generos, calificacion, evaluaciones])
    
    # ordenar series
    def obtener_orden(serie):
        return (-serie[2], -serie[3])  # desc
    
    series_filtradas.sort(key=obtener_orden)

    resultado = []
    for serie in series_filtradas:
        resultado.append([serie[0], serie[1]])
    
    return resultado

print("P2:")
print(recomendar_series(series,2017,["Drama"]))
print(recomendar_series(series,2020,["Animación"]))
print(recomendar_series(series,2010,[]))
print(recomendar_series(series,2022,["Fantasía","Animación"]))
print(recomendar_series(series,2024,["Biográfica"]))
