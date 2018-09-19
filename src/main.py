import queue;

def findEnterAndExit(dict):
    for pos, val in dict:
        if val == 'E':
            entry = pos
        if val == 'X':
            exit = pos
    return entry, exit


def drawMaze(mz):
    i = 0
    for pos, val in mz:
        if pos[1] == 0:
            print('\n' + val)
        else:
            print(val)
        pass

def main():
    dir = input("Enter the directory of the maze.txt file please: ")
    testDir = "C:\\Users\\Dakota\\Desktop\\maze.txt"
    maze = {}
    lines = [line.rstrip('\n') for line in open(testDir)]
    # content = open(testDir).read().
    i = 0
    for line in lines:
        maze[i] = line.split()
        i += 1
    # entry, exit = findEnterAndExit(maze)
    # for coord, value in maze.getItems():
    #     if coord < 10:
    #         coordy = "0"+coord
    #         maze[coordy] = value
    #     pass
    drawMaze(maze)
    entry, exit = findEnterAndExit(maze)



if __name__ == "__main__":
    main()
    pass



# class node: