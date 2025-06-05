from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

X, _ = make_blobs(n_samples=300, centers=1, cluster_std=0.60, random_state=42)

rng = np.random.RandomState(42)
outliers = rng.uniform(low=-6, high=6, size=(20, 2))
X = np.concatenate([X, outliers], axis=0)

model = IsolationForest(contamination=0.06, random_state=42) 
model.fit(X)

y_pred = model.predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], c='blue', label='Normal')
plt.scatter(X[y_pred == -1][:, 0], X[y_pred == -1][:, 1], c='red', label='Anomaly')
plt.legend()
plt.title("Isolation Forest Anomaly Detection")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
#輸出解釋這段程式會產生：一群「正常」的點（藍色）一些「異常」的點（紅色），由模型自動判斷Isolation Forest 能在不需要標籤資料的情況下，找出資料中的異常行為，非常適合用於：信用卡詐騙偵測,網路入侵偵測,製造流程品質控管