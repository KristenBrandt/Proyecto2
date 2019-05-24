# -*- coding: utf-8 -*-
"""
Created on Thu May 23 08:13:00 2019

@author: Odi
"""

# ejemplo de uso de Grafo

import networkx as nx
G = nx.DiGraph()

# agegar nodos
G.add_node("Inicio") # Ocasion, TiempoDeConocerse, Cuidado, Edad, Color
G.add_node("Rosa") # amor, mas, normal, menosDe20, rojo
G.add_node("Rosa blanca") # religioso, mas, normal, masDe20, blanco
G.add_node("Tulipan") # amor, menosDe6, normal, menosDe20, todosColores
G.add_node("Lirio") # religioso, menosDeUnAno, normal, masDe20, todosColores
G.add_node("Girasol") # amistad, menosDe6, normal, menosDe10, amarillo
G.add_node("Cactus") # amistad, menosDe6, facil, menosDe20, verde
G.add_node("Suculenta") # amistad, menosDe6, facil, menosde20, verde
G.add_node("Agapanto") # formal, menosDe5, dificil, masDe20, morado
G.add_node("Venus flytrap") # amistosa, menosDe5 dificil, menosDe20, exotico
G.add_node("Drosera") # amistosa, menosDe5, dificil, menosdDe20, exotico
G.add_node("Nepenthes") # amistosa, menosDe5, dificil, menosDe20, exotico
G.add_node("Helecho") # otra, menosDeUnAno, facil, masDe20, verde
G.add_node("Orquidea") # amorosa, mas, normal, masDe20, exotico

#Variables que regulan el peso de las aristas
amor = 5
amistad = 5
formal = 5
religiosa = 5
otra = 5

menosDe6M = 5
menosDe1A = 5
menosDe5A = 5
mas = 5

facil = 5
normal = 5
dificil = 5

menosDe10 = 5
menosDe20 = 5
masDe20 = 5

rojo = 5
blanco = 5
verde = 5
azul = 5
amarillo = 5
morado = 5
exotico = 5




print("Bienvenido a el programa recomendador de plantas como regalos! ")
print("Responda las siguientes preguntas por favor... ")
print("Responda 0 si desea saltar la pregunta: ")
print("¿Para que tipo de ocasion es el regalo?\n\t1. Amorosa\n\t2. Amistosa\n\t3. Formal\n\t4. Religiosa\n\t5. Otra")
res = input("")
val = int(res)
if val == 0:
    print("Saltando pregunta...")
elif val == 1:
    amor = amor - 5
elif val == 2:
    amistad = amistad -5
elif val == 3:
    formal = formal -5
elif val == 4:
    religiosa = religiosa -5

print("¿Cuanto tiempo llevan de conocerse el recipiente y usted?\n\t1. Menos de 6 meses\n\t2. Menos de un año\n\t3. Menos de 5 años\n\t4. Mas")
res = input("")
val = int(res)
if val == 0:
    print("Saltando pregunta...")
elif val == 1:
    menosDe6M = menosDe6M - 5
elif val == 2:
    menosDe1A = menosDe1A - 5
elif val == 3:
    menosDe5A = menosDe5A - 5
elif val == 4:
    mas = mas  - 5
print("¿Cuanto cuidado cree que el recipiente pueda darle a la planta?\n\t1. Poco\n\t2. Regular\n\t3. Mucho")
res = input("")
val = int(res)
if val == 0:
    print("Saltando pregunta...")
elif val == 1:
    facil = facil -5
elif val == 2:
    normal = normal -5
elif val == 3:
    dificil = dificil -5

print("¿Cuantos años tiene el recipiente?\n\t1. Menos de 10\n\t2. Menos de 20\n\t3. Mas de 20")
res = input("")
val = int(res)
if val == 0:
    print("Saltando pregunta...")
elif val == 1:
    menosDe10 = menosDe10 -5
elif val == 2:
    menosDe20 = menosDe20 -5
    menosDe10 = menosDe10 -5
elif val == 3:
    masDe20 = masDe20 -5
    menosDe20 = menosDe20 -5
    menosDe10 = menosDe10 -5
print("¿Y que hay del color de la planta?\n\t1. Rojo\n\t2. Blanco\n\t3. Verde\n\t4. Azul\n\t5. Amarillo\n\t5. Morado\n\t6. Exotico")
res = input("")
val = int(res)
if val == 0:
    print("Saltando pregunta...")
elif val == 1:
    rojo = rojo -5
elif val == 2:
    blanco = blanco -5
elif val == 3:
    verde = verde -5
elif val == 4:
    azul = azul -5
elif val==5:
    amarillo = amarillo -5
elif val==6:
    exotico = exotico -5

#print ("Nodos: ", G.nodes())


n1 = amor + mas + normal + menosDe20 + rojo
n2 = religiosa + mas + normal + masDe20 + blanco
n3 = amor + menosDe6M + normal + menosDe20 + exotico
n4 = religiosa + menosDe1A + normal + menosDe20 + exotico
n5 = amistad + menosDe6M + normal + menosDe10 + amarillo
n6 = amistad + menosDe6M + facil + menosDe20 + verde
n7 = amistad + menosDe6M + facil + menosDe20 + verde
n8 = formal + menosDe5A + dificil + masDe20 + morado
n9 = amistad + menosDe5A + dificil + menosDe20 + exotico
n10 = amistad + menosDe5A + dificil + menosDe20 + exotico
n11 = amistad + menosDe5A + dificil + menosDe20 + exotico
n12 = otra + menosDe1A + facil + masDe20 + verde
n13 = amor + mas + normal + masDe20 + exotico
# agregar aristas
G.add_edge("Inicio", "Rosa",weight=n1)
G.add_edge("Inicio", "Rosa blanca", weight=n2)
G.add_edge("Inicio", "Tulipan",weight=n3)
G.add_edge("Inicio", "Lirio",weight=n4)
G.add_edge("Inicio", "Girasol",weight=n5)
G.add_edge("Inicio", "Cactus", weight=n6)
G.add_edge("Inicio", "Suculenta", weight=n7)
G.add_edge("Inicio", "Agapanto", weight=n8)
G.add_edge("Inicio", "Venus flytrap", weight=n9)
G.add_edge("Inicio", "Drosera", weight=n10)
G.add_edge("Inicio", "Nepenthes",weight=n11)
G.add_edge("Inicio", "Helecho", weight=n12)
G.add_edge("Inicio", "Orquidea", weight=n13)

G.add_edge("Rosa", "Tulipan",weight=amor)
G.add_edge("Rosa", "Rosa blanca",weight=amor)
G.add_edge("Orquidea", "Tulipan", weight=exotico)
G.add_edge("Rosa", "Girasol",weight=amistad)
G.add_edge("Lirio", "Girasol",weight=amistad)
G.add_edge("Lirio", "Tulipan",weight=exotico)
G.add_edge("Lirio", "Orquidea",weight=exotico)
G.add_edge("Girasol", "Tulipan",weight=menosDe6M)
G.add_edge("Girasol", "Cactus",weight=amistad)
G.add_edge("Cactus", "Girasol",weight=amistad)
G.add_edge("Cactus", "Agapanto",weight=formal)
G.add_edge("Cactus", "Suculenta", weight=facil)
G.add_edge("Cactus", "Helecho", weight=facil)
G.add_edge("Suculenta", "Tulipan", weight=menosDe20)
G.add_edge("Suculenta", "Agapanto",weight=formal)
G.add_edge("Agapanto", "Tulipan", weight=morado)
G.add_edge("Agapanto", "Drosera", weight=dificil)
G.add_edge("Agapanto", "Venus flytrap", weight=dificil)
G.add_edge("Agapanto", "Nepenthes", weight=dificil)
G.add_edge("Venus flytrap", "Cactus", weight=verde)
G.add_edge("Venus flytrap", "Helecho", weight=verde)
G.add_edge("Venus flytrap", "Agapanto", weight=verde)
G.add_edge("Drosera", "Tulipan", weight=exotico)
G.add_edge("Nepenthes", "Cactus", weight=menosDe20)
G.add_edge("Orquidea", "Tulipan", weight=exotico)
G.add_edge("Orquidea", "Rosa blanca", weight=normal)

#print ("Aristas: ", G.edges())

# single source shortest path with Dijkstra

print ()


print
print ("Salieron los resultados!:\n")
resultados = nx.single_source_dijkstra_path_length(G,"Inicio")
for resultado in resultados:
    print (resultado)





