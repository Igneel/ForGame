# Sample code from http://www.redblobgames.com/pathfinding/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

# utility functions for dealing with square grids
def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = "\u2192"
        if x2 == x1 - 1: r = "\u2190"
        if y2 == y1 + 1: r = "\u2193"
        if y2 == y1 - 1: r = "\u2191"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r

def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()

# data from main article
DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,334,343,344,373,374,403,404,433,434]]

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6), 
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6), 
                                       (5, 7), (5, 8), (6, 2), (6, 3), 
                                       (6, 4), (6, 5), (6, 6), (6, 7), 
                                       (7, 3), (7, 4), (7, 5)]}

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start) # optional
    path.reverse() # optional
    return path

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


def convert (matrix):
    newmatrix={}
    g = GridWithWeights(41, 21)
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j]=='+' or matrix[i][j]=='-' or matrix[i][j]=='|':
                newmatrix[i,j]=10000
                g.walls.append((j,i))
            else:
                newmatrix[i,j]=1
                
    return g


def genmovements(path):
    move=""
    for i in range(0,len(path)-1):
        x1,y1=path[i]
        x2,y2=path[i+1]
        dx=x2-x1
        dy=y2-y1
        if dx==0 and dy==0:
            continue
        if dx==1:
            move=move+"d"
        if dx==-1:
            move=move+"a"
        if dy==1:
            move=move+"s"
        if dy==-1:
            move=move+"w"
    return move

import telnetlib
import re
import time

HOST = "hackyou-ppc300.ctf.su"
tn=telnetlib.Telnet(HOST,port=11111)

p3= re.compile('[+][+ |O\r\n-]{899}[+]',re.IGNORECASE)
p4= re.compile('[\S ]+level[ \S]+',re.IGNORECASE)
p5= re.compile('[\S ]+flag[ \S]+',re.IGNORECASE)

levels=[]
flags=[]


dat=tn.read_until(b'+\r\n\r\n')

dat=dat.decode('utf-8')
#print('dat is:')
print(dat)
    
#dat,split
matrix=p3.findall(dat)
level=p4.findall(dat)
flag=p5.findall(dat)

if level!=[]:
    levels.append(level[len(level)-1])
if flag!=[]:
    flags.append(flag[len(flag)-1])

tn.write('\n'.encode('utf-8'))

for i in range(0,337):
    print('iteration')
    print(i)
    dat=tn.read_until(b'+\r\n\r\n')

    dat=dat.decode('utf-8')
    #print('dat is:')
    #print(dat)
    
    #dat,split
    matrix=p3.findall(dat)
    level=p4.findall(dat)
    flag=p5.findall(dat)

    if level!=[]:
        levels.append(level[len(level)-1])
    if flag!=[]:
        flags.append(flag[len(flag)-1])

    print(levels[len(levels)-1])
    print(flags[len(flags)-1])
    
    if len(matrix)==0:
        continue    
    matrix=matrix[len(matrix)-1]

    #print(matrix)
    matrix=matrix.split('\r\n')
    
    newmatrix=convert(matrix)

    startx=1
    starty=19
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j]=='O':
                startx=j
                starty=i
    print('start')
    print(startx)
    print(starty)    

    finishx=39
    finishy=1

    came_from, cost_so_far = a_star_search(newmatrix, (startx, starty), (finishx, finishy))
    #draw_grid(newmatrix, width=1, point_to=came_from, start= (startx, starty), goal=(finishx, finishy))
    #draw_grid(newmatrix, width=3, number=cost_so_far, start= (startx, starty), goal=(finishx, finishy))
    #print(came_from)
    path=reconstruct_path(came_from,start= (startx, starty), goal=(finishx, finishy))
    #print(path)
    movems=genmovements(path)
    #print(movems)
       
    for rep in range(0,len(movems)):
        #print('rep='+ str(rep)+movems[rep])
        tn.write(movems[rep].encode('utf-8')) 
        dat=tn.read_until(b'+\r\n\r\n')
        dat=dat.decode('utf-8')
        print('.', end="")
        #print(dat)
        #time.sleep(0.1)
    matrix=[]
    #tn.write('\n'.encode('utf-8'))

print(tn.read_all())
