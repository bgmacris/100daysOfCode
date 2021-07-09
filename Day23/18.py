'''
*Longitud de una cadena*
Crear una función que calcule la longitud de una cadena alfanumérica. Crear otra función que dada una cadena 
devuelva el primer caracter en mayúsculas y el resto en minúsculas. Pasar una palabra por ambas funciones y 
dar el resultado.
'''

cadena = input('')

length_text = lambda text: f"La cadena de texto tiene {str(len(text))} caracteres"
capitaliza = lambda text: text.lower().capitalize() 

print(length_text(cadena), '->', capitaliza(cadena))
