def buscar(lista, Elnumero):
  izquierda = 0
  derecha = len(lista) - 1

  while izquierda <= derecha:
      medio = (izquierda + derecha) // 2
      if lista[medio] == Elnumero:
          return True
      elif lista[medio] < Elnumero:
          izquierda = medio + 1
      else:
          derecha = medio - 1

  return False

def ordenar(lista):
  sirve = True
  while sirve:
      sirve = False
      for i in range(len(lista) - 1):
          if lista[i] > lista[i + 1]:
              lista[i], lista[i + 1] = lista[i + 1], lista[i]
              sirve = True
  return lista

try:
  cant = int(input('Ingresa la cantidad de números que va a tener la lista: '))
except ValueError:
  print('Solo puedes ingresar números.')
  cant = int(input('Ingresa la cantidad de números que va a tener la lista: '))

lista = []
for _ in range(cant):
  try:
     lista.append(int(input('Ingresa un número para añadir a la lista: ')))
  except ValueError:
      print('No ingresaste un número. Por favor, inténtalo nuevamente.')

try:
  numero_buscar = int(input('Ingresa un número para buscar en la lista: '))
  if buscar(ordenar(lista), numero_buscar):
      print('El número que buscas sí está en la lista.')
  else:
      print('El número que buscas no se encuentra en la lista.')
except ValueError:
  print('No ingresaste un número para buscar. Por favor, inténtalo nuevamente.')
