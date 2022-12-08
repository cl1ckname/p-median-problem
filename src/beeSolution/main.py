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

network = Network.random(1000, 100000)

swarm = Swarm(6, network, 0.5, attraction=30)
swarm.init()

_, _, weights = swarm.run(1000, 25, False)


plt.grid()
plt.plot(weights)

plt.show()