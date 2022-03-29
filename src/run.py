# Search methods

#FICHERO QUE INVOCA A LOS OTROS 2 FICH

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path()) #EXPANSION POR NIVELES/ O DE AMPLITUD
print(search.depth_first_graph_search(ab).path()) #EXPANSION EN PROFUNDIDAD
print(search.branch_and_bound_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
