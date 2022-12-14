from utility import Network
from random import randint, choice, choices
from heapq import nsmallest
from utility import Solution, StepData

class Individual:
	def __init__(self, network: Network, init: list[int]) -> None:
		self.network = network
		self.positions = list(init)
		self.weight = self.network.weight(self.positions)
		self.p = len(init)

	def __add__(self, i: 'Individual'):
		newPosition = [choice(i) for i in zip(i.positions, self.positions)]
		return Individual(self.network, newPosition[:self.p])
	
	def mutate(self):
		self.positions[randint(0, self.p-1)] = self.network.randomNode()

	@staticmethod
	def random(network: Network, p: int):
		return Individual(network, [randint(0, len(network)-1) for _ in range(p)])

	def __str__(self) -> str:
		return f'Individual[position: {self.positions}, weight: {self.weight}]'


class GenePool(Solution):
	pool: list[Individual]
	parentProbs: list[float]

	def __init__(self, p: int, network: Network, populationSize: int):
		self.populationSize = populationSize
		self.p = p
		self.network = network

		self.pool = [Individual.random(self.network, p) for _ in range(populationSize)]
		self.calculateParentProps()

	def calculateParentProps(self):
		parentWeights = [i.weight for i in self.pool]
		normilizeMul = 1 / sum(parentWeights)
		self.parentPorbs = [w * normilizeMul for w in parentWeights]

	def getChilds(self):
		childs: list[Individual] = []
		for _ in range(self.populationSize * 2):
			parent1, parent2 = choices(self.pool, k=2, weights=self.parentPorbs)
			child = parent1 + parent2
			childs.append(child)
		return nsmallest(self.populationSize, childs, key=lambda c: c.weight)

	def mutate(self):
		for i in range(int(self.populationSize * 0.5)):
			ind = self.pool[i]
			ind.mutate()

	def best(self):
		bestI = self.parentPorbs.index(max(self.parentPorbs))
		return self.pool[bestI]

	def init(self):
		pass

	def iter_init(self):
		pass

	def after_init(self):
		pass

	def step(self):
		childs = self.getChilds()
		self.pool = childs
		self.mutate()
		self.calculateParentProps()
		localBest = self.best()
		return StepData(localBest.weight, localBest.positions)

	def run(self, iters: int, steps: int, verbose=True):
		bestIndivid = self.best()
		print('Start', bestIndivid)

		for i in range(iters):
			# if verbose:
			# 	print(f'=============Iter {i}=============')

			for _ in range(steps):
				childs = self.getChilds()
				self.pool = childs
				self.mutate()
				self.calculateParentProps()
			localBest = self.best()
			print(f'Local best {localBest}')
			if localBest.weight < bestIndivid.weight:
				bestIndivid = localBest
				print('New Best', bestIndivid)
			# print(f'==============CurrentBestWeight {bestIndivid.weight}===================')

		return bestIndivid


			