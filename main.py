from pythonds.basic.stack import Stack
from _collections import deque
from src import node as n

def findEnterAndExit(maze):
    for i in range(10):
        for j in range(10):
            if maze[i][j] == 'E':
                entry = str(i)+str(j)
            if maze[i][j] == 'X':
                exit = str(i)+str(j)
    return entry, exit


# walks through maze using a queue
def WalkQueue(entry, exit, maze):
    queue = deque([])
    traveledNodes = []
    traveledNodes.append(entry)
    node = n.Node(entry, getValue(entry), traveledNodes)
    queue.append(node)
    while str(queue.popleft().position) != exit:
        children = getChildren(node, maze)
        if not children:
            pass
        else:
            for pos in children:
                if pos in traveledNodes:
                    pass
                else:
                    traveledNodes.append(pos)
                    newNode = n.Node(pos, getValue(pos,maze), traveledNodes, parent=node)
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
        node = n.Node(entry, maze[int(entry[0])][int(entry[1])], traveledNodes)
        stack.push(node)
        while str(stack.pop().position) != exit:
            children = getChildren(node, maze)
            if not children:
                stack.pop()
            else:
                for pos in children:
                    if pos in traveledNodes:
                        pass
                    else:
                        traveledNodes.append(pos)
                        newNode = n.Node(pos, getValue(pos, maze), traveledNodes, parent=node)
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
    if (r !=9) and maze[r-1][c] == 'P' or maze[r-1][c] == 'X':
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
    # dir = input("Enter the directory of the maze.txt file please: ")
    testDir = "C:\\Users\\Dakota\\Desktop\\maze.txt"
    testRes = "C:\\Users\\dmcguire\\PycharmProjects\\ai\\resources\\maze.txt"
    lines = open(testRes, 'r').readlines()
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
    # WalkQueue(entry, exit, maze2d)

    print("Depth first search: ")
    WalkStack(entry, exit, maze2d)


if __name__ == "__main__":
    main()
    pass


