"""
Reference Link: https://www.youtube.com/watch?v=Pe7dL-u7acI
Github Link: https://github.com/jg-fisher/k-means/blob/master/k_means.py
"""


import numpy as np
import operator
import matplotlib.pyplot as plt
import matplotlib.cm as cm

r = lambda: np.random.randint(1, 100)


class Centroid:
    """
    pos    = [x, y] coordinate array
    points = points assigned to centroid
    """

    def __init__(self, pos):
        self.pos = pos
        self.points = []
        self.previous_points = []
        self.color = None


class KMeans:
    """
    Unsupervised clustering algortihm.
    """

    def __init__(self, n_centroids=5):
        self.n_centroids = n_centroids
        self.centroids = []

        # generate initial centroids
        for _ in range(n_centroids):
            self.centroids.append(Centroid(np.array([r(), r()])))

        # assign a color to each centroid
        colors = cm.rainbow(np.linspace(0, 1, len(self.centroids)))
        for i, c in enumerate(self.centroids):
            c.color = colors[i]

    def sample_data(self, samples=50):
        """
        Generates sample data assings to self.X
        """
        self.X = [[r(), r()] for _ in range(samples)]

    def fit(self):
        """
        Fits points in self.X
        Assigns points to centroids.
        Calls to update centroid mean to reflect mean of assigned points.
        """
        self.n_iters = 0
        fit = False
        while not fit:
            for point in self.X:
                closest = self.assign_centroid(point)
                closest.points.append(point)

            # if length of array of centroids that did not change == number of centroids
            if len([c for c in self.centroids if c.points == c.previous_points]) == self.n_centroids:
                fit = True
                self._update_centroids(reset=False)
            else:
                self._update_centroids()

            self.n_iters += 1

    def assign_centroid(self, x):
        """
        Returns centroid closest to point.
        """
        distances = {}
        for centroid in self.centroids:
            distances[centroid] = np.linalg.norm(centroid.pos - x)
        closest = min(distances.items(), key=operator.itemgetter(1))[0]
        return closest

    def _update_centroids(self, reset=True):
        """
        Updates centroid position based on mean of assigned points.
        """
        for centroid in self.centroids:
            centroid.previous_points = centroid.points
            x_cor = [x[0] for x in centroid.points]
            y_cor = [y[1] for y in centroid.points]
            try:
                centroid.pos[0] = sum(x_cor) / len(x_cor)
                centroid.pos[1] = sum(y_cor) / len(y_cor)
            except:
                pass

            if reset:
                centroid.points = []

    def show(self):
        """
        Displays clustering, saves plot to {title}.png.
        """

        for i, c in enumerate(self.centroids):
            plt.scatter(c.pos[0], c.pos[1], marker='o', color=c.color, s=75)
            x_cors = [x[0] for x in c.points]
            y_cors = [y[1] for y in c.points]
            plt.scatter(x_cors, y_cors, marker='.', color=c.color)

        title = 'K-Means'
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()


if __name__ == '__main__':
    kmeans = KMeans(n_centroids=3)
    kmeans.sample_data()
    kmeans.fit()
    print('Iterations: {0}'.format(kmeans.n_iters))
    kmeans.show()