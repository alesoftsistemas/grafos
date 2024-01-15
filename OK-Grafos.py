# Estructura de Datos y Algoritmos
# Facultad de Ciencias Exactas y Naturales
# Universidad Nacional de Catamarca
# Título: Ejemplo de operaciones con Grafos  
# Descripción:  Crea un Grafo y 
# 1. Agrega los nodos N = {A,E,I}
# 2. Agregar las ramas R= {(a,e), (e,i), (i,u)}

# El modulo ‘networkx’ de python tiene en sus funciones soporte para crear y manipular grafos.
# En caso de no tener el módulo networkx instalado, con el comando ‘pip install networkx’ Python 2 
# o ‘pip3 install networkx’ para Python 3 se instalará el modulo.

import networkx as nx # importación del Módulo

# Creación de una instancia de tipo "Grafo"
Grafo = nx.Graph() 
print(Grafo) 

# Una vez que el objeto Grafo ha sido creado, se puede poblar con nodos y conexiones. 
# Para ello se utilizan dos métodos:
# add_node: Añade un único nodo al grafo.
# add_nodes_from: Añade multiples nodos al grafo.
# add_edge: Añade un eje entre los nodos u y v. Si los nodos no existen, se crean y 
#           añaden automáticamente al grafo.
# add_edges_from: Mismo comportamiento que add_edge pero utilizando una colección de ejes. 
#                 Cada eje se define con una tupla (u, v).

# Agregar nodos {A,E,I} 
Grafo.add_node("A")      # add_node("n") agrega "n" como nodo del grafo
Grafo.add_node("E")
Grafo.add_node("I")

# Agregar ramas {(a,e), (e,i), (i,u)} 
Grafo.add_edge("A","E")  # add_edge("e") agrega "e" como borde de un nodo
Grafo.add_edge("E","I")
Grafo.add_edge("I","U")
print(Grafo)