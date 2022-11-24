from loader import Loader
from graph import Network

loader = Loader('src/swarm/data/OpM_LIB_2016/pmed17.txt.table.p25.A.txt')
data = loader.load()
network = Network(data)
print(network.weight())