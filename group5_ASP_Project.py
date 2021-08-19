import pandas as pd
data = pd.read_excel('IMVA.xls', sheet_name = 2)
print(data)

data.columns
print(data.columns)

asia = data['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand', 'Vietnam', 'Other Markets In Southeast Asia', 'Greater China', 'China', 'Hong Kong SAR', 'Taiwan', 'Other Markets In Greater China', 'North Asia', 'Japan', 'South Korea', 'Other Markets In North Asia', 'South Asia', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Other Markets In South Asia', 'West Asia', 'Iran', 'Israel', 'Kuwait', 'Saudi Arabia', 'United Arab Emirates']
print(data.columns)

asia = data(['Periods']).str.split

data.head(3)
print(data.head)






