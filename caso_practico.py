# Funciones para crear e insertar nodos en un árbol binario de búsqueda

def crear_nodo(value):
    return {'valor': value, 'izq': None, 'der': None}

def insertar(nodo, value):
    if nodo is None:
        return crear_nodo(value)
    if value < nodo['valor']:
        nodo['izq'] = insertar(nodo['izq'], value)
    else:
        nodo['der'] = insertar(nodo['der'], value)
    return nodo


# Funciones para los distintos tipos de recorridos
def inorden(nodo):
    if nodo is not None:
        inorden(nodo['izq'])
        print(nodo['valor'], end=' ')
        inorden(nodo['der'])

def preorden(nodo):
    if nodo is not None:
        print(nodo['valor'], end=' ')
        preorden(nodo['izq'])
        preorden(nodo['der'])

def postorden(nodo):
    if nodo is not None:
        postorden(nodo['izq'])
        postorden(nodo['der'])
        print(nodo['valor'], end=' ')

# Función para imprimir el árbol de forma visual
def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        imprimir_arbol(nodo['der'], nivel + 1)
        print('    ' * nivel + str(nodo['valor']))
        imprimir_arbol(nodo['izq'], nivel + 1)



# MAIN PROGRAM
arbol = None
values = []
root = None
while root is None:
    root = input("Ingrese el valor que sera la raiz del arbol (Numero entero): ")
try:
    value = int(root)
    values.append(value)
except ValueError:
        root = input("Por favor, ingrese un número válido:")

# Se pide al usuario que ingrese valores para el árbol
while True:
    
    entry = input("Ingrese un valor para insertar al árbol (o 'Q' para terminar): ")
    # Si el usuario ingresa -1, se termina la entrada de datos
    if entry.lower() == 'q':
        break
    
    # Intentar convertir la entrada a un entero y agregarlo al árbol
    # Si la conversion falla, es porque no se ingresó un número válido y sigue pidiendo inputs
    # Si la conversión es exitosa, se agrega el valor al árbol
    try:
        value = int(entry)
        values.append(value)
    except ValueError:
        print("Por favor, ingrese un número válido.")
# Por cada elemento ingresado, se llama a la recursiva INSERTAR para construir el árbol
for element in values:
    arbol = insertar(arbol, element)

# Menu para que el usuario elija la forma de recorrer el árbol o imprimirlo
print(f"Árbol creado con los valores: {values}\n")
# Este print es útil para verificar que los valores se han insertado correctamente y para la correción del TPI
while True:
    entrada = input("\n\nSeleccione el tipo de recorrido:\n1. Inorden\n2. Preorden\n3. Postorden\n4. Imprimir Arbol\n5. Salir\nOpción: ")
    if entrada == '1':
        print("Recorrido inorden:")
        inorden(arbol)
    elif entrada == '2':
        print("Recorrido preorden:")
        preorden(arbol)
    elif entrada == '3':
        print("Recorrido postorden:")
        postorden(arbol)
    elif entrada == '4':
        print("Arbol representado visualmente:")
        imprimir_arbol(arbol)
    elif entrada == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Ingrese numeros del 1 al 4.\n")
