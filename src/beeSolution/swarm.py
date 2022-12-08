from utility import Network
from random import choice, randint, shuffle


class Agent:
	def __init__(self, network: Network, **kwargs):
		self.network = network
		self.pos = -1
		self.kwargs = kwargs

	def init(self, pos: int):
		pass

	def rotation(self):
		ATTRACTION = self.kwargs.get('attraction', 10)

		verties = self.network.get_conjugate_vertices(self.pos)
		sorted_verties = sorted(verties, key=lambda x: x.weight)
		valid_attraction = min(ATTRACTION, len(sorted_verties))
		closest_ind = randint(1, valid_attraction)
		newPos = sorted_verties[closest_ind]
		self.pos = newPos.n

	def iter_init(self):
		pass

	def step(self):
		pass


class Scout(Agent):

	def iter_init(self):
		verties = self.network.get_conjugate_vertices(self.pos)
		newPos = choice(verties)
		self.pos = newPos.n
	
	def step(self):
		self.rotation

class Seeker(Agent):

	def step(self):
		self.rotation

class Swarm:
	DASH = 10
	agents: list[Agent]
	visited: set[int] = set()
	visited_hist: list[int] = []

	def __init__(self, p: int, network: Network, scout_c = 0.5, **kwargs):
		self.p = p
		self.DASH = kwargs.get('dash', 10)

		scout_number = int(p * scout_c)
		seeker_number = p - scout_number
		self.scouts = [Scout(network, **kwargs) for _ in range(scout_number)]
		self.seekers = [Seeker(network, **kwargs) for _ in range(seeker_number)]
		self.agents = self.scouts + self.seekers  # type: ignore


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
		shuffle(position)
		for pos, agent in zip(position, self.agents):
			agent.pos = pos

	def iter_init(self):
		for agent in self.agents:
			agent.iter_init()

	def step(self):
		for agent in self.agents:
			agent.step()
		
		weight = self.weight()
		if weight < self.best_weight:
			self.best_weight = weight
			self.best_postition = [a.pos for a in self.agents]

	def run(self, iters: int, steps: int, verbose=True):
		weights: list[int] = []

		for i in range(iters):
			if verbose:
				print('-' * self.DASH, i+1, 'ITERATION' , '-' * self.DASH)

			self.iter_init()
			for _ in range(steps):
				self.step()
				for agent in self.agents:
					self.visited.add(agent.pos)
					self.visited_hist.append(len(self.visited))
			self.place(self.best_postition)

			weight = self.weight()
			weights.append(weight)

			if verbose:
				print('Sum of distances', weight)
				print('Best position', self.best_postition)
				print()

		if verbose:
			print('-' * self.DASH, 'SUMMARY', '-' * self.DASH)
			print('Best position', self.best_postition)
			print('Distances', self.network.getDistanceList(self.best_postition))
			print('Sum of distances', self.weight())

		return (self.weight(), self.best_postition, weights, self.visited_hist)

