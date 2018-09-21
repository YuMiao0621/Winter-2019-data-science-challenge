import pandas as pd

data = pd.read_excel('/Users/joy/Desktop/Shopify_intern/2019Winter_Data_Science_Intern_Challenge_Data_Set.xlsx', sheetname='Sheet1')
order_amount = data['order_amount']

order_amounts = order_amount.tolist()
amount = sorted(order_amounts)

print('median: ', amount[len(order_amounts)/2 - 1])

print('Finish!')
