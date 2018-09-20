import queue as q
from pythonds.basic.stack import Stack

def findEnterAndExit(dict):
    for pos, val in dict:
        if val == 'E':
            entry = pos
        if val == 'X':
            exit = pos
    return entry, exit


def drawMaze(mz):
    for i in range(10):
        line = ""
        for j in range(10):
            line = line + mz[i][j] + " "
        print(line)

    # for pos, val in mz:
    #     if pos[1] == 0:
    #         print('\n' + val)
    #     else:
    #         print(val)
    #     pass

def main():
    dir = input("Enter the directory of the maze.txt file please: ")
    testDir = "C:\\Users\\Dakota\\Desktop\\maze.txt"
    rows = 10
    queue = q.deque()
    stack = Stack()
    columns = 10
    maze2d = [[0]*rows]*columns
    # while line in open(testDir):
    #     pass
    # for i in range(10):
    #     for j in range(10):
    #         maze[i][j] =
    #

    maze = {}
    lines = [line.rstrip('\n') for line in open(testDir)]
    # content = open(testDir).read().
    i = 0
    for line in lines:
        maze[i] = line
        i += 1
    # entry, exit = findEnterAndExit(maze)
    # for coord, value in maze.getItems():
    #     if coord < 10:
    #         coordy = "0"+coord
    #         maze[coordy] = value
    #     pass

    entry, exit = findEnterAndExit(maze)
    drawMaze(maze)


if __name__ == "__main__":
    main()
    pass



class Node:
    def __init__(self, value, ):
        self.element = value
        self.nextEl = None
