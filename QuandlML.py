import pandas as pd
import os
import quandl
import time


auth_tok = "sLhh2N3bVm9XsrQdaC6V"

# data = quandl.get("WIKI/AAPL", start_date="2000-12-12", end_date="2014-01-01", auth_token= auth_tok)

# print(data["Adj. Close"])

dirpath = os.path.dirname(__file__)
iQpath = os.path.join(dirpath, 'intraQuarter\\intraQuarter')

def Stock_Prices():
	df = pd.DataFrame()
	statspath = iQpath+"/_KeyStats"
	stock_list = [x[0] for x in os.walk(statspath)]

	for each_dir in stock_list[1:25]:
		try:
			ticker = each_dir.split("_KeyStats\\")[1]
			print(ticker)
			name = "WIKI/"+ticker.upper()
			data = quandl.get(name, start_date="2000-12-12", end_date="2014-01-01", auth_token= auth_tok)
			data[ticker.upper()] = data["Adj. Close"]
			print(data[ticker.upper()])
			time.sleep(5)
			df = pd.concat([df, data[ticker.upper()]], axis = 1) #add new column for each stock
		except Exception as e:
			print(str(e))

	df.to_csv("stock_prices2.csv")

Stock_Prices()