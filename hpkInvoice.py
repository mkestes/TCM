import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import Workbook
from pymongo import MongoClient
import xlwt




client = MongoClient('localhost', 27017)
db = client.shipped

# HpkInvoice = create_model(hpkInvoice, db['hpkInvoice'])

# read excel file and create dataframe = df
df = pd.read_excel('/Users/mk/tokul/TCM/Shipped/2020/raw/Hydrapak/invoice0122.xls',sheet_name='Sheet1')

# rename columns

df.rename(columns = {'Invoice':'orderNo',
					 'Date':'date',
					 'Customer No.':'accountFull',
					 'Item Code':'itemCode',
					 'Shipped':'qty',
					 'Revenue':'amount'},
		  inplace=True)


# use drop to eliminate desired columns

df.drop(['Salesperson', 'Unit Price', 'Year', 'Extra'], axis=1, inplace=True)

# write data into a new excel file

# writer = pd.ExcelWriter('/Users/mk/tokul/TCM/Shipped/2020/raw/adjusted/hpk.xls')
# df.to_excel(writer, sheet_name='Sheet1', index=False)
# writer.save()

holding = []

# iterate over rows with iterrows()
for row in df.itertuples():
	entry = {
		"orderNo": row[1],
		"date": row[2],
		"accountFull": row[3],
		"itemCode": row[4],
		"qty": row[6],
		"amount": row[7]
	}
	holding.append(entry) # append puts the next one at the end of the list

# print(len(holding)) # print the length of the list

try:
	result = db.data.insert_many(holding)
	print(result.inserted_ids)
except Exception as e:
	raise e
	






