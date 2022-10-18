import pandas

def dijkstra(origen,destino,graph):
        menor_distancia={}
        distancia_total={}
        harassmentsRisks={}
        track_predecessor={}
        nodos_noVisitados=graph
        numero_Infinito=999999
        rastreo_Camino=[]
        

        for node in nodos_noVisitados:
            menor_distancia[node]=numero_Infinito
        menor_distancia[origen]=0

        while nodos_noVisitados:

            min_distance_node=None

            for node in nodos_noVisitados:

                if min_distance_node is None:

                    min_distance_node=node

                elif menor_distancia[node]<menor_distancia[min_distance_node]:

                    min_distance_node=node
            
                
            rastreo_Camino_options=graph[min_distance_node].items()

            for child_node,[weight,risk] in rastreo_Camino_options:

                if (weight+(weight*risk))+menor_distancia[min_distance_node]<menor_distancia[child_node]:

                    menor_distancia[child_node]=(weight+(6*risk))+menor_distancia[min_distance_node]
                    track_predecessor[child_node]=min_distance_node
                    distancia_total[child_node]=weight
                    harassmentsRisks[child_node]=risk
                
            nodos_noVisitados.pop(min_distance_node)

        currentNode=destino
        total=0
        totalRiesgo=0
        contador=0

        while currentNode !=origen:

            try:

                rastreo_Camino.insert(0, currentNode)
                total+=int(distancia_total[currentNode])
                totalRiesgo+=float(harassmentsRisks[currentNode])
                contador+=1
                currentNode = track_predecessor[currentNode]

            except KeyError:

                print("camino is not reachable")
                break

        rastreo_Camino.insert(0, origen)

        if menor_distancia[destino] != numero_Infinito:

            print('mejor camino teniendo en cuenta la distancia y el riesgo de acoso:', str(rastreo_Camino))
            print('distancia total:', str(total))
            print('media del riesgo de acoso:', str(totalRiesgo/contador))
            




df = pandas.read_csv('calles_de_medellin_con_acoso.csv', sep= ';')
df['harassmentRisk'] = df['harassmentRisk'].fillna(df['harassmentRisk'].mean())


origenes_sinRep = df["origin"].unique()
grafo = {}

for a in origenes_sinRep :
    grafo[a] = {}

for i in df.index:

    grafo[df["origin"][i]][df["destination"][i]] =[(df["length"][i]),(df["harassmentRisk"][i])]

    if df['oneway'][i] == True:

        grafo[df['destination'][i]] = {df["origin"][i]: [(df["length"][i]),(df["harassmentRisk"][i])]}
#-------------------------------------------------------------------------------------------------------#
# pruebas:    
"""grafo2={
"a":{"b":[9,0.2],"c":[2,1],"d":[7,3]},
"b":{"c":[1,0.5],"f":[9,0.2]},
"c":{"f":[6,1],"d":[2,1]},
"d":{"e":[2,1],"g":[6,1]},
"e":{"g":[3,1],"h":[2,1]},
"f":{"e":[1,1],"h":[9,0.2]},
"g":{"h":[2,0.3]},
"h":{"g":[2,1]},
}"""

#grafo2["h"]["z"]=[200,200]
#grafo2["h"]={"z":[200,200]}
#print(grafo2["h"].items())
#dijkstra(grafo2,"a","h")
#-------------------------------------------------------------------------------------------------#
dijkstra("(-75.5705202, 6.2106275)", "(-75.5613081, 6.2357138)" ,grafo)







