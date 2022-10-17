from tokenize import Double
import pandas

def dijkstra(graph,origin,destination):
        shortest_distance={}
        distancia_total={}
        track_predecessor={}
        unseenNodes=graph
        infinity=999999
        path=[]
        harassmentsRisks={}

        for node in unseenNodes:
            shortest_distance[node]=infinity
        shortest_distance[origin]=0

        while unseenNodes:
            min_distance_node=None
            for node in unseenNodes:

                if min_distance_node is None:
                    min_distance_node=node
                elif shortest_distance[node]<shortest_distance[min_distance_node]:
                    min_distance_node=node
            
                
            path_options=graph[min_distance_node].items()
            for child_node,[weight,risk] in path_options:
                if (weight+(100*risk))+shortest_distance[min_distance_node]<shortest_distance[child_node]:
                    shortest_distance[child_node]=(weight+(100*risk))+shortest_distance[min_distance_node]
                    track_predecessor[child_node]=min_distance_node
                    distancia_total[child_node]=weight
                    harassmentsRisks[child_node]=risk
                
            unseenNodes.pop(min_distance_node)
        currentNode=destination
        total=0
        totalRiesgo=0
        contador=0

        while currentNode !=origin:
            try:
                path.insert(0, currentNode)
                total+=int(distancia_total[currentNode])
                totalRiesgo+=float(harassmentsRisks[currentNode])
                contador+=1
                currentNode = track_predecessor[currentNode]
            except KeyError:
                print("camino is not reachable")
                break
        path.insert(0, origin)

        if shortest_distance[destination] != infinity:
            print('mejor camino teniendo en cuenta la distancia y el riesgo de acoso:', str(path))
            print('distancia total:', str(total))
            print('media del riesgo de acoso:', str(totalRiesgo/contador))
            



df = pandas.read_csv('calles_de_medellin_con_acoso.csv', sep= ';')
average = df['harassmentRisk'].mean()
df['harassmentRisk'] = df['harassmentRisk'].fillna(average)


origenes_sinRep = df["origin"].unique()
grafo = {}

for a in origenes_sinRep :
    grafo[a] = {}

for i in df.index:

        grafo[df["origin"][i]][df["destination"][i]] =[(df["length"][i]),(df["harassmentRisk"][i])]
    
        if df['oneway'][i] == True:
            grafo[df['destination'][i]] = {df["origin"][i]: [(df["length"][i]),(df["harassmentRisk"][i])]}
#---------------------------------------------------------------------------------------------------
# pruebas:    
grafo2={
"a":{"b":[9,0.2],"c":[2,1],"d":[7,3]},
"b":{"c":[1,0.5],"f":[9,0.2]},
"c":{"f":[6,1],"d":[2,1]},
"d":{"e":[2,1],"g":[6,1]},
"e":{"g":[3,1],"h":[2,1]},
"f":{"e":[1,1],"h":[9,0.2]},
"g":{"h":[2,0.3]},
"h":{"g":[2,1]},
}
print(grafo2["a"])
#dijkstra(grafo2,"a","h")
#------------------------------------------------------------------------------------------------
#dijkstra(grafo,'(-75.7161351, 6.3424055)', '(-75.7025278, 6.3425976)')







