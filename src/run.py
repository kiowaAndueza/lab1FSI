# Search methods

#FICHERO QUE INVOCA A LOS OTROS 2 FICH

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("------------ALGORITMO DE AMPLITUD------------------")
print(search.breadth_first_graph_search(ab).path()) #EXPANSION POR NIVELES/ O DE AMPLITUD

print("------------ALGORITMO DE PROFUNDIDAD------------------")
print(search.depth_first_graph_search(ab).path()) #EXPANSION EN PROFUNDIDAD

print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN------------------")
print(search.branch_and_bound_search(ab).path()) #EXPANSION DE RAMIFICACION Y ACOTACION

print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACION------------------")
print(search.branch_and_bound_with_underestimation_search(ab).path()) #EXPANSION DE ACOTACION Y RAMIFICACION CON SUBESTIMACION*/

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
