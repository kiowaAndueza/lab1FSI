# Search methods

#FICHERO QUE INVOCA A LOS OTROS 2 FICH

import search

ab = search.GPSProblem('A', 'B', search.romania)
print("-----------------------------TRAYECTO DE ARAD-BUCHAREST------------------------------------------")
print("------------ALGORITMO DE AMPLITUD------------------")
print(search.breadth_first_graph_search(ab).path()) #EXPANSION POR NIVELES/ O DE AMPLITUD
print("------------ALGORITMO DE PROFUNDIDAD------------------")
print(search.depth_first_graph_search(ab).path()) #EXPANSION EN PROFUNDIDAD
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN------------------")
print(search.branch_and_bound_search(ab).path()) #EXPANSION DE RAMIFICACION Y ACOTACION
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACION------------------")
print(search.branch_and_bound_with_underestimation_search(ab).path()) #EXPANSION DE ACOTACION Y RAMIFICACION CON SUBESTIMACION*/


oe = search.GPSProblem('O', 'E', search.romania)
print("-----------------------------TRAYECTO DE ORADEA-EFORIE------------------------------------------")
print("------------ALGORITMO DE AMPLITUD------------------")
print(search.breadth_first_graph_search(oe).path())
print("------------ALGORITMO DE PROFUNDIDAD------------------")
print(search.depth_first_graph_search(oe).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN------------------")
print(search.branch_and_bound_search(oe).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACION------------------")
print(search.branch_and_bound_with_underestimation_search(oe).path())


gz = search.GPSProblem('G', 'Z', search.romania)
print("-----------------------------TRAYECTO DE GIURGIU-ZERIND------------------------------------------")
print("------------ALGORITMO DE AMPLITUD------------------")
print(search.breadth_first_graph_search(gz).path())
print("------------ALGORITMO DE PROFUNDIDAD------------------")
print(search.depth_first_graph_search(gz).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN------------------")
print(search.branch_and_bound_search(gz).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACION------------------")
print(search.branch_and_bound_with_underestimation_search(gz).path())


nd = search.GPSProblem('N', 'D', search.romania)
print("-----------------------------TRAYECTO DE NEAMT-DOBRETA------------------------------------------")
print("------------ALGORITMO DE AMPLITUD------------------")
print(search.breadth_first_graph_search(nd).path())
print("------------ALGORITMO DE PROFUNDIDAD------------------")
print(search.depth_first_graph_search(nd).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN------------------")
print(search.branch_and_bound_search(nd).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACION------------------")
print(search.branch_and_bound_with_underestimation_search(nd).path())



mf = search.GPSProblem('M', 'F', search.romania)
print("-----------------------------TRAYECTO DE MEHADIA-FAGARAS------------------------------------------")
print("------------ALGORITMO DE AMPLITUD------------------")
print(search.breadth_first_graph_search(mf).path())
print("------------ALGORITMO DE PROFUNDIDAD------------------")
print(search.depth_first_graph_search(mf).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN------------------")
print(search.branch_and_bound_search(mf).path())
print("------------ALGORITMO DE RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACION------------------")
print(search.branch_and_bound_with_underestimation_search(mf).path())