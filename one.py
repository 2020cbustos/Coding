def BFS(start,maze):
    queue = [start]
    explored = []
    #while something in queue, keep looking
    while queue:
        next = queue.pop # "pop" takes from the end (first in first out)
        #get nodes connected to our edge
        edges = find_edges(next, maze)
        #loop thorugh all connecting nodes
        for edge in edges:
            if edge not in explored:
            queue.append(edges)
return explored

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        #find connecting nodes
            #check if connecting nodes are explored
            #add conneting nodes to level, parent, and next
        for u in frontier:
            x,y = u
        frontier = next
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
              explored.append(node)
              # find connections
              # add connections to frontier
              edges = find_edges(matrix, node)
              for edge in edges:
                new_path = list(path)
                new_path.append(edge)
                queue.append(new_path)
                if edge == t: # check if a connection is A[-1]B[-1]
                    return True
