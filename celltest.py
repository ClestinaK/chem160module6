from ising_class import *
acell = cell(0, 3, 10) #Args: i, j, n
print(acell.cellspin())
print(acell.spin.flip()) #Reaching through cell to inner spin object
print(acell.left) #Directly accessing the neighbor indices
print(acell.right)
print(acell.up)
print(acell.down)