import networkx as nx
import numpy as np

class Network:
	def __init__(self, matrix: list[list[float]] | np.ndarray) -> None:
		if isinstance(matrix, list):
			matrix = np.array(matrix)
		self.graph: nx.DiGraph = nx.from_numpy_matrix(matrix)

	def weight(self):
		s = 0
		a = nx.algorithms.shortest_paths.single_source_bellman_ford_path_length(self.graph, 0)
		return a