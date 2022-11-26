from utility import Network
from random import choice, randint


class Agent:
	def __init__(self, network: Network):
		self.network = network
		self.pos = -1

	def init(self, pos: int):
		pass

	def step(self):
		pass

class Scout(Agent):

	def step(self):
		verties = self.network.get_conjugate_vertices(self.pos)
		newPos = choice(verties)
		self.pos = newPos.n

class Seeker(Agent):
	ATTRACTION = 8

	def step(self):
		verties = self.network.get_conjugate_vertices(self.pos)
		sorted_verties = sorted(verties, key=lambda x: x.weight)
		closest_ind = randint(1, self.ATTRACTION)
		newPos = sorted_verties[closest_ind]
		self.pos = newPos.n

class Swarm:
	agents: list[Agent]
	def __init__(self, p: int, network: Network):
		self.p = p
		self.agents = []
		self.network = network
		self.best_postition: list[int] = [-1] * p
		self.best_weight: float = float('inf')


	def weight(self):
		positions = [i.pos for i in self.agents]
		return self.network.weight(positions)

	def init(self):
		initial_position = [randint(0, len(self.network) -1) for _ in range(self.p)]
		self.best_postition = initial_position
		self.place(initial_position)

	def place(self, position: list[int]):
		assert len(position) == self.p
		for pos, agent in zip(position, self.agents):
			agent.pos = pos

	def step(self):
		for agent in self.agents:
			agent.step()
		
		weight = self.weight()
		if weight < self.best_weight:
			self.best_weight = weight
			self.best_postition = [a.pos for a in self.agents]

