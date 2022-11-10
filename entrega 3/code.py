import pandas
import gmplot


df = pandas.read_csv('calles_de_medellin_con_acoso.csv', sep= ';')
df['harassmentRisk'] = df['harassmentRisk'].fillna(df['harassmentRisk'].mean())


def algoritmo1(a,b):
    valor=a*b
    return valor

def algoritmo2(a,b):
    valor=a**(10*b)
    return valor

def algoritmo3(a,b):
    valor=30*a+500*b
    return valor

def dijkstra(origen,destino,graph,func):
        menor_distancia={}
        track_predecessor={}

    

        nodos_noVisitados=graph
        numero_Infinito=float("inf")
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

                if func(weight,risk)+menor_distancia[min_distance_node]<menor_distancia[child_node]:

                    menor_distancia[child_node]=func(weight,risk)+menor_distancia[min_distance_node]
                    track_predecessor[child_node]=[min_distance_node,weight,risk]
                    
                
            nodos_noVisitados.pop(min_distance_node)

        currentNode=destino
        total=0
        totalRiesgo=0
        contador=0

        while currentNode !=origen:

            try:

                rastreo_Camino.insert(0, currentNode)
                total+=int(track_predecessor[currentNode][1])
                totalRiesgo+=float(track_predecessor[currentNode][2])
                contador+=1
                currentNode = track_predecessor[currentNode][0]

            except KeyError:

                print("camino is not reachable")
                break

        rastreo_Camino.insert(0, origen)

        if menor_distancia[destino] != numero_Infinito:

            print('mejor camino teniendo en cuenta la distancia y el riesgo de acoso:', rastreo_Camino)
            print('distancia total:', str(total))
            print('media del riesgo de acoso:', str(totalRiesgo/contador))
            return rastreo_Camino
            
def estructura(df):
    origenes_sinRep = df["origin"].unique()
    grafo = {}

    for a in origenes_sinRep :
        grafo[a] = {}

    for i in df.index:

        grafo[df["origin"][i]][df["destination"][i]] =[(df["length"][i]),(df["harassmentRisk"][i])]

        if df['oneway'][i] == True:

            grafo[df['destination'][i]] = {df["origin"][i]: [(df["length"][i]),(df["harassmentRisk"][i])]}
    
    return grafo

def main():

    grafo1=estructura(df)
    grafo2=estructura(df)
    grafo3=estructura(df)

    path1=dijkstra("(-75.5778046, 6.2029412)", "(-75.5762232, 6.266327)" ,grafo1,algoritmo1)
    path2=dijkstra("(-75.5778046, 6.2029412)", "(-75.5762232, 6.266327)" ,grafo2,algoritmo2)
    path3=dijkstra("(-75.5778046, 6.2029412)", "(-75.5762232, 6.266327)" ,grafo3,algoritmo3)

    for i in range(len(path1)):
        path1[i]=eval(path1[i])
    for i in range(len(path2)):
        path2[i]=eval(path2[i])
    for i in range(len(path3)):
        path3[i]=eval(path3[i])

    
    lat=[19.0790,19.0810,19.0850]
    lang=[72.890,72.910,72.930]
    gmapOne=gmplot.GoogleMapPlotter(6.217,-75.567,15)
    gmapOne.scatter(lat,lang,'#ff000',size=50,marker=True)
    lang,lat=zip(*path1)
    gmapOne.plot(lat,lang,'blue',edge_width=2.5)
    lang,lat=zip(*path2)
    gmapOne.plot(lat,lang,'red',edge_width=2.5)
    lang,lat=zip(*path3)
    gmapOne.plot(lat,lang,'green',edge_width=2.5)
    gmapOne.draw("map.html")


main()






















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

