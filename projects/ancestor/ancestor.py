''' Find the earliest ancestor of a node '''
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    ''' Input: list of ancestor tuples and a starting point.
    First value in tuple is the parent, remainder are children.
    Output: longest graph path from given starting node. '''
    # make a list of verts for later traversal
    vert = list(set([y for x in ancestors for y in x]))

    # build a graph
    g = Graph()

    for tup in ancestors:
        #        print("t ", tup)
        #        vert.append(tup)
        parent = tup[0]
#        print(parent)
        child = tup[1]
#        print(child)
        g.add_vertex(parent)
#        print("add parent: ", g.vertices)
        g.add_vertex(child)
#        print("add child ", g.vertices)
#    for tup in ancestors:
        g.add_edge(child, parent)
#        print("added edge ", g.vertices)
#    print(g.vertices)
    paths = []
#    print(set(vert))
    for vertex in vert:
        if vertex != starting_node and g.dfs(starting_node, vertex):
            paths.append(g.dfs(starting_node, vertex))
    if len(paths) < 1:
        return -1
    else:
        return max(paths, key=len)[-1]
#    print(paths)


if __name__ == '__main__':
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                 (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(ancestors, 6))
