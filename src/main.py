# This code receives text input of a maze, builds the maze,
# and then steps through using breath-first search (queue),
# aswell as Depth-First Search (stack).
#
# It was developed for AI programming at the University of Southern Mississippi
#
# Written by Dakota McGuire 9/26/18
import os

from anytree import NodeMixin
# from pythonds.basic.stack import Stack
from _collections import deque
# from src import node as n


# Structure node builder for each state in maze
class Node(NodeMixin):
    position = ''
    value = ''
    path = []
    parent = ''

    def __init__(self, pos, val, path, parent=None):
        super(Node, self).__init__()
        self.position = pos
        self.value = val
        self.path = path
        self.parent = parent


# Generic stack:
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# This function receives the maze as a 2d-array and returns the entry and exit locations.
def findEnterAndExit(maze):

    for i in range(10): #  i = column #, j = row
        for j in range(10):
            if maze[i][j] == 'E':
                entry = str(i)+str(j)
            if maze[i][j] == 'X':
                exit = str(i)+str(j)
    return entry, exit


# walks through maze using a queue
def WalkQueue(entry, exit, maze):
    # queue to hold the successors of each node in the maze
    queue = deque([])

    # list that holds all nodes visited.
    traveledNodes = []
    traveledNodes.append(entry)

    # Creates initial node at position containing value 'E'
    node = Node(entry, getValue(entry, maze), traveledNodes)
    queue.append(node) #Adds node to queue

    # Loops checks to see if the node position at the front of the quqeue is goal state is reached (value = 'X')
    # If not, continue walking.
    while str(queue.popleft().position) != exit:
        # Grabs the children of node
        children = getChildren(node, maze)
        if not children:
            node = queue.popleft()
            children = getChildren(node, maze)
            for pos in children:
                if pos in traveledNodes:
                    pass
                else:
                    traveledNodes.append(pos)
                    newNode = Node(pos, getValue(pos ,maze), traveledNodes, parent=node)
                    node = newNode
                    queue.append(node)
            pass
        else:
            for pos in children:
                if pos in traveledNodes:
                    pass
                else:
                    traveledNodes.append(pos)
                    newNode = Node(pos, getValue(pos,maze), traveledNodes, parent=node)
                    node = newNode
                    queue.append(node)
    walkedPath = queue.popleft().path
    FINAL_PATH = ""
    for loc in walkedPath:
        FINAL_PATH = FINAL_PATH + loc + " "
    print(traveledNodes)
    print(FINAL_PATH)

#Walks through maze using a stack LIFO
def WalkStack(entry, exit, maze):
        stack = Stack()
        traveledNodes = []
        traveledNodes.append(entry)
        node = Node(entry, maze[int(entry[0])][int(entry[1])], traveledNodes)
        stack.push(node)
        while str(stack.pop().position) != exit:
            children = getChildren(node, maze)
            if not children:
                node = stack.pop()
                children = getChildren()
                for pos in children:
                    if pos in traveledNodes:
                        pass
                    else:
                        paths = node.path.add(pos)
                        traveledNodes.append(pos)
                        newNode = Node(pos, getValue(pos, maze), paths, parent=node)
                        node = newNode
                        stack.push(node)

            else:
                for pos in children:
                    if pos in traveledNodes:
                        pass
                    else:
                        traveledNodes.append(pos)
                        newNode = Node(pos, getValue(pos, maze), traveledNodes, parent=node)
                        node = newNode
                        stack.push(node)

        FINAL_PATH = ""
        while stack.isEmpty() != True:
            FINAL_PATH = FINAL_PATH + stack.pop().location + " "
        print(traveledNodes)
        print(FINAL_PATH)

def getChildren(node, maze):
    children = []
    r = int(node.position[0])
    c = int(node.position[1])
    if (r != 0) and maze[r+1][c] == 'P' or maze[r+1][c] == 'X':
        children.append(str(r + 1) + str(c))
    if (r != 9) and maze[r-1][c] == 'P' or maze[r-1][c] == 'X':
        children.append(str(r-1) + str(c))
    if (c != 0) and maze[r][ -1] == 'P' or maze[r][c-1] == 'X':
        children.append(str(r) + str(c-1))
    if (c != 9) and maze[r][c+1] == 'P' or maze[r][c+1] == 'X':
        children.append(str(r) + str(c+1))
    return children

def getValue(pos, mz):
    return mz[int(pos[0])][int(pos[1])]

# Draws the maze
def drawMaze(mz):
    for i in range(10):
        line = ""
        for j in range(10):
            line = line + mz[i][j] + " "
        print(line)



def main():
    # dir = input("Enter the path/directory of the maze.txt file please: ")
    my_path = os.path.abspath(os.path.dirname(__file__))
    file = open(my_path+"\\maze.txt", 'r')
    # data_folder = Path("/relative/path")
    # file_to_open = data_folder / "maze.txt"
    # while(dir.endswith("maze.txt") != True):
    #     dir = input("Enter the directory of the maze.txt file please: ")
    lines = file.readlines()
    # open(dir, 'r')
    testDir = "C:\\Users\\Dakota\\Desktop\\maze.txt"
    testRes = "C:\\Users\\dmcguire\\PycharmProjects\\ai\\resources\\maze.txt"
    maze2d = ['0']*10
    for g in range(10):
        maze2d[g] = ['0']*10
    z = 0
    for i in range(10):
        for j in range(10):
            maze2d[i][j] = lines[z].rstrip('\n')
            z += 1
    drawMaze(maze2d)
    entry, exit = findEnterAndExit(maze2d)

    print("Breath first search: ")
    WalkQueue(entry, exit, maze2d)

    print("Depth first search: ")
    # WalkStack(entry, exit, maze2d)


if __name__ == "__main__":
    main()
    pass


