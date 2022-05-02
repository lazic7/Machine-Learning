import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

# url koji sadrzi xml datoteku s mjerenjima:
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=4&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = ur.urlopen(url).read()
root = ET.fromstring(airQualityHR)

df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

i = 0
while True:
    
    try:
        obj = root[i]
    except:
        break
    
    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
    df.mjerenje[i] = float(df.mjerenje[i])
    i = i + 1

df.vrijeme = pd.to_datetime(df.vrijeme, utc=True)
df.plot(y='mjerenje', x='vrijeme')
plt.show()

# add date month and day designator
df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek


#2. zadatak
print(df.sort_values(['mjerenje']).tail(3))

#3. zadatak ne znam drugacije
nanValues = []
x = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(1,13):
    nanValues.append(df[(df.month == i)].isnull().count()['mjerenje'])

plt.bar(x,nanValues)
plt.show()

#4 zadatak ne znam drugacije
df.boxplot(by='month', column='mjerenje')
plt.show()

#5 zadatak ne znam rijesiti