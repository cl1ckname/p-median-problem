from dataclasses import dataclass
from random import randint
from methodtools import lru_cache
import networkx as nx
import numpy as np

@dataclass
class NeightborData:
	n: int
	weight: float | int

class Network:
	graph: nx.DiGraph

	def __init__(self, matrix: list[list[float]] | np.ndarray | nx.DiGraph) -> None:
		if isinstance(matrix, nx.DiGraph):
			self.graph = matrix
			return
		if isinstance(matrix, list):
			matrix = np.array(matrix)
		self.graph: nx.DiGraph = nx.from_numpy_matrix(matrix)

	@lru_cache()
	def bellman(self, n: int):
		assert isinstance(n, int)
		
		a = nx.algorithms.shortest_paths.single_source_bellman_ford_path_length(self.graph, n)
		arr = [0] * len(a)
		for v in a:
			arr[v] = a[v]
		return arr

	def getDistanceList(self, verties: list[int]):
		verties_distances = np.array([self.bellman(i) for i in verties])
		return np.min(verties_distances, axis=0)
	
	def weight(self, verties: list[int]) -> int:
		minimal_distances = self.getDistanceList(verties)
		return np.sum(minimal_distances)

	@lru_cache()
	def get_conjugate_vertices(self, n: int):
		neighbors = self.graph.neighbors(n)
		data: list[NeightborData] = []
		for i in neighbors:
			if i == n:
				continue
			edge_weight = self.graph.get_edge_data(n, i)['weight'] or float('inf')# type: ignore
			edge_data = NeightborData(i, edge_weight)
			data.append(edge_data)

		return data

	@staticmethod
	def random(n: int, m: int, max_weight: int = 100):
		base = Network(nx.gnm_random_graph(n, m, directed=True, seed=42))
		for e in base.graph.edges():
			base.graph[e[0]][e[1]]['weight'] = randint(1, max_weight)
		return base

	def draw(self):
		G = self.graph
		# pos=nx.spring_layout(G,'pos')
		# nx.draw_networkx(G,pos)
		# labels = nx.get_edge_attributes(G,'weight')
		# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
		nx.draw(G)


	def __len__(self):
		return self.graph.number_of_nodes()