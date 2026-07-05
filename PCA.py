#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Data manipulation and analysis
import pandas as pd
# Data visualization
import matplotlib.pyplot as plt
# Load iris dataset
from sklearn.datasets import load_iris
# Feature scaling (Note: should be sklearn.preprocessing, not just preprocessing)
from sklearn.preprocessing import StandardScaler


# In[7]:


# Load the iris dataset from sklearn
iris = load_iris()
# Create a pandas DataFrame from the feature data
X = pd.DataFrame(iris.data)
# Extract the target labels
y = iris.target


# In[9]:


X.head()


# In[11]:


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# In[16]:


# Import PCA (Principal Component Analysis) from scikit-learn
from sklearn.decomposition import PCA

# Initialize PCA with 2 components to reduce dimensionality to 2D
pca = PCA(n_components = 2)

# Fit PCA to the scaled data and transform it to 2 principal components
X_pca = pca.fit_transform(X_scaled)


# In[20]:


X_pca.shape


# In[24]:


print("Explained Variance Ratio:", pca.explained_variance_ratio_)


# In[26]:


print(pca.components_)


# In[30]:


# Create a scatter plot using the first two principal components
plt.scatter(
    X_pca[:,0],  # First principal component (PC1) on x-axis
    X_pca[:,1],   # Second principal component (PC2) on y-axis
    c = y
)
# Set x-axis label to indicate first principal component
plt.xlabel("PC1")
# Set y-axis label to indicate second principal component
plt.ylabel("PC2")
# Add descriptive title for the PCA visualization
plt.title("PCA for iris dataset")


# In[ ]:




