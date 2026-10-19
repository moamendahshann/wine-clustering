import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score
X,y=load_wine(return_X_y=True)
Z=StandardScaler().fit_transform(X)
scores={}; labels={}
for k in range(2,7):
 labels[k]=KMeans(n_clusters=k,n_init=20,random_state=42).fit_predict(Z)
 scores[k]=silhouette_score(Z,labels[k])
best=max(scores,key=scores.get)
metrics={"samples":len(X),"selected_k":best,"silhouette_by_k":scores,"adjusted_rand_vs_reference":adjusted_rand_score(y,labels[best])}
xy=PCA(n_components=2).fit_transform(Z)
plt.scatter(xy[:,0],xy[:,1],c=labels[best],cmap="viridis",s=30)
plt.xlabel("Principal component 1");plt.ylabel("Principal component 2");plt.title(f"Wine data: {best} exploratory clusters")
plt.tight_layout();plt.savefig(OUT/"clusters.png",dpi=160);plt.close()

(OUT/"metrics.json").write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics,indent=2))
