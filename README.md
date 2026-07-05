# Dimensionality-Reduction-with-PCA

## 📌 Project Overview

This project demonstrates **Principal Component Analysis (PCA)** using the famous **Iris Dataset**.

PCA is an **unsupervised machine learning algorithm** used for:

- 📉 Reducing dimensionality
- 🚀 Improving computational efficiency
- 📊 Visualizing high-dimensional datasets
- 🎯 Preserving maximum variance

The project applies feature scaling, performs PCA to reduce the dataset from **4 dimensions to 2 principal components**, and visualizes the transformed data.

---

# 🚀 Project Workflow

```
Load Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Scaling
      │
      ▼
Principal Component Analysis
      │
      ▼
Transform Dataset
      │
      ▼
Explained Variance Analysis
      │
      ▼
2D Scatter Plot Visualization
```

---

# 📂 Dataset

Dataset Used:

- 🌸 Iris Dataset
- Source: Scikit-Learn

Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target Classes:

- Setosa
- Versicolor
- Virginica

---

# 🛠️ Technologies Used

- 🐍 Python
- 📊 Pandas
- 📈 Matplotlib
- 🤖 Scikit-Learn
- 📐 StandardScaler
- 📉 Principal Component Analysis (PCA)

---

# 📚 Libraries

```python
pandas
matplotlib
scikit-learn
```

Install using

```bash
pip install pandas matplotlib scikit-learn
```

---

# 📈 Steps Performed

## ✅ Load Iris Dataset

The Iris dataset is loaded from Scikit-Learn.

---

## ✅ Convert to DataFrame

The dataset is converted into a Pandas DataFrame for easier manipulation.

---

## ✅ Feature Scaling

StandardScaler is applied to normalize the features before PCA.

---

## ✅ Principal Component Analysis

PCA reduces the original 4 features into 2 Principal Components.

---

## ✅ Explained Variance

The explained variance ratio is calculated to understand how much information is retained.

---

## ✅ Data Visualization

A scatter plot visualizes the transformed data across the first two principal components.

---

# 📊 Output

The project generates:

- ✅ Scaled Dataset
- ✅ Principal Components
- ✅ Explained Variance Ratio
- ✅ PCA Component Matrix
- ✅ 2D Scatter Plot

---

# 📷 Sample Visualization

```
          PC2
           ▲

    ● ● ●
  ●       ●

           ▲

  ■ ■ ■ ■

            ▲

      ▲ ▲ ▲ ▲

────────────────────────► PC1
```

Each color represents one Iris species.

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

- ✅ What is Principal Component Analysis
- ✅ Why Feature Scaling is Important
- ✅ Eigenvectors and Principal Components
- ✅ Dimensionality Reduction
- ✅ Explained Variance Ratio
- ✅ Data Visualization using PCA

---

# 💡 Real-World Applications

- 📷 Image Compression
- 🧬 Bioinformatics
- 💰 Financial Analysis
- 🤖 Machine Learning
- 📊 Data Visualization
- 🧠 Pattern Recognition
- 🚗 Autonomous Vehicles
- 🏥 Healthcare Analytics

---

# 📁 Project Structure

```
PCA-on-Iris-Dataset/
│
├── PCA.py
├── README.md
└── requirements.txt
```

---

# ▶️ Run the Project

Clone the repository

Move into the project directory

```bash
cd PCA-on-Iris-Dataset
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python PCA.py
```

---

# ⭐ Future Improvements

- 📊 PCA with 3D Visualization
- 🌈 Interactive Plotly Charts
- 📉 Scree Plot
- 📈 Cumulative Explained Variance Graph
- 🔍 Compare PCA with t-SNE and UMAP
- 🤖 Apply PCA before Classification Models

---
