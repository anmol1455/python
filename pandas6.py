import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
from openpyxl.workbook import Workbook
data=pd.read_excel("data.xlsx","Sheet1")
#print(data)
w=ExcelWriter("data1.xlsx")
data.to_excel(w,"Sheet2",index=False)
w.save()
print("writing complete")
