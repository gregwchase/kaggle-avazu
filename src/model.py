# import h2o4gpu
import h2o
import pandas as pd

class Avazu():

	def __init__(self):
		self.test = None
		self.train = None


	def import_data(self, data_directory):
		"""
		Imports necesary data for training the model.

		INPUT
			data_directory: string of the data location

		OUTPUT
			H2O Frame
		"""
		return h2o.import_file(data_directory)


if __name__ == '__main__':


	avazu = Avazu()
	
	h2o.init()

	print("Importing Data")

	# train = avazu.import_data("../data/train.gz")
	test = avazu.import_data("../data/test.gz")

	print(test.head())