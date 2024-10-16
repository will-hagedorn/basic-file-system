import table_pb2, table_pb2_grpc, grpc
from concurrent import futures
import os
import uuid
import pandas as pd
import pyarrow as pa
import pyarrow.csv as csv
import pyarrow.parquet as pq
import threading

# Global lock
globalLock = threading.Lock()

class MyTable(table_pb2_grpc.TableServicer):
	def __init__(self):
		self.filePaths = {}

	def ColSum(self, request, response):
		try:
			column = request.column
			format = request.format

			sum = 0

			# CSV summation over csv files
			if (format == "csv"):
				for x in self.filePaths:

					#  Access csv with lock
					with globalLock:
						csvFP = self.filePaths[x]["csv"]

					csv = pd.read_csv(csvFP)

					if column in csv.columns:
						sum += csv[column].sum()
			# Parquet summation over parquet files
			elif (format == "parquet"):
				for x in self.filePaths:

					# Access parquet with lock
					with globalLock:
						parquetFP = self.filePaths[x]["parquet"]

					# Only read necessary column
					try:
						parquet = pq.read_table(parquetFP, columns = [column])
						table  = parquet.to_pandas()

						sum += table[column].sum()
					except Exception as e:
						continue

			return table_pb2.ColSumResp(total = sum, error = "")
		except Exception as e:
			return table_pb2.ColSumResp(total = 0, error = str(e))


	def Upload(self, request, response):
		try:
			# Data in csv form
			csv_data = request.csv_data
			# Name of csv

			# Generates filename
			filename = str(uuid.uuid4())
			dir = f"{filename}Data"

			# Create data directory if it doesn't exist
			if not (os.path.exists(dir)):
				os.makedirs(dir)

			# Create file paths for csv and parquet
			csvFP = os.path.join(dir, f"{filename}.csv")
			parquetFP = os.path.join(dir, f"{filename}.parquet")

			# Write to csv
			with open(csvFP, "w") as csvFile:
				csvFile.write(csv_data)

			# Convert csv data to parquet
			dfP = csv.read_csv(csvFP)
			pq.write_table(dfP, parquetFP)

			# Add file paths to dictionary with lock
			with globalLock:
				self.filePaths[filename] = {
					"csv": csvFP,
					"parquet": parquetFP

				}

			return table_pb2.UploadResp(error = "")
		except Exception as e:
			return table_pb2.UploadResp(error = str(e))


def server():

	#Temp dummy port
	port = '5440'

	print("start server")
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=8), options=[("grpc.so_reuseport", 0)])

	table_pb2_grpc.add_TableServicer_to_server(MyTable(), server)

	server.add_insecure_port("[::]:" + str(port))
	server.start()
	print(f'Server started on port {port}')
	server.wait_for_termination()

if __name__ == "__main__":
	server()
