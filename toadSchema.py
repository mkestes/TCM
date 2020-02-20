import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('dataHPK.xlsx', sheet_name='Data')

# print column headings
#print ("Column headings:")
#print(df.columns)

# print specific column data (prints a snapshot)
#print(df['Customer No.'])

# iterate through the column and print contents (prints all contents)
#for i in df.index:
#	print(df['Customer No.'][i])

# create list of column Customer No and assign it a name. Then print
#listCustomerNo = df['Customer No.']
#print(listCustomerNo[0])


# define desired columns
date = df['Date']
customerNo = df['Customer No']
itemCode = df['Item Code']

# create pandas dataframe with desired columns
df = pd.DataFrame({date, customerNo, itemCode})

# write desired columns to new file and save
writer = ExcelWriter('myData.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()