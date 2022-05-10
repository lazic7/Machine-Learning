from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

X = generate_data(n_samples=500,flagc=1)
plt.figure(1)
plt.scatter(X[:,0], X[:,1])
plt.title("Podaci")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

model = KMeans(n_clusters=3)
model.fit(X)

plt.figure(2)
plt.title("Rezultat KMeans")
plt.xlabel("x1")
plt.ylabel("x2")
plt.scatter(X[:,0], X[:,1], c= model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], c = 'r', marker='x')
plt.show()

model = linkage(X,'average')

plt.figure(3)
dg = dendrogram(model)
plt.show()
