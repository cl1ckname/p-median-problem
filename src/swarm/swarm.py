class Agent:
	def __init__(self, pos: int):
		self.pos = pos

	def step(self):
		pass



class Swarm:
	agents: list[Agent]
	def __init__(self, p: int):
		self.p = p
		self.agents = []

	def step(self):
		for agent in self.agents:
			agent.step()

