import pandas as pd
country = pd.read_excel('IMVA.xls', sheet_name = "IMVA")
print(country)

print(country.columns)

asia5 = country[['Periods','Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam','China','Hong Kong SAR','Taiwan','Japan','South Korea','Bangladesh','India','Pakistan','Sri Lanka','Iran','Israel','Kuwait','Saudi Arabia','United Arab Emirates']]
print(asia5.columns)
print(asia5)


date = asia5['Periods'].str.split(' ', n = 1, expand = True)
print(date)

asia5 = asia5.assign(year=date[0])

set1 = asia5[(asia5['year']) >= str(2011)]
print(set1)

print(set1.head(3))
print(set1.tail(3))

set2 = set1[['Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam','China','Hong Kong SAR','Taiwan','Japan','South Korea','Bangladesh','India','Pakistan','Sri Lanka','Iran','Israel','Kuwait','Saudi Arabia','United Arab Emirates']]
asia = set2.replace(',','', regex=True)
asia111 = asia.replace('na','0', regex=True)
print(asia)

asia1 = asia111.astype(int)
print(asia1.dtypes)
psNotSorted=asia1.sum()
print(psNotSorted)
psSorted = psNotSorted.sort_values(ascending=False)
print(psSorted)
print(psSorted.head(3))
print('The total no. of visitors for the top 3 countries is',sum(psSorted.head(3)))
print('The mean value for the top 3 countries is',round(sum(psSorted.head(3))/len(psSorted.head(3)),2))

import numpy as np
import matplotlib.pyplot as plt

ps = psNotSorted.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values/2500)
plt.xlabel("Countries", fontsize=10)
plt.ylabel("No. of Travellers (In thousands)", fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=80)
plt.title("All other countries from (Period:2011 - 2020 ", size=12)
plt.show();

ps = psNotSorted.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values/2500)
plt.xlabel("Countries", fontsize=10)
plt.ylabel("No. of Travellers (In thousands)", fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=80)
plt.title("All other countries from (Period:2011 - 2020 ", size=12)
print(psSorted.head(3))
plt.show();


