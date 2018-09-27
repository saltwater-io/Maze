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


# Class for structure node builder for each state in maze
# Holds position in maze I.E 60 would be the entry 'E' for the maze

class Node(NodeMixin):
    position = ''
    value = ''
    path = []

    def __init__(self, pos, val, path, parent=None):
        super(Node, self).__init__()
        self.position = pos
        self.value = val
        self.path = path
        self.parent = parent


# Generic stack: code taken from http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html
# Im using this stack as opposed to the prebuilt one because this code is much cleaner
class Stack:
    def __init__(self):  # initial constructor
        self.items = []

    def isEmpty(self):  # is stack empty?
        return self.items == []

    def push(self, item):  # Pushes item onto stack
        self.items.append(item)

    def pop(self):  # Pops item off stack
        return self.items.pop()

    def peek(self):  # Peeks at the last value added to stack
        return self.items[len(self.items) - 1]

    def size(self):  # Returns size of stack
        return len(self.items)


# This function receives the maze as a 2d-array and returns the entry and exit locations.
def findEnterAndExit(maze):
    for i in range(10):  # i = column #, j = row
        for j in range(10):
            if maze[i][j] == 'E':
                entry = str(i) + str(j)  # Entry to maze
            if maze[i][j] == 'X':
                exit = str(i) + str(j)  # Exit of maze
    return entry, exit


# walks through maze using a queue
def WalkQueue(entry, exit, maze):
    # queue to hold the successors of each node in the maze
    queue = deque([])

    # list that holds all nodes visited.
    traveledNodes = []
    # walkedPath = []
    childNodes = []
    traveledNodes.append(entry)
    # Creates initial node at position containing value 'E'
    node = Node(entry, getValue(entry, maze), traveledNodes)
    queue.append(node)  # Adds node to queue

    # Loops checks to see if the node position at the front of the quqeue is goal state is reached (value = 'X')
    # If not, continue walking.
    position = queue.popleft().value
    while str(position) != exit:
        # Grabs the children of node
        children = getChildren(node, maze)
        if not children:
            pass
        else:
            for pos in children:
                if pos in traveledNodes:
                    pass
                else:
                    traveledNodes.append(pos)
                    newNode = Node(pos, getValue(pos, maze), node.ancestors, parent=node)
                    childNodes.append(newNode)
            for child in childNodes:
                queue.append(child)
            childNodes.clear()
            node = queue.popleft()
            position = node.position
            FINAL_PATH = []
            if position == exit:
                for ancestor in node.ancestors:
                    FINAL_PATH.append(ancestor.position)
                FINAL_PATH.append(position)
                printPath(FINAL_PATH)




# Walks through maze using a stack LIFO
def WalkStack(entry, exit, maze):
    stack = Stack()
    traveledNodes = []
    childNodes = []
    traveledNodes.append(entry)
    node = Node(entry, maze[int(entry[0])][int(entry[1])], traveledNodes)
    stack.push(node)
    position = stack.pop()
    while str(position) != exit:
        children = getChildren(node, maze)
        if not children:
            # node = stack.pop()
            # children = getChildren()
            pass
        else:
            for pos in children:
                if pos in traveledNodes:
                    pass
                else:
                    traveledNodes.append(pos)
                    newNode = Node(pos, getValue(pos, maze), node.ancestors, parent=node)
                    childNodes.append(newNode)
            for child in childNodes:
                stack.push(child)
            childNodes.clear()
            node = stack.pop()
            position = node.position
            FINAL_PATH = []
            if position == exit:
                for ancestor in node.ancestors:
                    FINAL_PATH.append(ancestor.position)
                FINAL_PATH.append(position)
                printPath(FINAL_PATH)


def getChildren(node, maze):
    children = []
    r = int(node.position[0])
    c = int(node.position[1])
    if (r != 0) and maze[r + 1][c] == 'P' or maze[r + 1][c] == 'X':
        children.append(str(r + 1) + str(c))
    if (r != 9) and maze[r - 1][c] == 'P' or maze[r - 1][c] == 'X':
        children.append(str(r - 1) + str(c))
    if (c != 0) and maze[r][c - 1] == 'P' or maze[r][c - 1] == 'X':
        children.append(str(r) + str(c - 1))
    if (c != 9) and maze[r][c + 1] == 'P' or maze[r][c + 1] == 'X':
        children.append(str(r) + str(c + 1))
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


def printPath(path):
    walkedPath = ''
    for pos in path:
        walkedPath = walkedPath + " " + pos
    print(walkedPath)

#Main function runs the program:
# Please note that the maze.txt file and this file must be in the SAME directory.
# Thanks!
def main():
    #grabs absolute path of
    my_path = os.path.abspath(os.path.dirname(__file__)) #
    file = open(my_path + "\\maze.txt", 'r')

    lines = file.readlines()

    maze2d = ['0'] * 10
    for g in range(10):
        maze2d[g] = ['0'] * 10
    z = 0
    for i in range(10):
        for j in range(10):
            maze2d[i][j] = lines[z].rstrip('\n')
            z += 1
    drawMaze(maze2d)
    entry, exit = findEnterAndExit(maze2d)
    print("")
    print("Breath first search: ")
    WalkQueue(entry, exit, maze2d)

    print("")
    print("Depth first search: ")
    WalkStack(entry, exit, maze2d)


if __name__ == "__main__":
    main()
    pass
