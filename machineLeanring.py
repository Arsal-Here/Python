import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler,normalize
from sklearn.decomposition import PCA

creditcard_df = pd.read_csv("4.+Marketing_data.csv")

creditcard_df.loc[(creditcard_df['MINIMUM_PAYMENTS'].isnull()==True),'MINIMUM_PAYMENTS'] = creditcard_df['MINIMUM_PAYMENTS'].mean()
creditcard_df.loc[(creditcard_df['CREDIT_LIMIT'].isnull()==True),'CREDIT_LIMIT'] = creditcard_df['CREDIT_LIMIT'].mean()

creditcard_df.drop('CUST_ID',axis=1,inplace=True)

plt.figure(figsize=(25,50))



scaler = StandardScaler()
creditcard_df_scaled = scaler.fit_transform(creditcard_df)

scores_1=[]

range_values = range(1,20)

for i in range_values:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(creditcard_df_scaled)
    scores_1.append(kmeans.inertia_)

plt.plot(scores_1,'bx-')
plt.title('K Mean values')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS Scores')
#plt.show() 

kmeans = KMeans(8)
kmeans.fit(creditcard_df_scaled)
labels = kmeans.labels_

pca = PCA(n_components=2)
principal_comp = pca.fit_transform(creditcard_df_scaled)
print(principal_comp)

pca_df = pd.DataFrame(data=principal_comp,columns = ['pca1','pca2'])

pca_df = pd.concat([pca_df,pd.DataFrame({'cluster': labels})],axis=1)
plt.figure(figsize=(5,30))
ax = sns.scatterplot(data= pca_df,hue='cluster',x= 'pca1',y = 'pca2',palette=['black','red','blue','yellow','pink','purple','brown','green'])
plt.show()
