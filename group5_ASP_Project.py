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
