import csv #para leer los datos
import pandas as pd #para crear dataframes
datos=[] #lista para guardar los datos 
transportes=[] #lista para guardar los medios de transporte
paises_origen=[] #lista para guardadr los paises de origen
paises_destino=[] #lista para guardar los paises de destino
frec_imp=0 #inicio contador de importaciones
frec_exp=0 #inicio contador de exportaciones
total_imp=0 #inicio sumatoria de importaciones
total_exp=0 #inicio sumatoria de exportaciones
with open('synergy_logistics_database.csv','r',encoding='utf-8-sig') as archivo:
   lect_dict=csv.DictReader(archivo)#lee la informacion, y crea diccionarios

   for line in lect_dict:
       datos.append(line) #guardar los datos
       if line['transport_mode'] not in transportes: #guardar las diferentes formas de transporte
           transportes.append(line['transport_mode']) 
       if line['origin'] not in paises_origen: #guardar los diferentes paises de origen
           paises_origen.append(line['origin']) 
       if line['destination'] not in paises_destino: #guardar los diferentes paises de origen
           paises_destino.append(line['destination']) 
       if line['direction']=='Exports': #contar y sumar exportaciones
        total_exp+=int(line['total_value'])
        frec_exp+=1
       else:
        total_imp+=int(line['total_value'])#contar y sumar importaciones
        frec_imp+=1
    
#Info general
print('Importaciones totales: ',frec_imp, 'Valor: $',total_imp)
print('Exportaciones totales: ',frec_exp, 'Valor: $',total_exp)
#CONSIGNA 1
"""
#funcion para contar y sumar valor del viaje por pais y direccion
def rutas_valor(pais_origen,direccion):
    lista_ruta=[] #guardar la info de cada pais
    rutas_contadas=[] #guardar las rutas ya evaluadas
    for linea in datos:
        if linea['origin']==pais_origen and linea['direction']==direccion: #crea las rutas
                ruta_actual=[pais_origen,linea['destination']]
                contador=0
                valor=0
                if ruta_actual not in rutas_contadas: 
                    for movimiento in datos: #recorre los datos contando frec y valor
                        if ruta_actual==[movimiento['origin'],movimiento['destination']] and movimiento['direction']==direccion:
                            contador+=1
                            valor+=int(movimiento['total_value'])
                    lista=[pais_origen,linea['destination'],contador,valor] 
                    lista_ruta.append(lista) #guarda la info de las rutas
                    rutas_contadas.append(ruta_actual) #guarda la ruta
        else:
            continue
    return(lista_ruta)


Exportaciones=[] #lista para guardar la info de todos los paises
for pais in paises_origen:#une la info de cada pais
    Exportaciones+=rutas_valor(pais,'Exports')
print('\n \n 10 rutas con mayores exportaciones\n')
Exportaciones.sort(key=lambda x :x[2],reverse=True)#ordena las exportaciones por frecuencia
df_exp=pd.DataFrame(Exportaciones,columns=['Origen','Destino','Viajes totales','Valor Exportado'])#crea data frame
print(df_exp[0:10]) #imprime los datos
viajes=sum(df_exp.loc[0:9,'Viajes totales']) #suma las frecuencia de los 10 primeros datos del df
valor=sum(df_exp.loc[0:9,'Valor Exportado']) #suma el valor de los 10 primeros datos del df
print('Viajes:',viajes)
print('Valor movido: ',valor)
print('Valor Exportado promedio: ',valor/viajes)

Importaciones=[]#lista para guardar la info de todos los paises
for pais in paises_origen:#une la info de cada pais
    Importaciones+=rutas_valor(pais,'Imports')

print('\n \n 10 rutas con mayores importaciones\n')
Importaciones.sort(key=lambda x :x[2],reverse=True)#ordena las importaciones
df_imp=pd.DataFrame(Importaciones,columns=['Origen','Destino','Viajes totales','Valor Importado'])#crea data frame
print(df_imp[0:10])

viajes=sum(df_imp.loc[0:9,'Viajes totales'])#suma las frecuencia de los 10 primeros datos del df
valor=sum(df_imp.loc[0:9,'Valor Importado'])#suma el valor de los 10 primeros datos del df
print('Viajes:',viajes) #imprime los datos
print('Valor movido: ',valor)
print('Valor Importado promedio: ',valor/viajes)
"""

#CONSIGNA 2
"""
 #funcion para contar y sumar valor del viaje por medio de transporte y direccion   
def transporte_valor(modo,direccion):
    valor=0 #inicia sumatoria del valor del viaje
    frec=0 #inicia contador de fecuencia del medio de transporte
    for linea in datos:
        if linea['transport_mode']==modo:
            if linea['direction']==direccion:
                valor+=int(linea['total_value'])
                frec+=1
    lista=[modo,valor,frec] #guarda la info de cada pais
    return(lista)

Exportaciones_ruta=[] #lista para guardar la info de cada medio de transporte
for transporte in transportes:
    Exportaciones_ruta.append(transporte_valor(transporte,'Exports'))#une la info de cada transporte
    
print('\n \n 3 medios de trasnporte con mayores exportaciones\n')
Exportaciones_ruta.sort(key=lambda x :x[1],reverse=True) #ordena las exportaciones por valor
df_transporte_exp=pd.DataFrame(Exportaciones_ruta,columns=['Medio','Valor Exportado','Viajes totales'])#crea df
print(df_transporte_exp[0:3]) #imprime los primeros 3 datos
viajes=sum(df_transporte_exp.loc[0:2,'Viajes totales']) #suma las frecuencia de los 3 primeros datos del df
valor=sum(df_transporte_exp.loc[0:2,'Valor Exportado'])#suma el valor de los 3 primeros datos del df
print('Viajes:',viajes)
print('Valor movido: ',valor)
print('Valor Exportado promedio: ',valor/viajes)

Importaciones_ruta=[]#lista para guardar la info de cada medio de transporte
for transporte in transportes: #une la info de cada transporte
    Importaciones_ruta.append(transporte_valor(transporte,'Imports'))
print('\n \n 3 medios de transporte con mayores importaciones\n')
Importaciones_ruta.sort(key=lambda x :x[1],reverse=True)#ordena las exportaciones por valor
df_transporte_imp=pd.DataFrame(Importaciones_ruta,columns=['Medio','Valor Importado','Viajes totales'])#crea df
print(df_transporte_imp[0:3])#imprime los primeros 3 datos
viajes=sum(df_transporte_imp.loc[0:2,'Viajes totales']) #suma las frecuencia de los 3 primeros datos del df
valor=sum(df_transporte_imp.loc[0:2,'Valor Importado']) #suma el valor de los 3 primeros datos del df
print('Viajes:',viajes)
print('Valor movido: ',valor)
print('Valor Importado promedio: ',valor/viajes)
"""
#CONSIGNA 3
"""
#funcion que ordena la lista e imprime la frecuencia acumulada de la columna que deseas, hasta el 80% del valor acumulado
def acumulado(listas,columna):
    lista_participacion=[] #guarda los datos
    acum=0 #inicio de cuenta la frecuencia acumulada
    listas.sort(key=lambda x :x[columna],reverse=True) #ordena la lista
    for  lista in listas:
        acum+=lista[columna]
        if acum<=83: #mientras sea <80+ margen guarda los datos
            lista.append(acum)
            lista_participacion.append(lista)
        else:
            break
    return(lista_participacion)
            
#funcion para contar y sumar valor del viaje por medio de transporte y direccion 
def imp_exp_value(pais,direccion):
    valor=0 #inicia contador de valor movido
    frec=0 #inicia contador de frecuencia
    for linea in datos:
        if direccion=='Imports':
            if linea['destination']==pais and linea['direction']==direccion:#saca valores si es exportacion
                 valor+=int(linea['total_value'])
                 frec+=1
        else:
            if linea['origin']==pais and linea['direction']==direccion:#saca valores si es importacion
                 valor+=int(linea['total_value'])
                 frec+=1
        
    if direccion=='Imports':
        total=total_imp
    else:
        total=total_exp
    porcentaje=(valor/total)*100 #calcula porcentaje
    lista=[pais,frec,valor,porcentaje] #guarda la info de cada pais
    return(lista)


Exportaciones_pais=[] #lista para guardar la info de cada pais
for pais in paises_origen:
    Exportaciones_pais.append(imp_exp_value(pais,'Exports')) #une la info de cada pais
print('\n \n Rutas con 80% del valor exportaciones\n')
df_pais_exp=pd.DataFrame(acumulado(Exportaciones_pais,3),columns=['Pais','Viajes totales','Valor','Porcentaje','Acumulado'])#crea df
print(df_pais_exp)

viajes=sum(df_pais_exp.loc[:,'Viajes totales']) #suma las frecuencia de los datos del df
valor=sum(df_pais_exp.loc[:,'Valor'])   #suma el valor de del df
print('Viajes:',viajes)
print('Valor movido: ',valor)
print('Valor Exportado promedio: ',valor/viajes)

Importaciones_pais=[] #lista para guardar la info de cada pais
for pais in paises_destino:
    Importaciones_pais.append(imp_exp_value(pais,'Imports'))  #une la info de cada pais

print('\n \n Rutas con 80% del valor importaciones\n')
df_pais_imp=pd.DataFrame(acumulado(Importaciones_pais,3),columns=['Pais','Viajes totales','Valor','Porcentaje','Acumulado']) #crea df
print(df_pais_imp)

viajes=sum(df_pais_imp.loc[:,'Viajes totales']) #suma las frecuencia de los datos del df
valor=sum(df_pais_imp.loc[:,'Valor'])  #suma el valor de del df
print('Viajes:',viajes)
print('Valor movido: ',valor)
print('Valor Importado promedio: ',valor/viajes)
"""