#LLamado a los archivos de verificación de parámetros
Limit_Hectareas = open ("Proyecto1/Limit_Hectareas.py", "r")
Parametros_Hum = open ("Proyecto1/Parametros_Hum.py", "r")
#Ejecutamos los archivos
exec(Limit_Hectareas.read())
exec(Parametros_Hum.read())
#Le indicamos al usuario que la verificación ha sido completada
print("Verificación de parámetros completada.")
print("Se dará un resumen de los procesos iniciados o detenidos según los parámetros ingresados.")
#Se cierran los archivos
Limit_Hectareas.close()
Parametros_Hum.close()

