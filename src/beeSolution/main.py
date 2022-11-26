# from beeSolution.utility.loader import Loader
from swarm import *
from utility import Network
import matplotlib.pyplot as plt

DASH = 10

# loader = Loader('src/swarmSolution/data/OpM_LIB_2016/pmed17.txt.table.p25.A.txt')
# data = loader.load()
# network = Network(data)

# network = Network([
# 	[0, 7, 0 ,0, 0, 0, 4, 0, 0],
# 	[7, 0, 8, 0, 0, 6, 0, 0, 0],
# 	[0, 8, 0, 1, 4, 0, 0, 0, 0],
# 	[0, 0, 0, 1, 0, 0, 0, 0, 0],
# 	[0, 0, 4, 0, 0, 0, 3, 0, 5],
# 	[0, 6, 0, 0, 0, 0, 0, 0, 0],
# 	[4, 0, 0, 0, 3, 0, 0, 1, 0],
# 	[0, 0, 0, 0, 0, 0, 1, 0, 4],
# 	[0, 0, 0, 0, 5, 0, 0, 4, 0]
# ])
# print(network.get_conjugate_vertices(6))
# print(network.weight([0,1,2]))

network = Network.random(50, 1500)

swarm = Swarm(3, network)
swarm.agents = [
	Scout(network) for _ in range(3)
]
swarm.init()

for i in range(5):
	print('-' * DASH, i+1, 'ITERATION' , '-' * DASH)
	for _ in range(15):
		swarm.step()
	swarm.place(swarm.best_postition)
	print('Sum of distances', swarm.weight())
	print('Best position', swarm.best_postition)
	print()

print('-' * DASH, 'SUMMARY', '-' * DASH)
print('Best position', swarm.best_postition)
print('Distances', swarm.network.getDistanceList(swarm.best_postition))
print('Sum of distances', swarm.weight())
