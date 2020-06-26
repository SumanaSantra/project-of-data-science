import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sbn
import warnings
warnings.filterwarnings('ignore')

hp = pd.read_csv('Happiness_data.csv',sep=",")

#print(hp.shape)
#print(hp.columns)
#print(hp.describe())
#print(hp.info())
#print(hp)

#hp.plot.hist(x = 'Country', y =['Social support','Freedom to make life choices'])
#hp.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)

'''sbn.lineplot(data=hp.drop(['Country','Score','Generosity'], axis=1))
plt.show()'''


'''print("avg Score: ", hp['Score'].mean())
print("99% country scores", hp['Score'].quantile(0.99))
print("Maximum Score: ", hp['Score'].max(),'Minimum Score : ',hp['Score'].min())'''


'''data = hp.copy()
data = data[data["Social support"] < hp['Social support'].quantile(0.99)]
plt.figure(figsize=(15,10))
plt.title("Social support Distribution", fontsize=20)
sbn.distplot(data['Social support'])
plt.show()'''


'''data = hp.copy()
data = data[data['Freedom to make life choices'] <= 0.5]
plt.figure(figsize=(15,10))
plt.title("Not free to live life", fontsize=20)
sbn.distplot(data['Freedom to make life choices'])
plt.show()'''

'''sbn.jointplot(x="Generosity", y="Social support", data=hp, height=5, ratio=10, color ='b')
plt.show()'''

'''data = hp.copy()
f, ax1 = plt.subplots(figsize=(20,10))
sbn.pointplot(x='Score', y='GDP per capita', data=data, color='b', alpha =0.8)
plt.xlabel("Score", fontsize=15)
plt.ylabel("GDP per capita", fontsize=15)
plt.title("Happiness ratio", fontsize=20, color='b')
plt.grid()
plt.show()'''
