# Kirubel Aklilu 12 October 2015
from math import pi , acos , sin , cos
import time
from collections import deque
import pickle
from pprint import pprint
names = []
abrv = []
yval = []
xval = []
edge1 = []
edge2 = []
pos = {}
tmpx = 0
edges = {}
index = 0
dist = {} #key = 2 letters, value = dist
myNbrs = 0
firstLetters = []
global globalIndex
globalIndex = 0
romNodes = open("romNodes.txt").read().split()
romEdges = open("romEdges.txt").read().split()
h = len(romEdges)
i = len(romNodes)
for x in range(0,h):
	if x%2 == 0:
		edge1.append(romEdges[x])
	else : 
		edge2.append(romEdges[x])
for x in range(0,i):
   if x%3==0:
      abrv.append(romNodes[x])
   elif x %3 == 1:
       yval.append(romNodes[x])
   elif x %3 ==2:
      xval.append(romNodes[x])
def edgeIt():
        tmp = 0
        for e in edge1:
                edges[e] = []
        for e in edge2:
                edges[e]= []
        while tmp < len(edge1):
                edges[edge1[tmp]].append(edge2[tmp])
                edges[edge2[tmp]].append(edge1[tmp])
                tmp += 1
        #pprint(edges) 
               
def calcd(y1,x1, y2,x2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76 # miles
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
def makePos():
        globalIndex = 0
        while globalIndex < len(abrv):
                pos[abrv[globalIndex]] = [yval[globalIndex], xval[globalIndex]]
                globalIndex += 1              
def makeDist():
     globalIndex = 0
     ar = []
     y1 = 0
     x1 = 0
     y2 = 0
     x2 = 0
     e1 = ""
     e2 = ""
     while globalIndex < len(edge1):
            e1 = edge1[globalIndex]
            e2 = edge2[globalIndex]
            for key in pos:
                  if edge1[globalIndex] == key:
                        ar = pos[key]
                        y1 = ar[0]
                        x1 = ar[1]
                  elif edge2[globalIndex] == key:
                        ar = pos[key]
                        y2 = ar[0]
                        x2 = ar[1]  
            dist[e1+e2] = round(calcd(y1,x1,y2,x2),1)
            globalIndex += 1
                  
def makebfs(first, last, dict, ans, q):
    tmpx = 0
    visited = {first}
    q = deque([first])
    if first not in firstLetters:
            while len(q) > 0:
                word = q.popleft()
                for n in dict[word]:
                    if n not in visited :
                        visited.add(n)
                        q.append(n)
                        ans[n] = word
                        if n == last:
                            return
def find_all_paths(graph, first, last, path=[]):
        tmpx =0
        path= path+ [first]
        if first == last:
            return [path]
        if first not in graph.keys():
            return []
        paths = []
        for n in graph[first]:
            if n not in path:
                nps = find_all_paths(graph, n, last, path)
                for np in nps:
                    paths.append(np)
        return paths
def cost(ar):
        cost = 0
        for i in range(0,len(ar)):
                if( (i+1) < len(ar)):
                        s = ar[i]+ar[i+1]
                        cost += dist[s]
        return round(cost, 2)
                
def mirror(dct):
        ans = {}
        for key in dct:
                first = key[0:1]
                last = key [1:]
                ans[last+first] = dct[key]
        dct.update(ans)
def rom(): 
    makePos()
    makeDist()
    edgeIt()
    dict = edges
    mirror(dist)
    #pprint (dist)
    #pprint (dict)
    first = input("City 1:")
    last = input("City 2:")
    f1 = first[0:1].upper()
    l1 = last[0:1].upper()
    fl = f1+l1
    lf = l1+f1
    t = time.time() 
    path = []
    paths = find_all_paths(dict, f1, l1)
    pprint(paths)
    costAr = []
    for r in range(0,len(paths) ):
        costAr.append(cost(paths[r]))   
    #print (costAr)
    minVal = min(costAr)
    index = costAr.index(minVal)
    print()
    print(("Distance from " +(first.upper())+ " to "+(last.upper())+" is "),minVal, 'miles' )
    print()
    print('Path is below')
    pprint(paths[index])
    print()
    print ('runtime = ', time.time() - t, ' sec')

   

rom()
