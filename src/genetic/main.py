from utility import Network, SolutionRunner
from genepool import GenePool

network = Network.random(200, 15000)

gp = GenePool(5, network, 200)
sol = SolutionRunner(gp)
sol.run(100, 5)