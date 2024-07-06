import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class AlwaysOneclassifier(BaseEstimator, ClassifierMixin):

    def __init__(self):
        pass

    def fit(self, X, y):
        return self
    
    def predict(self, X):
        return np.ones((X.shape[0],))
    
    def predict_proba(self, X):
        pass


class NearestCentroidClassifier(BaseEstimator, ClassifierMixin):

    def __init__(self):
        self.centroids_ = None
        self.classes_ = None

    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.centroids_ = np.zeros((len(self.classes_), X.shape[1]))

        for idx, cls in enumerate(self.classes_):
            self.centroids_[idx, :] = X[y==cls].mean(axis=0)

        return self

    def predict(self, X):
        distances = np.zeros((X.shape[0], len(self.classes_)))

        for idx, centroid in enumerate(self.centroids_):
            distances[:, idx] = np.linalg.norm(X - centroid, axis=1)

        return self.classes_[np.argmin(distances, axis=1)]
    

    def predict_proba(self, X):
        distances = np.zeros((X.shape[0], len(self.classes_)))

        for idx, centroid in enumerate(self.centroids_):
            distances[:, idx] = np.linalg.norm(X - centroid, axis=1)

        inv_distances = 1 / distances
        inv_distances_sum = np.sum(inv_distances, axis=1, keepdims=True)

        return inv_distances / inv_distances_sum

    
class MeanRegressor(BaseEstimator, RegressorMixin):
    def __init__(self):
        self.mean_ = None

    def fit(self, X, y):
        self.mean_ = np.mean(y)
        return self
    
    def predict(self, X):
        return np.full((X.shape[0],), self.mean_)


if __name__ == '__main__':
    # data = load_iris()

    data = fetch_california_housing()

    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    reg = MeanRegressor()

    reg.fit(X_train, y_train)

    print(reg.score(X_test, y_test))

    # # clf = AlwaysOneclassifier()

    # clf = NearestCentroidClassifier()

    # # clf = KNeighborsClassifier()

    # clf.fit(X_train, y_train)

    # print(clf.score(X_test, y_test))

    # print(clf.predict(np.array([X_test[0]])))

    # print(clf.predict_proba(np.array([X_test[0]])))

    reg = LinearRegression()

    reg.fit(X_train, y_train)

    print(reg.score(X_test, y_test))

