#Validador de contraseña.

#Aqui es donde se define la funcion que validara la contraseña.
def Verificar_Contrasena(contrasena: str) -> bool|str:

    #Aqui se hacer la 1era verificacion, que tiene que tener minimo 8 digitos.
    if len(contrasena) < 8 or ' ' in contrasena:
        return "La contraseña no es segura, tiene que tener minimo 8 digitos"
    
    #Aqui se creo una lista, conde cada lambda valida 1 de las demas validaciones necesarias, solo si tiene mas de 8 digitos.
    validadores = [
        lambda s: any(caracter.islower() for caracter in s),
        lambda s: any(caracter.isupper() for caracter in s),
        lambda s: any(caracter.isdigit() for caracter in s),
        lambda s: any(not caracter.isalnum() for caracter in s),
    ]

    #Aqui con validamos que cada elemento de la lista anterior
    resultados_booleanos = map(lambda func: func(contrasena), validadores)

    #Aqui validamos que todas las validaciones de "resultados_booleanos" son verdaderas "True", si no, da un mensaje he indicaciones.
    if all (resultados_booleanos):
        return True
    else:
        return "Las contraseña no es segura, debe tener mínimo 8 dígitos, minúsculas, MAYUSCULAS, números, 1 carácter no alfanumérico y no tener espacios en blanco"

#Aqui se le pide la contraseña al usuario    
contrasena_usuario = input("Escriba su contraseña para validar: ")

#Aqui es donde se usa la funcion creada "Verificar_Contrasena", para validar la contraseña
resultado = Verificar_Contrasena(contrasena_usuario)

#Aqui es donde se imprimen los mensajes finales
if resultado is True:
    print("✅ Contraseña validada, es segura")
else:
    print(f"❌ {resultado}")