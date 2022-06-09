# defino funciones del menu principal

def inicio_med():
  cuenta_encontrada = {}

  user = input("Ingrese su usuario: ")
  password = input("Ingrese la contraseña: ")

  for medico in medicos:
    if medico["user_id"] == user:
      if medico["password"] == password:
        print("El usuario esta logueado")
        cuenta_encontrada = cuenta

      else:
        print("Procesando... \nPermiso denegado - Usuario invalido")
  return cuenta_encontrada

#cuenta = inicio_med()
#print(cuenta)

def inicio_pac():
  cuenta_encontrada = {}

  user = input("Ingrese su usuario: ")
  password = input("Ingrese la contraseña: ")

  for paciente in pacientes:
    if paciente["user_id"] == user:
      if paciente["password"] == password:
        print("El usuario esta logueado")
        cuenta_encontrada = cuenta

      else:
        print("Procesando... \nPermiso denegado - Usuario invalido")
  return cuenta_encontrada

#cuenta = inicio_pac()
#print(cuenta)

def salir():
  print("Gracias ", user, " por utilizar nuestro sistema.")


# defino menu inicial

def menu_inicial():
  opcion = 0
  while opcion not in [1,2,3]:
    print("App medica")
    print("1) Ingresar como medico")
    print("2) Ingresar como paciente")
    print("3) Salir")

    opcion = int(input("Seleccione una opcion:"))

    return opcion

#opcion = menu_inicial()
#print("La opción elegida es: " , opcion)



while True:
  opcion = menu_inicial()
  print("La opción elegida es: ", opcion)

  if opcion == 1:
    cuenta = inicio_med()

  elif opcion == 2:
    cuenta = inicio_pac()

  elif opcion == 3:
    salir()