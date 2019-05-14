#You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

def path_finder(a):
    #puts matrix values in string
    matrix = list(map(list, a.splitlines()))
    #length of matrix
    length = len(matrix)
    #start and end point
    s = (0,0)
    t = (length - 1,length - 1)
    #memoization / hash 
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s] #spaces in level 
    while frontier:
        next = []
        for u in frontier: #u is the spaces, the node
            #assigns coordinates to nodes in frontier
            x,y = u
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length: #out of range
                    #if you cant move in level
                    if (x,y) not in level and matrix[x][y] != 'W':
                        #if can't move within level #W is wall
                        level[(x,y)] = i
                        parent[(x,y)] = u
                        next.append((x,y))
                        if (x,y) == t:
                            return level[(x,y)]
                                #list of past nodes
        frontier = next
        i += 1
    return False
