from utility import Network
from genepool import GenePool

network = Network.random(200, 15000)

gp = GenePool(5, network, 200)
bi = gp.run(100, 5)

print(bi)