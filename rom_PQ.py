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
    if stype == 'Uniform Cost':
  print ('Uniform Cost')
  start=raw_input('Starting City: ')
  target=raw_input('Ending City: ')
  city = start
  queue = [[0, start]]
  boolean = 0
  tic = time()
  toc = 0
  distance = 0
  masterlist = []
  while boolean == 0:
    slist = queue.pop(0)
    print '***',slist
    city = slist.pop()
    index1 = cityNames.index(city)
    edge1 = edgeList[index1]
    neighbors=findnbrs(city, nlist2)
    slist.append(city)
    while len(neighbors) != 0:
      looplist = slist[:]
      value = neighbors.pop(0)
      index2 = cityNames.index(value)
      edge2 = edgeList[index2]
      if value not in masterlist:
	masterlist.append(value)
	if value == target:
	  boolean = 1
	  d = distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY())
	  looplist[0] = looplist[0] + d
	  looplist.append(value)
	  queue.append(looplist)
	  queue.sort()
	  toc = time()
	  print looplist
	  print toc - tic
	if value not in looplist and value != target and looplist not in queue:
	  d = distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY())
	  looplist[0] = looplist[0] + d
	  looplist.append(value)
	  queue.append(looplist)
	  queue.sort()


   

rom()
