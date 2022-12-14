from abc import ABC, abstractmethod
from dataclasses import dataclass
from sys import maxsize

@dataclass
class StepData:
	bestWeight: int
	bestPositions: list[int]

class Solution(ABC):

	@abstractmethod
	def init(self):
		pass

	@abstractmethod
	def iter_init(self):
		pass

	@abstractmethod
	def after_init(self):
		pass

	@abstractmethod
	def step(self) -> StepData:
		pass

class SolutionRunner:
	DASH = 10
	def __init__(self, solution: Solution):
		self.solution = solution

	def run(self, iters: int, steps: int, verbose=2):
		if verbose > 0:
			self.fPrint('RUN', self.solution.__class__.__name__, 'SOLUTION', dashes=True)

		self.solution.init()
		globalBestWeight = maxsize
		globalBestPositions = [-1]

		for i in range(iters):
			if verbose > 1:
				self.fPrint('ITERATION', i, dashes=True)
			self.solution.iter_init()

			for _ in range(steps):
				solutionData = self.solution.step()
				if (solutionData.bestWeight < globalBestWeight):
					globalBestWeight = solutionData.bestWeight
					globalBestPositions = solutionData.bestPositions

			if verbose > 1:
				self.solution.after_init()
				self.fPrint('LOCAL BEST', globalBestWeight, globalBestPositions)

		if verbose > 0:
			self.fPrint('SUMMARY', dashes=True)
			self.fPrint('BEST WEIGHT', globalBestWeight)
			self.fPrint('BEST POSITIONS', globalBestPositions)


	def fPrint(self, *args, dashes: bool = False):
		print('-' * self.DASH * dashes, *args, '-' * self.DASH * dashes)