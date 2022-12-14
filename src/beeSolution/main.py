from swarm import *
from utility import Network, SolutionRunner

DASH = 10

network = Network.random(200, 15000)

swarm = Swarm(6, network, 0.5, attraction=10)

sol = SolutionRunner(swarm)
sol.run(200, 20)