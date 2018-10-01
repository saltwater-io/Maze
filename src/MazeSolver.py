# This code receives text input of a maze, builds the maze,
# and then steps through using breath-first search (queue),
# as well as Depth-First Search (stack).
#
# It was developed for AI programming at the University of Southern Mississippi
#
# Written by Dakota McGuire 9/26/18

import os
from anytree import NodeMixin
from _collections import deque


# Class for structure node builder for each state in maze
# Holds position in maze I.E 60 would be the entry 'E' for the maze
class Node(NodeMixin):
    position = ''
    value = ''
    path = []
    # Prebuilt constructor for the nodes at the each state
    def __init__(self, pos, val, path, parent=None):
        super(Node, self).__init__()
        self.position = pos
        self.value = val
        self.path = path
        self.parent = parent


# Generic stack: code taken from http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html
# Im using this stack as opposed to the precompiled imported one because this code is much cleaner
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


# This function receives the maze as a 2d-array and returns the entry location.
def findEntryOfMaze(maze):
    for i in range(10):  # i = column #, j = row
        for j in range(10):
            if maze[i][j] == 'E':
                entry = str(i) + str(j)  # Entry to maze
    return entry


# Function walks through maze using a queue,
# Receives the entry and exit positions,
# As well as the maze as parameters
def WalkQueue(entry, maze):

    # queue to hold the successors of each node in the maze
    queue = deque([])

    # list that holds all nodes visited.
    traveledNodes = []
    traveledNodes.append(entry)  # Entry stored

    # list to hold all child nodes of a given state
    childNodes = []

    # Creates initial node at entry position containing value 'E'
    node = Node(entry, getValue(entry, maze), traveledNodes)

    queue.append(node)  # Adds node to queue

    value = node.value  # Value is the maze value of the maze('E', 'P', 'X')
    
    # Loop checks to see if the node at the front of the queue
    # is goal state e.g. (the node's value = 'X')
    # If not, continue walking.
    while str(value) != 'X':
        # Grabs the children of node
        children = getChildren(node, maze)
        if not children:  # Checks to see if any children exist
            print("No solution! :(")
        else:  # if children do exists:
            for pos in children:  # Loops through each child/position in children
                if pos in traveledNodes:  # Checks if position has been visited
                    pass
                else:  # if position is fresh
                    traveledNodes.append(pos)  # Drops position into traveled nodes
                    newNode = Node(pos, getValue(pos, maze), node.ancestors, parent=node)  # Creates new node
                    childNodes.append(newNode)  # Throws the new node into the list of child nodes

            for child in childNodes:  # Drops each child node into the queue for further processing
                queue.append(child)

            childNodes.clear()  # Clears the children for next set of child nodes

            node = queue.popleft()  # Gets next node in queue
            value = node.value  # Grabs current state's maze value

            FINAL_PATH = []  # List of the of path from start to finish

            if value == 'X':  # Checks if current position state is indeed the goal state
                for ancestor in node.ancestors:  # Gets the parent of each node
                    FINAL_PATH.append(ancestor.position)  # adds their respective positions to the the final path

                FINAL_PATH.append(node.position)  # Adds final goal state position to the final path
                printPath(FINAL_PATH)  # Prints the walked path


# Walks through maze using a stack LIFO
def WalkStack(entry, maze):

    stack = Stack()  # Stack LIFO

    # list that holds all nodes visited.
    traveledNodes = []
    traveledNodes.append(entry)  # Entry stored

    # list to hold all child nodes of a given state
    childNodes = []

    # Creates initial node at entry position containing value 'E'
    node = Node(entry, getValue(entry, maze), traveledNodes)

    stack.push(node)  # Adds node to queue
    node = stack.pop()

    value = node.value  # Value is the maze value of the maze('E', 'P', 'X')

    # Loop checks to see if the node at the front of the stack
    # is goal state e.g. (the node's value = 'X')
    # If not, continue walking.
    while str(value) != 'X':
        # Grabs the children of node
        children = getChildren(node, maze)
        if not children:  # Checks to see if any children exist
            print("No solution! :(")
        else:  # if children do exists:
            for pos in children:  # Loops through each child/position in children
                if pos in traveledNodes:  # Checks if position has been visited
                    pass
                else:  # if position is fresh
                    traveledNodes.append(pos)  # Drops position into traveled nodes
                    newNode = Node(pos, getValue(pos, maze), node.ancestors, parent=node)  # Creates new node
                    childNodes.append(newNode)  # Throws the new node into the list of child nodes

            for child in childNodes:  # Drops each child node into the stack for further processing
                stack.push(child)

            childNodes.clear()  # Clears the children for next set of child nodes

            node = stack.pop()  # Gets next node in queue

            value = node.value # Grabs current state's maze value

            FINAL_PATH = []  # List of the of path from start to finish

            if value == 'X':  # Checks if current position state is indeed the goal state
                for ancestor in node.ancestors:  # Gets the parent of each node
                    FINAL_PATH.append(ancestor.position)  # adds their respective positions to the the final path

                FINAL_PATH.append(node.position)  # Adds final goal state position to the final path
                printPath(FINAL_PATH)  # Prints the walked path

# Gets child node positions of the current state
# Takes the maze and current state as parameters
# Returns a list of positions of valid children from current state
def getChildren(node, maze):
    children = []  # List of children
    r = int(node.position[0])  # Row
    c = int(node.position[1])  # Column

    # If not top row, check value of position directly above current state
    if (r != 0) and maze[r + 1][c] == 'P' or maze[r + 1][c] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r + 1) + str(c))

    # If column is not farthest left column, check value of position directly left of current state
    if (c != 0) and maze[r][c - 1] == 'P' or maze[r][c - 1] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r) + str(c - 1))

    # If not bottom row, check value of position directly to the bottom of current state
    if (r != 9) and maze[r - 1][c] == 'P' or maze[r - 1][c] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r - 1) + str(c))

    # If column is not farthest right column, check value of position directly right of current state
    if (c != 9) and maze[r][c + 1] == 'P' or maze[r][c + 1] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r) + str(c + 1))

    return children


# Function returns the value of the maze at a position
def getValue(pos, mz):
    # pos[0] = row, pos[1] = column
    return mz[int(pos[0])][int(pos[1])]


# Draws the maze in a correct and readable format
def drawMaze(mz):
    for i in range(10):  # For each row,
        line = ""        # Create a line
        for j in range(10):
            line = line + mz[i][j] + " "  # Put data located at the position into the line
        print(line)  # Print line

# Prints the path of a list in correct format
def printPath(path):
    walkedPath = ""
    for pos in path:  # Adds each position visited in the path to a single sting to be displayed
        walkedPath = walkedPath + " " + pos  #
    print(walkedPath)


# Main function runs the program:
# Please note that the maze.txt file and this file must be in the SAME directory.
# Thanks!
def main():
    # grabs absolute path of the current location of this file
    my_path = os.path.abspath(os.path.dirname(__file__))
    file = open(my_path + "\\maze.txt", 'r')  #Opens maze.txt file as file

    lines = file.readlines()  # Reads lines from a file and returns a list containing each line

    maze = ['0'] * 10  # Builds initial 1-d maze array maze with length 10

    for g in range(10):  # For each index of maze,
        maze[g] = ['0'] * 10  # Another array of length 10 is inserted.

    z = 0  # Z = index used for data stored inside line list

    for i in range(10):  # Initial indexing i = row
        for j in range(10):  # 2d Indexing j = column
            maze[i][j] = lines[z].rstrip('\n')  # This for loop adds the value at index 'Z',
            z += 1                              # Of the lines list into its corresponding index in the 2-d Maze Array

    drawMaze(maze)  # Draws maze

    entry = findEntryOfMaze(maze)  # Maze entry and exit

    print("")  # Output formatting
    print("Breath first search: ")

    WalkQueue(entry, maze)  # Walks through maze with queue (FIFO)

    print("")  # Output formatting
    print("Depth first search: ")

    WalkStack(entry, maze)  # Walks through maze with a stack (LIFO)


if __name__ == "__main__":  # Start
    main()