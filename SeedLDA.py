import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# loadin the data and standardizing it
seedData = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)
seedFeatures = np.array(seedData.iloc[:,:7])
seedTargets = np.array(seedData.iloc[:,7]) - 1 # starting from zero
targetNames = ['Kama','Rosa','Canadian']
targetColors = ['red','blue','green']
seedFeaturesNorm = StandardScaler().fit_transform(seedFeatures)

X = seedFeaturesNorm
y = seedTargets

# Performing the linear discriminant analysis
seedLDA = LinearDiscriminantAnalysis(n_components=2)
X_LDA = seedLDA.fit_transform(X,y)

# Plotting the first and second LDs
plt.figure(figsize=[8,4])
# Plotting the first and second LDs
plt.scatter(X_LDA[:,0],X_LDA[:,1],c=y,marker='+')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.title('Linear discriminant analysis')
plt.show()
