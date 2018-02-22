import sqlite3
import os
import pandas as pd
from os.path import join, dirname
from dotenv import find_dotenv, load_dotenv

class Analysis:

	def __init__(self):

		envPath = join(dirname(__file__), '.env')
		load_dotenv(envPath)
		db_file = os.environ['db_file']
		self.conn = sqlite3.connect(db_file)


	def find_general_sentiment(self):
		df = pd.read_sql_query("SELECT * from tweets", self.conn)
		return df["polarity"].mean()


	# Creates a new table in the DB which maps a user's tweet sentiments to the user
	def generate_user_sentiment(self):
		df = pd.read_sql_query("SELECT * from users LEFT JOIN tweets using (user_id)", self.conn)
		new_df = df.groupby(["user_id", "name"])["polarity"].mean()
		new_df.to_sql("user_sentiments", self.conn, if_exists="replace")

		