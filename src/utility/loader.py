import re
from os.path import isfile, splitext

class Loader:
	def __init__(self, path: str):
		assert isfile(path)
		path_tup = splitext(path)
		assert path_tup[-1] == '.txt'
		self.path = path

	def load(self):
		with open(self.path, 'r') as f:
			file_data = f.read()
			return self.__extract_data_from_string(file_data)

	def __extract_data_from_string(self, string: str):
		raw_table_match = re.search(r'table = {([.\n\s{0-9},]*)}', string)
		assert raw_table_match is not None
		row_table = raw_table_match.group(1)
		string_table_match: list[str] = re.findall(r'{([0-9\.\,\n]*)', row_table)
		float_table = [[float(j) for j in i.split(',')] for i in string_table_match]
		return float_table