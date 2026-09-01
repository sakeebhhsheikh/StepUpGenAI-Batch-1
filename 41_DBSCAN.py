import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_csv('datasets/iris.csv').iloc[:,1:]

# 1. Generate synthetic non-linear data (Two interlocking half-moons)
# X, y_true = make_moons(n_samples=300, noise=0.05, random_state=42)

X, y_true = df.iloc[:, :-1], df.iloc[:, -1]
# 2. Scale features (Crucial for DBSCAN as it relies on distance calculations)
X_scaled = StandardScaler().fit_transform(X)

# 3. Initialize and fit the DBSCAN model
# eps: radius of neighborhood; min_samples: minimum points to form a dense region
dbscan = DBSCAN(eps=0.3, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)

# 4. Extract insights and evaluation metrics
labels = dbscan.labels_
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)  # Exclude noise label (-1)
n_noise = list(labels).count(-1)                           # Outliers labeled as -1

print(f"Estimated number of clusters: {n_clusters}")
print(f"Estimated number of noise points: {n_noise}")

if n_clusters > 1:
    score = silhouette_score(X_scaled, labels)
    print(f"Silhouette Score: {score:.3f}")
else:
    print("Silhouette Score cannot be computed with fewer than 2 clusters.")

# 5. Visualize the clustering results
plt.figure(figsize=(8, 6))

# Highlight noise points in black, and use a colormap for distinct clusters
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1] # Black color assigned for noise/outliers

    class_member_mask = (labels == k)
    plt.scatter(
        X_scaled[class_member_mask, 0], 
        X_scaled[class_member_mask, 1], 
        c=[col], 
        edgecolor='k', 
        s=50, 
        label='Noise' if k == -1 else f'Cluster {k}'
    )

plt.title(f"DBSCAN Clustering (Found {n_clusters} Clusters)", fontsize=14)
plt.xlabel("Feature 1 (Scaled)")
plt.ylabel("Feature 2 (Scaled)")
plt.legend(loc="upper right")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()