import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import Workbook


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

# use .loc to slice out desired columns
# rename to grouped dataframe = gdf
#gdf = df.loc[:,['orderNo','date','account','style','qty','amount','itemCode']]

# OR

# use drop() to drop desired columns
# rename to grouped dataframe = gdf

df.drop(['Salesperson', 'Unit Price', 'Year', 'Extra'], axis=1, inplace=True)

# write grouped data into a new excel file
writer = ExcelWriter('/Users/mk/tokul/TCM/Shipped/2020/raw/adjusted/hpk.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

